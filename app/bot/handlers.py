import os
import asyncio
from datetime import datetime
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from ..services.contract_builder import render_text, text_to_docx, text_to_pdf
from ..models.contract import ContractInput, ContractParams
from ..models.party import Party
from .states import ContractFSM
from .keyboards import (
    reply_start_kb, reply_main_menu_kb, reply_remove,
    choose_contract_type_kb, choose_output_kb, confirm_kb
)

router = Router()  # корневой роутер бота

# Подключаем подроутер проверки по ИНН
from .checkinn import router as checkinn_router
router.include_router(checkinn_router)

# ---------- утилита надёжной отправки ----------
async def _try_send(coro_factory, retries: int = 3, backoff: float = 1.0):
    last_exc = None
    for i in range(retries):
        try:
            return await coro_factory()
        except Exception as e:
            last_exc = e
            await asyncio.sleep(backoff * (i + 1))
    raise last_exc

# ---------- старт и главное меню ----------
@router.message(CommandStart())
async def cmd_start(m: Message, state: FSMContext):
    await state.clear()
    await _try_send(lambda: m.answer(
        "Привет! Нажми кнопку <b>Старт</b> ниже, чтобы открыть меню.",
        reply_markup=reply_start_kb()
    ))

@router.message(F.text.casefold() == "старт")
async def on_start_pressed(m: Message, state: FSMContext):
    await state.clear()
    await _try_send(lambda: m.answer(
        "Выберите действие:",
        reply_markup=reply_main_menu_kb()
    ))

@router.message(F.text.casefold() == "договор")
async def on_contract_menu(m: Message, state: FSMContext):
    await state.set_state(ContractFSM.contract_type)
    await _try_send(lambda: m.answer(
        "Выберите тип договора:",
        reply_markup=choose_contract_type_kb()
    ))

@router.message(F.text.casefold() == "выход")
async def on_exit(m: Message, state: FSMContext):
    await state.clear()
    await _try_send(lambda: m.answer(
        "Спасибо за использование! Чтобы начать заново — /start",
        reply_markup=reply_remove()
    ))

# ---------- FSM поток «Договор» ----------
@router.callback_query(ContractFSM.contract_type, F.data.startswith("type_"))
async def set_type(c: CallbackQuery, state: FSMContext):
    await state.update_data(contract_type="services")
    await _try_send(lambda: c.message.answer("Введите полное наименование Заказчика:"))
    await state.set_state(ContractFSM.customer_name)
    await c.answer()

@router.message(ContractFSM.customer_name)
async def customer_name(m: Message, state: FSMContext):
    await state.update_data(customer_name=m.text.strip())
    await _try_send(lambda: m.answer("ИНН Заказчика:"))
    await state.set_state(ContractFSM.customer_inn)

@router.message(ContractFSM.customer_inn)
async def customer_inn(m: Message, state: FSMContext):
    await state.update_data(customer_inn=m.text.strip())
    await _try_send(lambda: m.answer("КПП Заказчика (если есть) или '-' :"))
    await state.set_state(ContractFSM.customer_kpp)

@router.message(ContractFSM.customer_kpp)
async def customer_kpp(m: Message, state: FSMContext):
    kpp = None if m.text.strip() == '-' else m.text.strip()
    await state.update_data(customer_kpp=kpp)
    await _try_send(lambda: m.answer("Полное наименование Исполнителя:"))
    await state.set_state(ContractFSM.contractor_name)

@router.message(ContractFSM.contractor_name)
async def contractor_name(m: Message, state: FSMContext):
    await state.update_data(contractor_name=m.text.strip())
    await _try_send(lambda: m.answer("ИНН Исполнителя:"))
    await state.set_state(ContractFSM.contractor_inn)

@router.message(ContractFSM.contractor_inn)
async def contractor_inn(m: Message, state: FSMContext):
    await state.update_data(contractor_inn=m.text.strip())
    await _try_send(lambda: m.answer("КПП Исполнителя (если есть) или '-' :"))
    await state.set_state(ContractFSM.contractor_kpp)

@router.message(ContractFSM.contractor_kpp)
async def contractor_kpp(m: Message, state: FSMContext):
    kpp = None if m.text.strip() == '-' else m.text.strip()
    await state.update_data(contractor_kpp=kpp)
    await _try_send(lambda: m.answer("Номер договора:"))
    await state.set_state(ContractFSM.params_number)

@router.message(ContractFSM.params_number)
async def params_number(m: Message, state: FSMContext):
    await state.update_data(number=m.text.strip())
    await _try_send(lambda: m.answer("Дата (напр. 30.09.2025):"))
    await state.set_state(ContractFSM.params_date)

@router.message(ContractFSM.params_date)
async def params_date(m: Message, state: FSMContext):
    await state.update_data(date=m.text.strip())
    await _try_send(lambda: m.answer("Город заключения:"))
    await state.set_state(ContractFSM.params_city)

@router.message(ContractFSM.params_city)
async def params_city(m: Message, state: FSMContext):
    await state.update_data(city=m.text.strip())
    await _try_send(lambda: m.answer("Опишите предмет договора:"))
    await state.set_state(ContractFSM.params_subject)

@router.message(ContractFSM.params_subject)
async def params_subject(m: Message, state: FSMContext):
    await state.update_data(subject=m.text.strip())
    await _try_send(lambda: m.answer("Стоимость (с валютой):"))
    await state.set_state(ContractFSM.params_price)

@router.message(ContractFSM.params_price)
async def params_price(m: Message, state: FSMContext):
    await state.update_data(price=m.text.strip())
    await _try_send(lambda: m.answer("Порядок расчетов:"))
    await state.set_state(ContractFSM.params_payment)

@router.message(ContractFSM.params_payment)
async def params_payment(m: Message, state: FSMContext):
    await state.update_data(payment=m.text.strip())
    await _try_send(lambda: m.answer("Срок исполнения/действия:"))
    await state.set_state(ContractFSM.params_term)

@router.message(ContractFSM.params_term)
async def params_term(m: Message, state: FSMContext):
    await state.update_data(term=m.text.strip())
    await _try_send(lambda: m.answer("Штрафные санкции (или '-' ):"))
    await state.set_state(ContractFSM.params_penalties)

@router.message(ContractFSM.params_penalties)
async def params_penalties(m: Message, state: FSMContext):
    penalties = None if m.text.strip() == '-' else m.text.strip()
    await state.update_data(penalties=penalties)
    await _try_send(lambda: m.answer("Выберите формат файла:", reply_markup=choose_output_kb()))
    await state.set_state(ContractFSM.output_format)

@router.callback_query(ContractFSM.output_format, F.data.startswith("out_"))
async def output_choice(c: CallbackQuery, state: FSMContext):
    mapping = {"out_docx": "docx", "out_pdf": "pdf", "out_both": "both"}
    await state.update_data(output=mapping[c.data])
    await _try_send(lambda: c.message.answer(
        "Проверяю реквизиты и готовлю предпросмотр... Подтвердите формирование:",
        reply_markup=confirm_kb()
    ))
    await state.set_state(ContractFSM.confirm)
    await c.answer()

@router.callback_query(ContractFSM.confirm, F.data == "confirm_yes")
async def do_generate(c: CallbackQuery, state: FSMContext):
    data = await state.get_data()

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
        verification_report=None
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
        "verification_status": "OK"
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

    await _try_send(lambda: c.message.answer("Готово. Вот файлы:"))
    for f in files:
        await _try_send(lambda f=f: c.message.answer_document(f))

    await state.clear()
    await c.answer()

@router.callback_query(ContractFSM.confirm, F.data == "confirm_no")
async def cancel(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await _try_send(lambda: c.message.answer("Ок, отменил. /start заново"))
    await c.answer()