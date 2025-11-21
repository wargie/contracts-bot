import os
import aiohttp
from typing import Optional, Dict, Any, List
from .base import VerificationProvider

DADATA_PARTY_URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party"
DADATA_OKVED_URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/okved2"


def _ms(v: Optional[int]) -> Optional[int]:
    if v is None:
        return None
    try:
        iv = int(v)
    except Exception:
        return None
    if iv < 10_000_000_000:
        iv *= 1000
    return iv


def _list_values(xs: Optional[List[Any]]) -> List[str]:
    if not xs:
        return []
    out: List[str] = []
    for it in xs:
        if isinstance(it, str):
            out.append(it)
        elif isinstance(it, dict):
            v = it.get("value") or it.get("unrestricted_value") or it.get("number")
            if isinstance(v, str):
                out.append(v)
    return out


async def _resolve_okved_name(session: aiohttp.ClientSession, token: str, code: Optional[str]) -> Optional[str]:
    """Подтягиваем название ОКВЭД по коду, если его не было в party-ответе."""
    if not code:
        return None
    headers = {"Authorization": f"Token {token}", "Content-Type": "application/json", "Accept": "application/json"}
    payload = {"query": code, "count": 1}
    async with session.post(DADATA_OKVED_URL, json=payload, headers=headers, timeout=15) as r:
        r.raise_for_status()
        j = await r.json()
    sgs = j.get("suggestions") or []
    if not sgs:
        return None
    d = (sgs[0] or {}).get("data") or {}
    return d.get("name") or (sgs[0] or {}).get("value")


class DaDataProvider(VerificationProvider):
    """Возвращает расширенную структуру: summary (плоско), details (полно), raw (исходник)."""

    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv("DADATA_API_TOKEN")
        if not self.token:
            raise RuntimeError("DADATA_API_TOKEN not set")

    async def verify(self, *, inn: str, kpp: Optional[str] = None) -> Dict[str, Any]:
        headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        payload = {"query": inn}
        if kpp:
            payload["kpp"] = kpp

        async with aiohttp.ClientSession() as session:
            # 1) Основной запрос по организации/ИП
            async with session.post(DADATA_PARTY_URL, json=payload, headers=headers, timeout=25) as resp:
                resp.raise_for_status()
                data = await resp.json()

            if not data.get("suggestions"):
                return {"found": False, "reason": "not_found", "query": {"inn": inn, "kpp": kpp}}

            s = data["suggestions"][0]
            d = s.get("data") or {}
            name = d.get("name") or {}
            opf = d.get("opf") or {}
            state = d.get("state") or {}
            addr = d.get("address") or {}
            addr_data = addr.get("data") or {}

            # ОКВЭД(ы)
            primary_okved_code = d.get("okved")
            primary_okved_name = None  # часто отсутствует у party
            okveds_raw = d.get("okveds") or []
            okveds = []
            for it in okveds_raw:
                if isinstance(it, dict):
                    okveds.append({"code": it.get("code"), "name": it.get("name")})
                elif isinstance(it, str):
                    okveds.append({"code": it, "name": None})

            # Контакты
            phones = _list_values(d.get("phones"))
            emails = _list_values(d.get("emails"))

            # Тип субъекта и особенности отображения
            subj_type = d.get("type")  # LEGAL / INDIVIDUAL
            ids = {
                "inn": d.get("inn"),
                "kpp": d.get("kpp") if subj_type == "LEGAL" else None,  # у ИП нет КПП
                "ogrn": d.get("ogrn"),
                "okpo": d.get("okpo"),
                "okato": d.get("okato"),
                "oktmo": d.get("oktmo"),
                "okogu": d.get("okogu"),
                "okfs": d.get("okfs"),
            }

            # Руководство
            mgmt = d.get("management") or {}
            managers = d.get("managers") or []
            founders = d.get("founders") or []

            # 2) Обогащаем расшифровку ОКВЭД при необходимости
            if primary_okved_code and not primary_okved_name:
                try:
                    primary_okved_name = await _resolve_okved_name(session, self.token, primary_okved_code)
                except Exception:
                    primary_okved_name = None

            details: Dict[str, Any] = {
                "type": subj_type,
                "branch": {
                    "branch_type": d.get("branch_type"),
                    "branch_count": d.get("branch_count"),
                },
                "name": {
                    "full_with_opf": name.get("full_with_opf"),
                    "short_with_opf": name.get("short_with_opf"),
                    "full": name.get("full"),
                    "short": name.get("short"),
                    "latin": name.get("latin"),
                },
                "opf": {
                    "type": opf.get("type"),
                    "code": opf.get("code"),
                    "full": opf.get("full"),
                    "short": opf.get("short"),
                },
                "state": {
                    "status": state.get("status"),
                    "code": state.get("code"),
                    "actuality_date": _ms(state.get("actuality_date")),
                    "registration_date": _ms(state.get("registration_date")),
                    "liquidation_date": _ms(state.get("liquidation_date")),
                },
                "ids": ids,
                "okved": {
                    "primary": {"code": primary_okved_code, "name": primary_okved_name},
                    "list": okveds,
                    "type": d.get("okved_type"),
                },
                "address": {
                    "value": addr.get("value"),
                    "unrestricted_value": addr.get("unrestricted_value"),
                    "data": {
                        "postal_code": addr_data.get("postal_code"),
                        "country": addr_data.get("country"),
                        "region_with_type": addr_data.get("region_with_type"),
                        "region_type_full": addr_data.get("region_type_full"),
                        "region": addr_data.get("region"),
                        "city_with_type": addr_data.get("city_with_type"),
                        "city_area": addr_data.get("city_area"),
                        "city_district_with_type": addr_data.get("city_district_with_type"),
                        "street_with_type": addr_data.get("street_with_type"),
                        "house": addr_data.get("house"),
                        "block": addr_data.get("block"),
                        "flat": addr_data.get("flat"),
                        "fias_id": addr_data.get("fias_id"),
                        "fias_level": addr_data.get("fias_level"),
                        "kladr_id": addr_data.get("kladr_id"),
                        "geo_lat": addr_data.get("geo_lat"),
                        "geo_lon": addr_data.get("geo_lon"),
                        "timezone": addr_data.get("timezone"),
                        "tax_office": addr_data.get("tax_office"),
                        "tax_office_legal": addr_data.get("tax_office_legal"),
                    },
                },
                "contacts": {
                    "phones": phones,
                    "emails": emails,
                    "website": None,  # party-API обычно не даёт сайт
                },
                "persons": {
                    "management": {
                        "name": mgmt.get("name"),
                        "post": mgmt.get("post"),
                        "start_date": _ms(mgmt.get("start_date")),
                        "disqualified": mgmt.get("disqualified"),
                    },
                    "managers": managers,
                    "founders": founders,
                },
                "capital": d.get("capital"),
                "authorities": d.get("authorities"),
                "documents": d.get("documents"),
                "licenses": d.get("licenses"),
                "finance": d.get("finance"),
                "employee_count": d.get("employee_count"),
                "hid": d.get("hid"),
                "ogrn_date": _ms(d.get("ogrn_date")),
            }

            # Плоская сводка для отчёта
            mgmt_line = None
            if details["persons"]["management"].get("name"):
                post = details["persons"]["management"].get("post")
                name_str = details["persons"]["management"]["name"]
                mgmt_line = f"{post}, {name_str}" if post else name_str

            summary = {
                "name": details["name"]["full_with_opf"] or s.get("value"),
                "name_short": details["name"]["short_with_opf"] or details["name"]["short"],
                "inn": ids["inn"],
                "kpp": ids["kpp"],
                "ogrn": ids["ogrn"],
                "address": details["address"]["unrestricted_value"] or details["address"]["value"],
                "management": mgmt_line,
                "status": details["state"]["status"],
                "registration_date": details["state"]["registration_date"],
                "liquidation_date": details["state"]["liquidation_date"],
                "opf_full": details["opf"]["full"],
                "opf_short": details["opf"]["short"],
                "okopf_code": details["opf"]["code"],
                "okved": {
                    "code": details["okved"]["primary"]["code"],
                    "name": details["okved"]["primary"]["name"],
                },
                "phones": details["contacts"]["phones"],
                "emails": details["contacts"]["emails"],
                "website": details["contacts"]["website"],
                "ogrn_date": details["ogrn_date"],
                "type": subj_type,
            }

            return {"found": True, "summary": summary, "details": details, "raw": s}