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

# ---------- локальная FSM ----------
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

def _ms_to_str(v) -> str:
    if not v:
        return "-"
    try:
        iv = int(v)
        return datetime.utcfromtimestamp(iv / 1000).strftime("%d.%m.%Y")
    except Exception:
        return "-"

def _after_check_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="В главное меню", callback_data="check_home")],
        [InlineKeyboardButton(text="Новая проверка", callback_data="check_new")],
        [InlineKeyboardButton(text="Выход", callback_data="check_exit")],
    ])

def _sections_from_info(info: dict) -> list[str]:
    """
    Строим несколько коротких блоков (чтобы не упереться в лимит 4096 символов).
    Показываем максимум данных, которые есть у DaData.
    """
    s = info.get("summary", info)  # на случай старого формата
    d = info.get("details", {})

    # Заголовок
    management = s.get("management") or "-"
    if ":" in management:
        management = management.replace(":", ",", 1)
    opf = s.get("opf_full") or s.get("opf_short") or "-"
    status = (s.get("status") or "-").upper()
    reg = _ms_to_str(s.get("registration_date") or s.get("ogrn_date"))
    liq = _ms_to_str(s.get("liquidation_date"))
    okved = s.get("okved") or {}
    okved_line = f"{okved.get('code')} — {okved.get('name') or '-'}" if okved.get("code") else "-"

    header = (
        f"🧾 <b>{s.get('name') or '-'}</b>\n"
        f"ОПФ: {opf}\n"
        f"Статус: {status}\n"
        f"Дата регистрации: {reg}" + (f" • Ликвидация: {liq}" if liq != "-" else "") + "\n"
        f"ИНН/КПП: {s.get('inn') or '-'} / {s.get('kpp') or '-'}\n"
        f"ОГРН: {s.get('ogrn') or '-'}\n"
        f"Адрес: {s.get('address') or '-'}\n"
        f"Руководитель: {management}\n"
        f"ОКВЭД (осн.): {okved_line}\n"
    )

    # Коды и даты
    ids = (d.get("ids") or {})
    st = (d.get("state") or {})
    more_codes = (
        "🔢 <b>Коды, даты</b>\n"
        f"ОКПО: {ids.get('okpo') or '-'} • ОКАТО: {ids.get('okato') or '-'} • ОКТМО: {ids.get('oktmo') or '-'}\n"
        f"ОКОГУ: {ids.get('okogu') or '-'} • ОКФС: {ids.get('okfs') or '-'}\n"
        f"Дата ОГРН: {_ms_to_str(d.get('ogrn_date'))}\n"
        f"Актуальность данных: {_ms_to_str(st.get('actuality_date'))}\n"
        f"Признак филиала: {(d.get('branch') or {}).get('branch_type') or '-'} • Филиалов: {(d.get('branch') or {}).get('branch_count') or '-'}"
    )

    # ОКВЭДы (дополнительные)
    okveds = (d.get("okved") or {}).get("list") or []
    if okveds:
        lines = [f"{it.get('code')} — {it.get('name') or '-'}" for it in okveds[:40]]
        okved_block = "📚 <b>Доп. ОКВЭДы</b>\n" + "\n".join(lines)
    else:
        okved_block = "📚 <b>Доп. ОКВЭДы</b>\n—"

    # Адрес подробно
    ad = ((d.get("address") or {}).get("data")) or {}
    addr_block = (
        "📍 <b>Адрес подробно</b>\n"
        f"Индекс: {ad.get('postal_code') or '-'} • Налоговая: {ad.get('tax_office') or '-'}\n"
        f"Регион: {ad.get('region_with_type') or '-'}\n"
        f"Город/р-н: {(ad.get('city_with_type') or '-')}, {(ad.get('city_district_with_type') or '-')}\n"
        f"Улица/дом: {(ad.get('street_with_type') or '-')}, {ad.get('house') or '-'}\n"
        f"FIAС: {ad.get('fias_id') or '-'} (lvl {ad.get('fias_level') or '-'}) • КЛАДР: {ad.get('kladr_id') or '-'}\n"
        f"Координаты: {ad.get('geo_lat') or '-'}, {ad.get('geo_lon') or '-'} • Часовой пояс: {ad.get('timezone') or '-'}"
    )

    # Контакты
    contacts = d.get("contacts") or {}
    phones = ", ".join(contacts.get("phones") or []) or "-"
    emails = ", ".join(contacts.get("emails") or []) or "-"
    website = contacts.get("website") or "-"
    contacts_block = (
        "☎️ <b>Контакты</b>\n"
        f"Телефоны: {phones}\n"
        f"E-mail: {emails}\n"
        f"Сайт: {website}"
    )

    # Состав, капитал, сотрудники (если есть)
    persons = d.get("persons") or {}
    capital = d.get("capital") or {}
    emp = d.get("employee_count")
    more_block = (
        "🏛️ <b>Дополнительно</b>\n"
        f"Уставный капитал: {capital.get('value') or '-'} ({capital.get('type') or '-'})\n"
        f"Численность сотрудников: {emp or '-'}\n"
        f"Документы/лицензии/власти: "
        f"{'есть' if d.get('documents') else '—'}/"
        f"{'есть' if d.get('licenses') else '—'}/"
        f"{'есть' if d.get('authorities') else '—'}"
    )

    return [header, more_codes, okved_block, addr_block, contacts_block, more_block]

# ---------- вход из главного меню ----------
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

    # Отправляем секциями
    for block in _sections_from_info(info):
        await _try_send(lambda b=block: m.answer(b))

    await _try_send(lambda: m.answer("—", reply_markup=_after_check_kb()))
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

    for block in _sections_from_info(info):
        await _try_send(lambda b=block: m.answer(b))

    await _try_send(lambda: m.answer("—", reply_markup=_after_check_kb()))

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