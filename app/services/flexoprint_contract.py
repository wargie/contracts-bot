import os
from pathlib import Path
from datetime import datetime, date
from typing import Optional, Dict, Any

from docxtpl import DocxTemplate

from ..models.party import Party
from .registry import Registry


PREFIX_FP = "ФП"          # индекс для Флексопринт
OUT_DIR = Path("out")     # каталог вывода DOCX


# --- утилиты ---

def _parse_date(d: Any) -> date:
    if isinstance(d, date):
        return d
    if isinstance(d, str):
        for fmt in ("%d.%m.%Y", "%Y-%m-%d", "%d/%m/%Y"):
            try:
                return datetime.strptime(d, fmt).date()
            except Exception:
                pass
    raise ValueError(f"Не могу распарсить дату: {d!r}")


def _date_ru(d: date) -> str:
    return d.strftime("%d.%m.%Y")


def _safe_filename(name: str) -> str:
    """Windows-safe: заменяем недопустимые символы."""
    bad = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    for ch in bad:
        name = name.replace(ch, '—' if ch in ['/', '\\', ':'] else '_')
    return name


def _payment_label(code: str) -> str:
    mapping = {"prepay": "Предоплата", "delay": "Отсрочка", "5050": "50/50"}
    return mapping.get(code, code)


# --- jinja-фильтры для docxtpl ---

def _tsms_to_date(value: Any, fmt: str = "%d.%m.%Y") -> str:
    """
    Преобразует миллисекунды от эпохи (как в DaData state.registration_date)
    в строку даты по формату fmt. Если value пусто — вернёт "-".
    """
    if value in (None, "", 0, "0"):
        return "-"
    try:
        iv = int(value)
        # Heuristic: если похоже на секунды (10 знаков) — умножим до мс
        if iv < 10_000_000_000:
            iv *= 1000
        return datetime.utcfromtimestamp(iv / 1000).strftime(fmt)
    except Exception:
        return str(value)


def _default(value: Any, fallback: str = "-") -> Any:
    """Возвращает fallback, если value пустое/None."""
    return value if value not in (None, "") else fallback


# --- вычисление «основания, на котором действует» ---

def _basis_for_party(dadata: Optional[Dict[str, Any]], fallback: str = "Устава") -> str:
    """
    Возвращает фразу об основании полномочий:
      - для ЮЛ: «Устава»
      - для ИП: «свидетельства о гос. регистрации»
      - иначе: fallback
    Можно расширить под иные типы.
    """
    if not dadata:
        return fallback
    t = (dadata.get("type") or "").upper()
    if t == "LEGAL":
        return "Устава"
    if t == "INDIVIDUAL":
        return "свидетельства о гос. регистрации"
    return fallback


def _our_management_from_env(our_entity: Party) -> Dict[str, str]:
    """
    Возвращает ФИО/должность/основание для нашего юрлица:
    - можно задать в .env: OUR_MANAGER_NAME, OUR_MANAGER_POST, OUR_ACTS_ON
    - если Party.manager заполнен, используем как «ФИО, должность» и попытаемся
      отделить запятой (не критично — можно держать всё в NAME)
    """
    name_env = os.getenv("OUR_MANAGER_NAME") or ""
    post_env = os.getenv("OUR_MANAGER_POST") or ""
    acts_env = os.getenv("OUR_ACTS_ON") or "Устава"

    name = name_env
    post = post_env

    # если party.manager задан, но .env нет — попробуем распарсить "Должность, ФИО" или "ФИО, должность"
    if (not name or not post) and our_entity.manager:
        s = our_entity.manager.strip()
        # простая эвристика: разбить по запятой
        parts = [p.strip() for p in s.split(",", 1)]
        if len(parts) == 2:
            # опробуем обе трактовки
            if not name:
                # чаще встречается "Директор, Иванов И.И." -> имя справа
                name = parts[1]
            if not post:
                post = parts[0]
        else:
            # если без запятой — положим в NAME
            if not name:
                name = s

    return {
        "NAME": name,
        "POST": post,
        "ACTS_ON": acts_env or "Устава",
    }


# --- основная функция ---

def generate_flexoprint_contract(
    *,
    template_path: str,
    date_value: Any,
    payment_form: str,
    counterparty: Party,
    our_entity: Party,
    manager_surname: str,
    cp_dadata: Optional[Dict[str, Any]] = None,   # «сырые» данные DaData для контрагента
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Рендерит договор «Флексопринт» из DOCX-шаблона (docxtpl),
    присваивает номер вида ДД/ММ/ГГГГ/ФПNN, сохраняет в реестр,
    возвращает путь к файлу и метаданные.

    В контекст шаблона передаются:
      - Общие поля: TITLE, FULL_NUMBER, DATE, PAYMENT_FORM, MANAGER_SURNAME
      - OUR.*  — реквизиты Исполнителя (Флексопринт)
      - OUR_MANAGEMENT.{NAME,POST}, OUR_ACTS_ON — ФИО/должность/основание для Исполнителя
      - CP.*   — реквизиты Контрагента (из DaData/Party)
      - CP_MANAGEMENT.{NAME,POST}, CP_ACTS_ON — из DaData (+автовычисление основания)
      - DADATA / CP_DADATA — «сырое» дерево DaData для прямых плейсхолдеров

    Jinja-фильтры:
      - tsms(fmt="%d.%m.%Y")  — миллисекунды → дата
      - default("-")          — подставляет дефолт, если значение пустое
    """
    dt = _parse_date(date_value)
    registry = Registry()

    # 1) Регистрируем запись и резервируем порядковый номер за день (атомарно)
    rec = registry.save_contract(
        date_value=dt,
        company_prefix=PREFIX_FP,
        payment_form=payment_form,
        counterparty_name=counterparty.name,
        counterparty_inn=counterparty.inn,
        our_entity=our_entity.name,
        manager_surname=manager_surname,
        filename="pending",
        meta={
            "payment_form": payment_form,
            "auto_filled": True if cp_dadata else False,
            **(extra or {}),
        },
    )

    # 2) Заголовок и итоговое имя файла
    title = f"ДОГОВОР ПОДРЯДА № {rec.full_number}"   # в документе — со слешами
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    safe_name = _safe_filename(f"{title}.docx")       # имя файла без недопустимых символов
    out_path = OUT_DIR / safe_name

    # 3) Менеджмент/основание для Контрагента из DaData
    cp_mgmt = (cp_dadata or {}).get("management") or {}
    cp_mgmt_name = cp_mgmt.get("name") or ""
    cp_mgmt_post = cp_mgmt.get("post") or ""
    cp_acts_on = _basis_for_party(cp_dadata, fallback="Устава")

    # 4) Менеджмент/основание для Исполнителя из .env/Party
    our_mgmt = _our_management_from_env(our_entity)

    # 5) Контекст для шаблона (и «сырые» DADATA)
    ctx = {
        "TITLE": title,
        "FULL_NUMBER": rec.full_number,
        "DATE": _date_ru(dt),
        "PAYMENT_FORM": _payment_label(payment_form),
        "MANAGER_SURNAME": manager_surname,

        "OUR": {
            "NAME": our_entity.name,
            "INN": our_entity.inn,
            "KPP": our_entity.kpp or "",
            "OGRN": our_entity.ogrn or "",
            "ADDRESS": our_entity.address or "",
            "BANK_NAME": our_entity.bank_name or "",
            "BANK_BIK": our_entity.bank_bik or "",
            "BANK_ACC": our_entity.bank_account or "",
            "BANK_CORR": our_entity.bank_corr or "",
        },
        "OUR_MANAGEMENT": {
            "NAME": our_mgmt["NAME"],
            "POST": our_mgmt["POST"],
        },
        "OUR_ACTS_ON": our_mgmt["ACTS_ON"],

        "CP": {
            "NAME": counterparty.name,
            "INN": counterparty.inn,
            "KPP": counterparty.kpp or "",
            "OGRN": counterparty.ogrn or "",
            "ADDRESS": counterparty.address or "",
            "BANK_NAME": counterparty.bank_name or "",
            "BANK_BIK": counterparty.bank_bik or "",
            "BANK_ACC": counterparty.bank_account or "",
            "BANK_CORR": counterparty.bank_corr or "",
        },
        "CP_MANAGEMENT": {
            "NAME": cp_mgmt_name,
            "POST": cp_mgmt_post,
        },
        "CP_ACTS_ON": cp_acts_on,

        # «сырые» данные DaData (для прямых плейсхолдеров)
        "DADATA": cp_dadata or {},
        "CP_DADATA": cp_dadata or {},
    }

    # 6) Рендер DOCX
    tpl = DocxTemplate(template_path)
    # подключаем jinja-фильтры
    tpl.jinja_env.filters["tsms"] = _tsms_to_date
    tpl.jinja_env.filters["default"] = _default

    tpl.render(ctx)
    tpl.save(str(out_path))

    # 7) Обновляем имя файла в реестре
    registry.update_filename(rec.full_number, str(out_path))

    return {
        "full_number": rec.full_number,
        "title": title,
        "date": rec.date_iso,
        "payment_form": payment_form,
        "path": str(out_path),
    }