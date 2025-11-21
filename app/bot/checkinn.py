import os
import re
import html
import asyncio
from datetime import datetime

from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    FSInputFile,
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from ..verification.dadata import DaDataProvider
from ..services.contract_builder import text_to_pdf
from .keyboards import reply_main_menu_kb

router = Router()


class CheckInnFSM(StatesGroup):
    wait_inn = State()
    view = State()  # показываем готовый отчёт и ждём действия


# -------- helpers --------
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
        return ""
    try:
        iv = int(v)
        return datetime.utcfromtimestamp(iv / 1000).strftime("%d.%m.%Y")
    except Exception:
        return ""


def _line(label: str, value: str) -> str:
    return f"{label}: {value}" if value else ""


def _join_nonempty(lines: list[str], sep: str = "\n") -> str:
    return sep.join([ln for ln in lines if ln])


def _kb_after() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💾 Сохранить PDF", callback_data="check_pdf")],
            [InlineKeyboardButton(text="🏠 В главное меню", callback_data="check_home")],
            [InlineKeyboardButton(text="🔁 Новая проверка", callback_data="check_new")],
            [InlineKeyboardButton(text="🚪 Выход", callback_data="check_exit")],
        ]
    )


def _compose_blocks(info: dict) -> list[str]:
    """Собираем логические блоки отчёта (в HTML)."""
    s = info.get("summary", info)
    d = info.get("details", {})

    opf = s.get("opf_full") or s.get("opf_short") or ""
    status = (s.get("status") or "").upper()
    reg = _ms_to_str(s.get("registration_date") or s.get("ogrn_date"))
    liq = _ms_to_str(s.get("liquidation_date"))

    okved = s.get("okved") or {}
    okved_line = " — ".join([okved.get("code", ""), okved.get("name", "")]).strip(" —")

    ids = (d.get("ids") or {})
    subj_type = d.get("type")
    kpp = ids.get("kpp") if subj_type == "LEGAL" else None
    ogrn_label = "ОГРНИП" if subj_type == "INDIVIDUAL" else "ОГРН"

    header = _join_nonempty(
        [
            f"🧾 <b>{s.get('name') or '-'}</b>",
            _line("ОПФ", opf),
            _line("Статус", status),
            _join_nonempty(
                [_line("Дата регистрации", reg), _line("Ликвидация", liq)], " • "
            ),
            _join_nonempty(
                [f"ИНН {s.get('inn') or ''}", f"КПП {kpp}" if kpp else ""], " / "
            ),
            _line(ogrn_label, s.get("ogrn") or ""),
            _line("Адрес", s.get("address") or ""),
            _line("Руководитель", (s.get("management") or "").replace(":", ",", 1)),
            _line("ОКВЭД (осн.)", okved_line),
        ]
    )

    # Коды/даты
    st = d.get("state") or {}
    codes = _join_nonempty(
        [
            "🔢 <b>Коды и даты</b>",
            _join_nonempty(
                [
                    f"ОКПО: {ids.get('okpo')}" if ids.get("okpo") else "",
                    f"ОКАТО: {ids.get('okato')}" if ids.get("okato") else "",
                    f"ОКТМО: {ids.get('oktmo')}" if ids.get("oktmo") else "",
                ],
                " • ",
            ),
            _join_nonempty(
                [
                    f"ОКОГУ: {ids.get('okogu')}" if ids.get("okogu") else "",
                    f"ОКФС: {ids.get('okfs')}" if ids.get("okfs") else "",
                ],
                " • ",
            ),
            _line("Дата присвоения ОГРН", _ms_to_str(d.get("ogrn_date"))),
            _line("Актуальность данных", _ms_to_str(st.get("actuality_date"))),
            _join_nonempty(
                [
                    f"Признак филиала: {(d.get('branch') or {}).get('branch_type')}"
                    if (d.get("branch") or {}).get("branch_type")
                    and subj_type == "LEGAL"
                    else "",
                    f"Филиалов: {(d.get('branch') or {}).get('branch_count')}"
                    if (d.get("branch") or {}).get("branch_count")
                    and subj_type == "LEGAL"
                    else "",
                ],
                " • ",
            ),
        ]
    )

    # Доп. ОКВЭДы
    okveds = (d.get("okved") or {}).get("list") or []
    okved_block = ""
    if okveds:
        okved_list = "\n".join(
            [
                f"{it.get('code')} — {it.get('name') or ''}".strip(" —")
                for it in okveds[:40]
            ]
        )
        okved_block = "📚 <b>Доп. ОКВЭДы</b>\n" + okved_list

    # Адрес подробно
    ad = ((d.get("address") or {}).get("data")) or {}
    addr_lines = _join_nonempty(
        [
            "📍 <b>Адрес подробно</b>",
            _join_nonempty(
                [
                    f"Индекс: {ad.get('postal_code')}" if ad.get("postal_code") else "",
                    f"Налоговая: {ad.get('tax_office')}" if ad.get("tax_office") else "",
                ],
                " • ",
            ),
            _line("Регион", ad.get("region_with_type") or ""),
            _join_nonempty(
                [
                    f"Город/р-н: {(ad.get('city_with_type') or '')}",
                    f"{(ad.get('city_district_with_type') or '')}",
                ],
                ", ",
            ),
            _join_nonempty(
                [f"Улица/дом: {(ad.get('street_with_type') or '')}", f"{ad.get('house') or ''}"],
                ", ",
            ),
            _join_nonempty(
                [
                    f"FIAС: {ad.get('fias_id')} (lvl {ad.get('fias_level')})"
                    if ad.get("fias_id")
                    else "",
                    f"КЛАДР: {ad.get('kladr_id')}" if ad.get("kladr_id") else "",
                ],
                " • ",
            ),
            _join_nonempty(
                [
                    f"Координаты: {ad.get('geo_lat')}, {ad.get('geo_lon')}"
                    if ad.get("geo_lat") and ad.get("geo_lon")
                    else "",
                    f"Часовой пояс: {ad.get('timezone')}" if ad.get("timezone") else "",
                ],
                " • ",
            ),
        ]
    )

    # Контакты
    contacts = d.get("contacts") or {}
    phones = ", ".join(contacts.get("phones") or [])
    emails = ", ".join(contacts.get("emails") or [])
    contacts_block = _join_nonempty(
        [
            "☎️ <b>Контакты</b>",
            _line("Телефоны", phones),
            _line("E-mail", emails),
            _line("Сайт", contacts.get("website") or ""),
        ]
    )

    # Прочее
    capital = d.get("capital") or {}
    emp = d.get("employee_count")
    misc = _join_nonempty(
        [
            "🏛️ <b>Дополнительно</b>",
            _line(
                "Уставный капитал",
                f"{capital.get('value')} ({capital.get('type')})"
                if capital.get("value")
                else "",
            ),
            _line("Численность сотрудников", str(emp) if emp is not None else ""),
            _join_nonempty(
                [
                    "Документы" if d.get("documents") else "",
                    "Лицензии" if d.get("licenses") else "",
                    "Органы" if d.get("authorities") else "",
                ]
            ),
        ]
    )

    return [header, codes, addr_lines, contacts_block, okved_block, misc]


def _fit_blocks_to_telegram_limit(blocks: list[str], max_len: int = 3800) -> str:
    """Собираем из блоков одно сообщение, не превышая лимит Telegram (≈4096)."""
    out: list[str] = []
    for b in blocks:
        test = "\n\n".join(out + [b])
        if len(test) <= max_len:
            out.append(b)
        else:
            # пробуем укоротить блок (обрежем до ближайшей границы)
            if len("\n\n".join(out)) < max_len:
                remain = max_len - len("\n\n".join(out)) - 1
                trimmed = (b[:remain]).rsplit("\n", 1)[0]
                if trimmed.strip():
                    out.append(trimmed + "\n…")
            break
    return "\n\n".join(out)


def _html_to_plain(s: str) -> str:
    no_tags = re.sub(r"<[^>]+>", "", s)
    return html.unescape(no_tags)


# --- NEW: нормализация текста для PDF (убираем эмодзи и служебные вариации) ---
_EMOJI_STRIP = {
    "🧾": "", "🔢": "", "📚": "", "📍": "", "☎️": "", "🏛️": "",
    "—": "—",  # оставляем длинное тире как есть
}
def _normalize_for_pdf(s: str) -> str:
    for k, v in _EMOJI_STRIP.items():
        s = s.replace(k, v)
    # удалить вариационные селекторы/ZWJ
    s = re.sub(r"[\u200D\uFE0F]", "", s)
    return s.strip()


# -------- entry points --------
@router.message(F.text.casefold() == "запрос по инн")
async def on_check_menu(m: Message, state: FSMContext):
    await state.set_state(CheckInnFSM.wait_inn)
    await _try_send(lambda: m.answer("Введите ИНН компании"))


@router.message(CheckInnFSM.wait_inn, F.text.regexp(r"^\D*\d[\d\D]*$"))
async def on_inn_entered(m: Message, state: FSMContext):
    inn = "".join(ch for ch in (m.text or "").strip() if ch.isdigit())
    if len(inn) not in (10, 12):
        await _try_send(lambda: m.answer("ИНН должен содержать 10 или 12 цифр. Попробуйте снова."))
        return

    info = await DaDataProvider().verify(inn=inn, kpp=None)
    if not info.get("found"):
        await _try_send(lambda: m.answer("Компания не найдена по указанному ИНН.", reply_markup=_kb_after()))
        await state.clear()
        return

    blocks = _compose_blocks(info)  # порядок важен для приоритета
    report_html = _fit_blocks_to_telegram_limit(blocks)
    report_plain = _html_to_plain(report_html)

    # сохраним в состоянии для генерации PDF
    await state.update_data(report_html=report_html, report_plain=report_plain, inn=inn)
    await state.set_state(CheckInnFSM.view)

    await _try_send(lambda: m.answer(report_html, parse_mode=ParseMode.HTML, reply_markup=_kb_after()))


@router.message(Command("checkinn"))
async def cmd_checkinn(m: Message, state: FSMContext):
    parts = (m.text or "").split()
    args = parts[1:] if len(parts) > 1 else []
    if not args:
        await state.set_state(CheckInnFSM.wait_inn)
        await _try_send(lambda: m.answer("Введите ИНН компании"))
        return

    inn = "".join(ch for ch in args[0] if ch.isdigit())
    if len(inn) not in (10, 12):
        await _try_send(lambda: m.answer("ИНН должен содержать 10 или 12 цифр. Попробуйте снова."))
        return

    info = await DaDataProvider().verify(inn=inn, kpp=None)
    if not info.get("found"):
        await _try_send(lambda: m.answer("Компания не найдена по указанному ИНН.", reply_markup=_kb_after()))
        return

    blocks = _compose_blocks(info)
    report_html = _fit_blocks_to_telegram_limit(blocks)
    report_plain = _html_to_plain(report_html)

    await state.update_data(report_html=report_html, report_plain=report_plain, inn=inn)
    await state.set_state(CheckInnFSM.view)

    await _try_send(lambda: m.answer(report_html, parse_mode=ParseMode.HTML, reply_markup=_kb_after()))


# -------- actions after report --------
@router.callback_query(CheckInnFSM.view, F.data == "check_pdf")
async def check_save_pdf(c: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    report_plain = data.get("report_plain")
    inn = data.get("inn") or "report"

    if not report_plain:
        await c.answer("Не удалось сформировать PDF, повторите проверку.", show_alert=True)
        return

    pdf_text = _normalize_for_pdf(report_plain)  # <-- без эмодзи и управляющих меток

    os.makedirs("out", exist_ok=True)
    out_path = f"out/checkinn_{inn}.pdf"
    text_to_pdf(pdf_text, out_path)
    await _try_send(lambda: c.message.answer_document(FSInputFile(out_path), caption=f"Отчёт по ИНН {inn}"))
    await c.answer()


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