import os
from datetime import datetime
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message, CallbackQuery, FSInputFile,
    InlineKeyboardMarkup, InlineKeyboardButton,
)
from aiogram.fsm.context import FSMContext

from ..verification.dadata import DaDataProvider
from ..services.contract_builder import render_text, text_to_docx, text_to_pdf
from ..models.contract import ContractInput, ContractParams
from ..models.party import Party
from .states import ContractFSM
from .keyboards import (
    reply_start_kb, reply_main_menu_kb, reply_remove,
    choose_contract_type_kb, choose_output_kb, confirm_kb
)

router = Router()

# ----------------- helpers for /checkinn -----------------

def _fmt_date_ms(v) -> str:
    if not v:
        return "-"
    try:
        iv = int(v)
        if iv < 10_000_000_000:
            iv *= 1000
        return datetime.utcfromtimestamp(iv / 1000).strftime("%d.%m.%Y")
    except Exception:
        return "-"

def _after_check_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="В главное меню", callback_data="check_home")],
        [InlineKeyboardButton(text="Новая проверка", callback_data="check_new")],
        [InlineKeyboardButton(text="Выход", callback_data="check_exit")],
    ])

def _format_report(d: dict) -> str:
    management = d.get("management") or "-"
    if ":" in management:
        management = management.replace(":", ",", 1)
    opf = d.get("opf_full") or d.get("opf_short") or "-"
    status = (d.get("status") or "-").upper()
    reg = _fmt_date_ms(d.get("registration_date") or d.get("ogrn_date"))
    liq = _fmt_date_ms(d.get("liquidation_date"))
    okved = d.get("okved") or {}
    okved_code = okved.get("code")
    okved_name = okved.get("name") or "-"
    okved_line = f"{okved_code} — {okved_name}" if okved_code else "-"
    phones = ", ".join(d.get("phones") or []) or "-"
    emails = ", ".join(d.get("emails") or []) or "-"
    website = d.get("website") or "-"

    txt = (
        f"🧾 <b>{d.get('name') or '-'}</b>\n"
        f"ОПФ: {opf}\n"
        f"Статус: {status}\n"
        f"Дата регистрации: {reg}" + (f" • Ликвидация: {liq}" if liq != "-" else "") + "\n"
        f"ИНН/КПП: {d.get('inn') or '-'} / {d.get('kpp') or '-'}\n"
        f"ОГРН: {d.get('ogrn') or '-'}\n"
        f"Адрес: {d.get('address') or '-'}\n"
        f"Руководитель: {management}\n"
        f"ОКВЭД (осн.): {okved_line}\n"
        f"Сайт: {website}\n"
        f"Тел.: {phones}\n"
        f"Email: {emails}"
    )
    return txt

# ----------------- Reply-клавиатуры: Старт → Главное меню -----------------

@router.message(CommandStart())
async def cmd_start(m: Message, state: FSMContext):
    await state.clear()
    await m.answer(
        "Привет! Нажми кнопку <b>Старт</b> ниже, чтобы открыть меню.",
        reply_markup=reply_start_kb()
    )

@router.message(F.text.casefold() == "старт")
async def on_start_pressed(m: Message, state: FSMContext):
    await state.clear()
    await m.answer(
        "Выберите действие:",
        reply_markup=reply_main_menu_kb()
    )

@router.message(F.text.casefold() == "запрос по инн")
async def on_check_menu(m: Message, state: FSMContext):
    await state.clear()
    await m.answer(
        "Отправьте команду:\n"
        "<code>/checkinn ИНН [КПП]</code>\n\n"
        "Например: <code>/checkinn 7707083893</code>",
    )

@router.message(F.text.casefold() == "договор")
async def on_contract_menu(m: Message, state: FSMContext):
    await state.set_state(ContractFSM.contract_type)
    await m.answer(
        "Выберите тип договора:",
        reply_markup=choose_contract_type_kb()
    )

@router.message(F.text.casefold() == "выход")
async def on_exit(m: Message, state: FSMContext):
    await state.clear()
    await m.answer(
        "Спасибо за использование! Чтобы начать заново — /start",
        reply_markup=reply_remove()
    )

# ----------------- FSM поток «Договор» (как раньше) -----------------

@router.callback_query(ContractFSM.contract_type, F.data.startswith("type_"))
async def set_type(c: CallbackQuery, state: FSMContext):
    await state.update_data(contract_type="services")
    await c.message.edit_text("Введите полное наименование Заказчика:")
    await state.set_state(ContractFSM.customer_name)
    await c.answer()

@router.message(ContractFSM.customer_name)
async def customer_name(m: Message, state: FSMContext):
    await state.update_data(customer_name=m.text.strip())
    await m.answer("ИНН Заказчика:")
    await state.set_state(ContractFSM.customer_inn)

@router.message(ContractFSM.customer_inn)
async def customer_inn(m: Message, state: FSMContext):
    await state.update_data(customer_inn=m.text.strip())
    await m.answer("КПП Заказчика (если есть) или '-' :")
    await state.set_state(ContractFSM.customer_kpp)

@router.message(ContractFSM.customer_kpp)
async def customer_kpp(m: Message, state: FSMContext):
    kpp = None if m.text.strip() == '-' else m.text.strip()
    await state.update_data(customer_kpp=kpp)
    await m.answer("Полное наименование Исполнителя:")
    await state.set_state(ContractFSM.contractor_name)

@router.message(ContractFSM.contractor_name)
async def contractor_name(m: Message, state: FSMContext):
    await state.update_data(contractor_name=m.text.strip())
    await m.answer("ИНН Исполнителя:")
    await state.set_state(ContractFSM.contractor_inn)

@router.message(ContractFSM.contractor_inn)
async def contractor_inn(m: Message, state: FSMContext):
    await state.update_data(contractor_inn=m.text.strip())
    await m.answer("КПП Исполнителя (если есть) или '-' :")
    await state.set_state(ContractFSM.contractor_kpp)

@router.message(ContractFSM.contractor_kpp)
async def contractor_kpp(m: Message, state: FSMContext):
    kpp = None if m.text.strip() == '-' else m.text.strip()
    await state.update_data(contractor_kpp=kpp)
    await m.answer("Номер договора:")
    await state.set_state(ContractFSM.params_number)

@router.message(ContractFSM.params_number)
async def params_number(m: Message, state: FSMContext):
    await state.update_data(number=m.text.strip())
    await m.answer("Дата (напр. 30.09.2025):")
    await state.set_state(ContractFSM.params_date)

@router.message(ContractFSM.params_date)
async def params_date(m: Message, state: FSMContext):
    await state.update_data(date=m.text.strip())
    await m.answer("Город заключения:")
    await state.set_state(ContractFSM.params_city)

@router.message(ContractFSM.params_city)
async def params_city(m: Message, state: FSMContext):
    await state.update_data(city=m.text.strip())
    await m.answer("Опишите предмет договора:")
    await state.set_state(ContractFSM.params_subject)

@router.message(ContractFSM.params_subject)
async def params_subject(m: Message, state: FSMContext):
    await state.update_data(subject=m.text.strip())
    await m.answer("Стоимость (с валютой):")
    await state.set_state(ContractFSM.params_price)

@router.message(ContractFSM.params_price)
async def params_price(m: Message, state: FSMContext):
    await state.update_data(price=m.text.strip())
    await m.answer("Порядок расчетов:")
    await state.set_state(ContractFSM.params_payment)

@router.message(ContractFSM.params_payment)
async def params_payment(m: Message, state: FSMContext):
    await state.update_data(payment=m.text.strip())
    await m.answer("Срок исполнения/действия:")
    await state.set_state(ContractFSM.params_term)

@router.message(ContractFSM.params_term)
async def params_term(m: Message, state: FSMContext):
    await state.update_data(term=m.text.strip())
    await m.answer("Штрафные санкции (или '-' ):")
    await state.set_state(ContractFSM.params_penalties)

@router.message(ContractFSM.params_penalties)
async def params_penalties(m: Message, state: FSMContext):
    penalties = None if m.text.strip() == '-' else m.text.strip()
    await state.update_data(penalties=penalties)
    await m.answer("Выберите формат файла:", reply_markup=choose_output_kb())
    await state.set_state(ContractFSM.output_format)

@router.callback_query(ContractFSM.output_format, F.data.startswith("out_"))
async def output_choice(c: CallbackQuery, state: FSMContext):
    mapping = {"out_docx": "docx", "out_pdf": "pdf", "out_both": "both"}
    await state.update_data(output=mapping[c.data])
    await c.message.edit_text(
        "Проверяю реквизиты и готовлю предпросмотр... Подтвердите формирование:",
        reply_markup=confirm_kb()
    )
    await state.set_state(ContractFSM.confirm)
    await c.answer()

@router.callback_query(ContractFSM.confirm, F.data == "confirm_yes")
async def do_generate(c: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    provider = DaDataProvider()
    customer_v = await provider.verify(inn=data["customer_inn"], kpp=data.get("customer_kpp"))
    contractor_v = await provider.verify(inn=data["contractor_inn"], kpp=data.get("contractor_kpp"))

    vr = {
        "customer": customer_v,
        "contractor": contractor_v,
        "match": (customer_v.get("found") and contractor_v.get("found"))
    }

    ci = ContractInput(
        contract_type="services",
        customer=Party(name=data["customer_name"], inn=data["customer_inn"], kpp=data.get("customer_kpp")),
        contractor=Party(name=data["contractor_name"], inn=data["contractor_inn"], kpp=data.get("contractor_kpp")),
        params=ContractParams(
            number=data["number"], date=data["date"], city=data["city"],
            subject=data["subject"], price=data["price"], payment_terms=data["payment"],
            term=data["term"], penalties=data.get("penalties")
        ),
        output=data["output"],
        verification_report=vr
    )

    context = {
        "number": ci.params.number,
        "date": ci.params.date,
        "city": ci.params.city,
        "subject": ci.params.subject,
        "price": ci.params.price,
        "payment_terms": ci.params.payment_terms,
        "term": ci.params.term,
        "jurisdiction": ci.params.jurisdiction,
        "penalties": ci.params.penalties,
        "customer": ci.customer.model_dump(),
        "contractor": ci.contractor.model_dump(),
        "verification_status": "OK" if vr.get("match") else "требуется проверка вручную"
    }

    text = render_text(context)

    files = []
    os.makedirs("out", exist_ok=True)
    if ci.output in ("docx", "both"):
        path_docx = f"out/contract_{ci.params.number}.docx"
        text_to_docx(text, path_docx)
        files.append(FSInputFile(path_docx))
    if ci.output in ("pdf", "both"):
        path_pdf = f"out/contract_{ci.params.number}.pdf"
        text_to_pdf(text, path_pdf)
        files.append(FSInputFile(path_pdf))

    await c.message.answer("Готово. Вот файлы:")
    for f in files:
        await c.message.answer_document(f)

    def line(v):
        if not v.get("found"):
            return "не найден"
        return f"{v.get('name')} | ИНН {v.get('inn')} | ОГРН {v.get('ogrn')} | статус: {v.get('status')}"

    await c.message.answer(
        "Проверка контрагентов:\n"+
        f"Заказчик: {line(customer_v)}\n"+
        f"Исполнитель: {line(contractor_v)}"
    )

    await state.clear()
    await c.answer()

@router.callback_query(ContractFSM.confirm, F.data == "confirm_no")
async def cancel(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text("Ок, отменил. /start заново")
    await c.answer()

# ----------------- /checkinn (быстрый режим без FSM) -----------------

@router.message(Command("checkinn"))
async def cmd_checkinn(m: Message):
    parts = (m.text or "").split()
    args = parts[1:] if len(parts) > 1 else []
    if not args:
        await m.answer(
            "Отправьте команду в формате:\n"
            "<code>/checkinn ИНН [КПП]</code>\n\n"
            "Например: <code>/checkinn 7707083893</code>"
        )
        return

    inn = "".join(ch for ch in args[0] if ch.isdigit())
    kpp = "".join(ch for ch in (args[1] if len(args) > 1 else "")) or None

    if len(inn) not in (10, 12):
        await m.answer("ИНН должен содержать 10 или 12 цифр. Попробуйте снова.")
        return

    provider = DaDataProvider()
    info = await provider.verify(inn=inn, kpp=kpp)

    if not info.get("found"):
        await m.answer("Компания не найдена по указанному ИНН.", reply_markup=_after_check_kb())
        return

    await m.answer(_format_report(info), reply_markup=_after_check_kb())

@router.callback_query(F.data == "check_home")
async def check_home(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text(
        "Привет! Нажмите «Старт» ниже, чтобы открыть меню.",
    )
    await c.message.answer("Меню:", reply_markup=reply_main_menu_kb())
    await c.answer()

@router.callback_query(F.data == "check_new")
async def check_new(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text(
        "Отправьте новый запрос в формате:\n"
        "<code>/checkinn ИНН [КПП]</code>\n\n"
        "Например: <code>/checkinn 7707083893</code>"
    )
    await c.answer()

@router.callback_query(F.data == "check_exit")
async def check_exit(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text("Спасибо за использование! Чтобы начать заново — /start")
    await c.answer()