import asyncio
from datetime import datetime
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from ..verification.dadata import DaDataProvider
from .keyboards import reply_main_menu_kb

router = Router()

# ---------- локальная FSM для ввода ИНН ----------
class CheckInnFSM(StatesGroup):
    wait_inn = State()

# ---------- утилиты ----------
async def _try_send(coro_factory, retries: int = 3, backoff: float = 1.0):
    last_exc = None
    for i in range(retries):
        try:
            return await coro_factory()
        except Exception as e:
            last_exc = e
            await asyncio.sleep(backoff * (i + 1))
    raise last_exc

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

    return (
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

# ---------- вход в сценарий из главного меню ----------
@router.message(F.text.casefold() == "запрос по инн")
async def on_check_menu(m: Message, state: FSMContext):
    await state.set_state(CheckInnFSM.wait_inn)
    await _try_send(lambda: m.answer("Введите ИНН компании"))

# ---------- обработка свободного ввода ИНН ----------
@router.message(CheckInnFSM.wait_inn, F.text.regexp(r"^\D*\d[\d\D]*$"))
async def on_inn_entered(m: Message, state: FSMContext):
    raw = (m.text or "").strip()
    inn = "".join(ch for ch in raw if ch.isdigit())
    if len(inn) not in (10, 12):
        await _try_send(lambda: m.answer("ИНН должен содержать 10 или 12 цифр. Попробуйте снова."))
        return
    provider = DaDataProvider()
    info = await provider.verify(inn=inn, kpp=None)
    if not info.get("found"):
        await _try_send(lambda: m.answer("Компания не найдена по указанному ИНН.", reply_markup=_after_check_kb()))
        await state.clear()
        return
    await _try_send(lambda: m.answer(_format_report(info), reply_markup=_after_check_kb()))
    await state.clear()

# ---------- команда /checkinn (поддержка старого варианта) ----------
@router.message(Command("checkinn"))
async def cmd_checkinn(m: Message, state: FSMContext):
    parts = (m.text or "").split()
    args = parts[1:] if len(parts) > 1 else []
    if not args:
        await state.set_state(CheckInnFSM.wait_inn)
        await _try_send(lambda: m.answer("Введите ИНН компании"))
        return

    inn = "".join(ch for ch in args[0] if ch.isdigit())
    kpp = "".join(ch for ch in (args[1] if len(args) > 1 else "")) or None

    if len(inn) not in (10, 12):
        await _try_send(lambda: m.answer("ИНН должен содержать 10 или 12 цифр. Попробуйте снова."))
        return

    provider = DaDataProvider()
    info = await provider.verify(inn=inn, kpp=kpp)

    if not info.get("found"):
        await _try_send(lambda: m.answer("Компания не найдена по указанному ИНН.", reply_markup=_after_check_kb()))
        return

    await _try_send(lambda: m.answer(_format_report(info), reply_markup=_after_check_kb()))

# ---------- пост-действия ----------
@router.callback_query(F.data == "check_home")
async def check_home(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await _try_send(lambda: c.message.answer("Меню:", reply_markup=reply_main_menu_kb()))
    await c.answer()

@router.callback_query(F.data == "check_new")
async def check_new(c: CallbackQuery, state: FSMContext):
    await state.set_state(CheckInnFSM.wait_inn)
    await _try_send(lambda: c.message.answer("Введите ИНН компании"))
    await c.answer()

@router.callback_query(F.data == "check_exit")
async def check_exit(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await _try_send(lambda: c.message.answer("Спасибо за использование! Чтобы начать заново — /start"))
    await c.answer()