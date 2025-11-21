from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from datetime import datetime
import os

from ..verification.dadata import DaDataProvider
from ..services.contract_builder import render_text, text_to_docx, text_to_pdf
from ..services.flexoprint_contract import generate_flexoprint_contract
from ..models.contract import ContractInput, ContractParams
from ..models.party import Party
from .states import ContractFSM, CheckFSM, FlexFSM
from .keyboards import (
    main_menu_kb,
    payment_menu_kb,
    after_check_kb,
    choose_output_kb,
    confirm_kb,
)

router = Router()

# -------- helpers --------

def _fmt_date_ms(v) -> str:
    if not v:
        return "-"
    try:
        return datetime.fromtimestamp(int(v) / 1000).strftime("%d.%m.%Y")
    except Exception:
        return str(v)

def _our_entity_from_env() -> Party:
    return Party(
        name=os.getenv("OUR_NAME", "ООО «ФЛЕКСПРИНТ»"),
        inn=os.getenv("OUR_INN", "0000000000"),
        kpp=os.getenv("OUR_KPP", None),
        ogrn=os.getenv("OUR_OGRN", None),
        address=os.getenv("OUR_ADDRESS", None),
        bank_name=os.getenv("OUR_BANK_NAME", None),
        bank_bik=os.getenv("OUR_BANK_BIK", None),
        bank_account=os.getenv("OUR_BANK_ACC", None),
        bank_corr=os.getenv("OUR_BANK_CORR", None),
    )

# -------- Старт / главное меню --------

@router.message(CommandStart())
async def start(m: Message, state: FSMContext):
    await state.clear()
    await m.answer(
        "Привет! Я помогу тебе составить договор или получить данные о контрагенте по ИНН.",
        reply_markup=main_menu_kb(),
    )

# -------- Главное меню: компании --------

@router.callback_query(F.data == "menu_flexoprint")
async def menu_flexoprint(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.update_data(company="flexoprint")
    await c.message.edit_text("Выбери условия оплаты для «Флексопринт»:", reply_markup=payment_menu_kb())
    await c.answer()

@router.callback_query(F.data == "menu_flexograph")
async def menu_flexograph(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.update_data(company="flexograph")
    await c.message.edit_text("Выбери условия оплаты для «Флексограф»:", reply_markup=payment_menu_kb())
    await c.answer()

@router.callback_query(F.data == "menu_doctorprint")
async def menu_doctorprint(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.update_data(company="doctorprint")
    await c.message.edit_text("Выбери условия оплаты для «Докторпринт»:", reply_markup=payment_menu_kb())
    await c.answer()

# -------- Меню оплаты: новый упрощенный поток для Флексопринт --------

@router.callback_query(F.data.in_(["pay_prepay", "pay_delay", "pay_5050"]))
async def payment_selected(c: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    company = data.get("company")
    code_map = {"pay_prepay": "prepay", "pay_delay": "delay", "pay_5050": "5050"}
    payment_form = code_map[c.data]

    if company == "flexoprint":
        await state.update_data(payment_form=payment_form)
        await c.message.edit_text(
            "Введите ИНН контрагента (10 или 12 цифр). "
            "Я найду сведения через DaData и подставлю их в договор."
        )
        await state.set_state(FlexFSM.wait_inn)
    else:
        # Пока для других компаний оставим заглушку
        await state.clear()
        await c.message.edit_text("ТЕСТ_ТЕСТ_ТЕСТ\n\nСпасибо за использование! Для возврата — /start")
    await c.answer()

@router.message(FlexFSM.wait_inn)
async def fp_wait_inn(m: Message, state: FSMContext):
    inn = "".join(ch for ch in (m.text or "") if ch.isdigit())
    if len(inn) not in (10, 12):
        await m.answer("ИНН должен содержать 10 или 12 цифр. Повторите ввод:")
        return

    provider = DaDataProvider()
    info = await provider.verify(inn=inn)

    if not info.get("found"):
        await m.answer("Компания не найдена по указанному ИНН. Введите другой ИНН:")
        return

    # Сохраним краткие сведения контрагента и сырой JSON DaData в состояние
    await state.update_data(
        cp=dict(
            name=info.get("name"),
            inn=info.get("inn"),
            kpp=info.get("kpp"),
            ogrn=info.get("ogrn"),
            address=info.get("address"),
        ),
        cp_dadata=info.get("dadata") or {},
    )

    # Показать предпросмотр и запросить фамилию менеджера
    preview = (
        f"Найдено:\n"
        f"<b>{info.get('name') or '-'}</b>\n"
        f"ИНН/КПП: {info.get('inn') or '-'} / {info.get('kpp') or '-'}\n"
        f"ОГРН: {info.get('ogrn') or '-'}\n"
        f"Адрес: {info.get('address') or '-'}\n\n"
        f"Введите фамилию менеджера, ответственного за договор:"
    )
    await m.answer(preview)
    await state.set_state(FlexFSM.wait_manager)

@router.message(FlexFSM.wait_manager)
async def fp_wait_manager(m: Message, state: FSMContext):
    manager = (m.text or "").strip()
    if not manager:
        await m.answer("Введите фамилию менеджера (только текст):")
        return

    data = await state.get_data()
    cp = data.get("cp") or {}
    cp_dadata = data.get("cp_dadata") or {}
    payment_form = data.get("payment_form")

    # Формируем стороны
    our = _our_entity_from_env()
    counterparty = Party(
        name=cp.get("name", "-"),
        inn=cp.get("inn", "-"),
        kpp=cp.get("kpp"),
        ogrn=cp.get("ogrn"),
        address=cp.get("address"),
    )

    # Дата берётся автоматически (сегодня) — по ТЗ вводим только ИНН и фамилию менеджера
    today_str = datetime.now().strftime("%d.%m.%Y")

    try:
        result = generate_flexoprint_contract(
            template_path="templates/ШАБЛОН_ФЛЕКСПРИНТ_100.docx",
            date_value=today_str,
            payment_form=payment_form,
            counterparty=counterparty,
            our_entity=our,
            manager_surname=manager,
            cp_dadata=cp_dadata,  # ← добавили «сырые» данные DaData для шаблона
            extra={"source": "telegram", "auto_filled": True},
        )
    except Exception as e:
        await m.answer(
            f"Не удалось сформировать договор: {e}\n"
            f"Проверьте наличие шаблона в папке templates и установки docxtpl."
        )
        await state.clear()
        return

    await m.answer(
        f"✅ Готово!\n"
        f"<b>{result['title']}</b>\n"
        f"Полный номер: {result['full_number']}\n"
        f"Оплата: {payment_form}\n"
        f"Файл сформирован и сохранён."
    )
    try:
        await m.answer_document(FSInputFile(result["path"]))
    except Exception:
        await m.answer(f"Путь к файлу: <code>{result['path']}</code>")

    await state.clear()
    await m.answer("Вернуться в главное меню?", reply_markup=main_menu_kb())

# -------- Проверка компании по ИНН (кнопка в меню) --------

@router.callback_query(F.data == "menu_checkinn")
async def menu_checkinn(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text("Введите ИНН (10 или 12 цифр) или 'ИНН КПП' через пробел:")
    await state.set_state(CheckFSM.wait_inn)
    await c.answer()

# -------- Проверка компании по ИНН (команда) --------

@router.message(Command("checkinn"))
async def checkinn_start(m: Message, state: FSMContext):
    await state.clear()
    await m.answer("Введите ИНН (10 или 12 цифр) или 'ИНН КПП' через пробел:")
    await state.set_state(CheckFSM.wait_inn)

@router.message(CheckFSM.wait_inn)
async def checkinn_process(m: Message, state: FSMContext):
    parts = (m.text or "").split()
    inn = "".join(ch for ch in (parts[0] if parts else "") if ch.isdigit())
    kpp = "".join(ch for ch in (parts[1] if len(parts) > 1 else "") if ch.isdigit()) or None

    if len(inn) not in (10, 12):
        await m.answer("ИНН должен содержать 10 или 12 цифр. Попробуйте снова или /checkinn для перезапуска.")
        return

    provider = DaDataProvider()
    data = await provider.verify(inn=inn, kpp=kpp)

    if not data.get("found"):
        await m.answer("Компания не найдена по указанному ИНН.", reply_markup=after_check_kb())
    else:
        okved = data.get("okved") or {}
        okved_code = okved.get("code")
        okved_name = okved.get("name") or "-"
        okved_line = f"{okved_code} — {okved_name}" if okved_code else "-"

        phones = ", ".join(data.get("phones") or []) or "-"
        emails = ", ".join(data.get("emails") or []) or "-"
        website = data.get("website") or "-"
        opf = data.get("opf_full") or data.get("opf_short") or "-"
        status = data.get("status") or "-"

        reg = _fmt_date_ms(data.get("registration_date") or data.get("ogrn_date"))
        liq = _fmt_date_ms(data.get("liquidation_date"))

        management_raw = data.get("management") or "-"
        management = management_raw.replace(":", ",", 1) if ":" in management_raw else management_raw

        txt = (
            f"🧾 <b>{data.get('name') or '-'}</b>\n"
            f"ОПФ: {opf}\n"
            f"Статус: {status}\n"
            f"Дата регистрации: {reg}" + (f" • Ликвидация: {liq}" if liq != "-" else "") + "\n"
            f"ИНН/КПП: {data.get('inn') or '-'} / {data.get('kpp') or '-'}\n"
            f"ОГРН: {data.get('ogrn') or '-'}\n"
            f"Адрес: {data.get('address') or '-'}\n"
            f"Руководитель: {management}\n"
            f"ОКВЭД (осн.): {okved_line}\n"
            f"Сайт: {website}\n"
            f"Тел.: {phones}\n"
            f"Email: {emails}"
        )
        await m.answer(txt, reply_markup=after_check_kb())
    await state.clear()

# -------- Пост-отчётные кнопки --------

@router.callback_query(F.data == "check_home")
async def check_home(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text(
        "Привет! Я помогу тебе составить договор или получить данные о контрагенте по ИНН.",
        reply_markup=main_menu_kb(),
    )
    await c.answer()

@router.callback_query(F.data == "check_new")
async def check_new(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text("Введите ИНН (10 или 12 цифр) или 'ИНН КПП' через пробел:")
    await state.set_state(CheckFSM.wait_inn)
    await c.answer()

@router.callback_query(F.data == "check_exit")
async def check_exit(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text("Спасибо за использование! Чтобы начать заново — /start")
    await c.answer()

# -------- Ниже остаётся мастер генерации старого вида (не используется из главного меню) --------

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
        reply_markup=confirm_kb(),
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
        "match": (customer_v.get("found") and contractor_v.get("found")),
    }

    ci = ContractInput(
        contract_type="services",
        customer=Party(name=data["customer_name"], inn=data["customer_inn"], kpp=data.get("customer_kpp")),
        contractor=Party(name=data["contractor_name"], inn=data["contractor_inn"], kpp=data.get("contractor_kpp")),
        params=ContractParams(
            number=data["number"], date=data["date"], city=data["city"],
            subject=data["subject"], price=data["price"], payment_terms=data["payment"],
            term=data["term"], penalties=data.get("penalties"),
        ),
        output=data["output"],
        verification_report=vr,
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
        "verification_status": "OK" if vr.get("match") else "требуется проверка вручную",
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
        "Проверка контрагентов:\n"
        f"Заказчик: {line(customer_v)}\n"
        f"Исполнитель: {line(contractor_v)}"
    )

    await state.clear()
    await c.answer()

@router.callback_query(ContractFSM.confirm, F.data == "confirm_no")
async def cancel(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text("Ок, отменил. /start заново")
    await c.answer()