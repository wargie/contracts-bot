from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from pathlib import Path

from ..services.registry import Registry

router = Router()
reg = Registry()


def _arg_after_command(text: str) -> str:
    parts = (text or "").split(maxsplit=1)
    return parts[1].strip() if len(parts) > 1 else ""


def _format_row(row: dict) -> str:
    fn = row.get("full_number", "-")
    date = row.get("date_iso", "-")
    pay = row.get("payment_form", "-")
    name = row.get("counterparty_name", "-")
    inn = row.get("counterparty_inn", "-")
    mgr = row.get("manager_surname") or "-"
    our = row.get("our_entity") or "-"
    return (
        f"№ <b>{fn}</b>\n"
        f"Дата: {date} • Оплата: {pay}\n"
        f"Контрагент: {name} (ИНН {inn})\n"
        f"Наше юрлицо: {our}\n"
        f"Менеджер: {mgr}"
    )


def _kb_for_rows(rows: list[dict]):
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    buttons = []
    for row in rows[:10]:
        fn = row.get("full_number")
        buttons.append([InlineKeyboardButton(text=f"📄 Скачать: {fn}", callback_data=f"regdl|{fn}")])
    return InlineKeyboardMarkup(inline_keyboard=buttons) if buttons else None


@router.message(Command("reg_inn"))
async def reg_by_inn(m: Message, state: FSMContext):
    inn = _arg_after_command(m.text)
    if not inn:
        await m.answer("Использование: <code>/reg_inn 7707083893</code>")
        return
    rows = reg.find_by_inn(inn)
    if not rows:
        await m.answer("Записей не найдено.")
        return
    await m.answer("\n\n".join(_format_row(r) for r in rows[:5]), reply_markup=_kb_for_rows(rows))


@router.message(Command("reg_date"))
async def reg_by_date(m: Message, state: FSMContext):
    arg = _arg_after_command(m.text)
    if not arg:
        await m.answer("Использование: <code>/reg_date 29.04.2025</code>")
        return
    try:
        rows = reg.find_by_date(arg)
    except Exception as e:
        await m.answer(f"Неверная дата. Пример: 29.04.2025\nОшибка: {e}")
        return
    if not rows:
        await m.answer("Записей не найдено.")
        return
    await m.answer("\n\n".join(_format_row(r) for r in rows[:10]), reply_markup=_kb_for_rows(rows))


@router.message(Command("reg_name"))
async def reg_by_name(m: Message, state: FSMContext):
    q = _arg_after_command(m.text)
    if not q:
        await m.answer("Использование: <code>/reg_name ДОКТОРПРИНТ</code>")
        return
    rows = reg.find_by_name(q)
    if not rows:
        await m.answer("Записей не найдено.")
        return
    await m.answer("\n\n".join(_format_row(r) for r in rows[:10]), reply_markup=_kb_for_rows(rows))


@router.callback_query(F.data.startswith("regdl|"))
async def reg_download(c: CallbackQuery, state: FSMContext):
    full_number = c.data.split("|", 1)[1]
    row = reg.get_by_full_number(full_number)
    if not row:
        await c.message.answer("Запись не найдена.")
        await c.answer()
        return
    filename = row.get("filename")
    if not filename or not Path(filename).exists():
        await c.message.answer("Файл не найден на диске.")
        await c.answer()
        return
    await c.message.answer_document(FSInputFile(filename), caption=f"№ {full_number}")
    await c.answer()