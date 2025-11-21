# app/bot/checkinn.py
from __future__ import annotations

import os
import re
from datetime import datetime
from typing import Dict, Optional, Tuple

from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

from app.verification.dadata import DaDataProvider

# Для генерации PDF с кириллицей
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from app.services.contract_builder import _ensure_cyrillic_font  # уже есть в проекте

router = Router(name="checkinn")


# ---------- FSM ----------

class CheckInnStates(StatesGroup):
    wait_inn = State()


# ---------- Helpers ----------

def _str(x: Optional[str]) -> str:
    return x if isinstance(x, str) and x.strip() else ""

def _dash(x: Optional[str]) -> str:
    v = _str(x)
    return v if v else "-"

def _ts_to_date(ms: Optional[int]) -> str:
    try:
        if not ms:
            return "-"
        return datetime.utcfromtimestamp(ms / 1000).strftime("%d.%m.%Y")
    except Exception:
        return "-"

def _extract_okved(info: Dict) -> str:
    okved = info.get("okved") or {}
    code = _str(okved.get("code"))
    name = _str(okved.get("name"))
    parts = [p for p in (code, name) if p]
    return " — ".join(parts) if parts else "-"

def _extract_contacts(info: Dict) -> Tuple[str, str]:
    """
    Поддерживаем оба варианта:
    - phone/email на верхнем уровне
    - phones/emails — списки от DaData
    """
    phone = info.get("phone")
    email = info.get("email")

    # из «сырых» данных
    dadata = info.get("dadata") or {}
    phones = dadata.get("phones") or []
    emails = dadata.get("emails") or []

    if not phone and phones and isinstance(phones, list):
        # объект может быть строкой или словарём
        p0 = phones[0]
        if isinstance(p0, dict):
            phone = p0.get("value") or p0.get("data") or ""
        else:
            phone = str(p0)

    if not email and emails and isinstance(emails, list):
        e0 = emails[0]
        if isinstance(e0, dict):
            email = e0.get("value") or e0.get("data") or ""
        else:
            email = str(e0)

    return _dash(_str(phone)), _dash(_str(email))

def _extract_manager(info: Dict) -> str:
    # уже собранная строка в provider: "ДОЛЖНОСТЬ, ФИО"
    mgmt = _str(info.get("management"))
    if not mgmt:
        # попытка вытащить из "сырых"
        raw = (info.get("dadata") or {}).get("management") or {}
        post = _str(raw.get("post"))
        name = _str(raw.get("name"))
        mgmt = ", ".join([p for p in (post, name) if p])
    # просьба была — «после генеральный директор поставить запятую, а не двоеточие»
    mgmt = mgmt.replace(":", ",")
    return _dash(mgmt)

def _status_line(info: Dict) -> str:
    st = _str(info.get("status"))
    return st if st else "-"

def _ogrn_line(info: Dict) -> str:
    return _dash(_str(info.get("ogrn")))

def _short_opf_name(info: Dict) -> str:
    opf = info.get("opf") or {}
    short = _str(opf.get("short"))
    full = _str(opf.get("full"))
    return short or full or "-"

def _full_name(info: Dict) -> str:
    # В отчёте хотели красивое имя
    return _dash(_str(info.get("name_short")) or _str(info.get("name")))

def _reg_date(info: Dict) -> str:
    # Пользователь просил «дата основания/регистрации»
    # В DaData это state.registration_date или ogrn_date — используем оба варианта, что есть.
    date1 = info.get("registration_date")
    if date1:
        return _ts_to_date(date1)
    # запасной вариант
    return _ts_to_date(info.get("ogrn_date"))


# ---------- Report building ----------

def _compose_report(info: Dict) -> str:
    """
    Один красивый текст отчёта.
    """
    title = _full_name(info)

    opf_short = _short_opf_name(info)
    status = _status_line(info)

    inn = _dash(_str(info.get("inn")))
    kpp = _dash(_str(info.get("kpp")))
    ogrn = _ogrn_line(info)
    addr = _dash(_str(info.get("address")))
    manager = _extract_manager(info)
    okved = _extract_okved(info)
    phone, email = _extract_contacts(info)
    reg_date = _reg_date(info)

    # Формат как просили ранее: статус и ОГРН — на отдельных строках,
    # после должности запятая.
    lines = [
        f"🏢 {title}",
        f"ОПФ: {opf_short}",
        f"Статус: {status}",
        f"Дата регистрации: {reg_date}",
        f"ИНН/КПП: {inn} / {kpp}",
        f"ОГРН: {ogrn}",
        f"Адрес: {addr}",
        f"Руководитель: {manager}",
        f"ОКВЭД (осн.): {okved}",
        f"Сайт: {_dash(_str((info.get('site') or info.get('website'))))}",
        f"Тел.: {phone}",
        f"Email: {email}",
    ]
    return "\n".join(lines)


# ---------- PDF ----------

def _report_to_pdf(text: str, out_path: str) -> str:
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    font_name = _ensure_cyrillic_font()  # вернёт, например, "Arial" или "DejaVuSans"

    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4
    left, top, line_h = 40, height - 40, 14

    text_obj = c.beginText()
    text_obj.setTextOrigin(left, top)
    text_obj.setFont(font_name, 10)

    # Перенос по ширине страницы грубым способом
    import textwrap
    wrap_width = 95

    for paragraph in text.split("\n"):
        for wrapped in textwrap.wrap(paragraph, width=wrap_width, replace_whitespace=False, drop_whitespace=False):
            text_obj.textLine(wrapped)
        # пустая строка между логическими блоками
        # (тут каждый абзац — это уже строка, поэтому просто перенос)
    c.drawText(text_obj)
    c.showPage()
    c.save()
    return out_path


# ---------- Keyboards ----------

def _kb_after_report() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔁 Новая проверка", callback_data="checkinn:new")],
        [InlineKeyboardButton(text="🏠 Главное меню", callback_data="checkinn:menu")],
        [InlineKeyboardButton(text="🚪 Выход", callback_data="checkinn:exit")],
    ])


# ---------- Entry points ----------

def checkinn_menu_kb() -> InlineKeyboardMarkup:
    """Кнопка для основного меню (используется в handlers)."""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Проверка по ИНН", callback_data="checkinn:start")]
    ])


@router.callback_query(F.data == "checkinn:start")
async def check_start(c: CallbackQuery, state: FSMContext):
    await state.set_state(CheckInnStates.wait_inn)
    await c.message.edit_text("Введите ИНН компании (10 или 12 цифр). Можно указать «ИНН КПП» через пробел для филиалов.")
    await c.answer()


@router.callback_query(F.data == "checkinn:new")
async def check_new(c: CallbackQuery, state: FSMContext):
    await state.set_state(CheckInnStates.wait_inn)
    await c.message.edit_text("Введите ИНН компании (10 или 12 цифр). Можно указать «ИНН КПП» через пробел для филиалов.")
    await c.answer()


@router.callback_query(F.data == "checkinn:menu")
async def back_to_menu(c: CallbackQuery, state: FSMContext):
    await state.clear()
    # Основное меню показывает /start
    await c.message.edit_text("Возвращаю в главное меню… Нажмите /start")
    await c.answer()


@router.callback_query(F.data == "checkinn:exit")
async def exit_flow(c: CallbackQuery, state: FSMContext):
    await state.clear()
    await c.message.edit_text("Спасибо за использование! Чтобы начать заново — /start")
    await c.answer()


# ---------- INN handler ----------

_INN_RE = re.compile(r"^\s*(\d{10}|\d{12})(?:\s+(\d{9}))?\s*$")

def _parse_inn_kpp(text: str) -> Tuple[Optional[str], Optional[str]]:
    m = _INN_RE.match(text or "")
    if not m:
        return None, None
    inn = m.group(1)
    kpp = m.group(2)
    return inn, kpp


@router.message(CheckInnStates.wait_inn)
async def on_inn_entered(m: Message, state: FSMContext):
    inn, kpp = _parse_inn_kpp(m.text or "")
    if not inn:
        await m.answer("Не распознал ИНН. Введите 10 или 12 цифр (опционально через пробел КПП — 9 цифр).")
        return

    await m.chat.do("typing")
    provider = DaDataProvider()
    info = await provider.verify(inn=inn, kpp=kpp)

    if not info.get("found"):
        await m.answer("Ничего не найдено по указанным данным. Проверьте ИНН/КПП и попробуйте снова.", reply_markup=_kb_after_report())
        await state.set_state(CheckInnStates.wait_inn)
        return

    # 1) Собираем единый текст
    report_text = _compose_report(info)

    # 2) Отправляем единым сообщением
    await m.answer(report_text, reply_markup=_kb_after_report())

    # 3) Готовим PDF и отправляем
    safe_inn = inn
    out_dir = os.path.join("out", "reports")
    os.makedirs(out_dir, exist_ok=True)
    pdf_path = os.path.join(out_dir, f"inn_{safe_inn}.pdf")
    _report_to_pdf(report_text, pdf_path)
    await m.answer_document(FSInputFile(pdf_path))

    # остаёмся в состоянии новой проверки, чтобы можно было вводить следующий ИНН
    await state.set_state(CheckInnStates.wait_inn)