import os
import aiohttp
from typing import Optional, Dict, Any, List
from .base import VerificationProvider

DADATA_URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party"


def _ms(v: Optional[int]) -> Optional[int]:
    """
    Dadata иногда отдаёт секунды, иногда миллисекунды.
    Нормализуем к миллисекундам (int) для единообразия.
    """
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
    """
    Универсальная выемка значений из списков строк или словарей вида {"value": "..."}.
    """
    if not xs:
        return []
    out: List[str] = []
    for it in xs:
        if isinstance(it, str):
            out.append(it)
        elif isinstance(it, dict):
            # чаще всего поле называется "value"
            v = (
                it.get("value")
                or it.get("unrestricted_value")
                or it.get("data")
                or it.get("number")
            )
            if isinstance(v, str):
                out.append(v)
    return out


class DaDataProvider(VerificationProvider):
    """
    Расширенный провайдер: возвращает плоское summary + подробный details и raw.
    """

    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv("DADATA_API_TOKEN")
        if not self.token:
            raise RuntimeError("DADATA_API_TOKEN not set")

    async def verify(self, *, inn: str, kpp: Optional[str] = None) -> Dict[str, Any]:
        payload = {"query": inn}
        if kpp:
            payload["kpp"] = kpp

        headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(DADATA_URL, json=payload, headers=headers, timeout=25) as resp:
                resp.raise_for_status()
                data = await resp.json()

        if not data.get("suggestions"):
            return {"found": False, "reason": "not_found", "query": {"inn": inn, "kpp": kpp}}

        s = data["suggestions"][0]
        d = s.get("data") or {}

        # Основные разделы
        name = d.get("name") or {}
        opf = d.get("opf") or {}
        state = d.get("state") or {}
        addr = d.get("address") or {}
        addr_data = addr.get("data") or {}

        okved_code = d.get("okved")
        okveds_raw = d.get("okveds") or []
        okveds = []
        for it in okveds_raw:
            if isinstance(it, dict):
                code = it.get("code")
                nm = it.get("name")
                okveds.append({"code": code, "name": nm})
            elif isinstance(it, str):
                okveds.append({"code": it, "name": None})

        mgmt = d.get("management") or {}
        managers = d.get("managers") or []   # расширенный список, если есть
        founders = d.get("founders") or []

        phones = _list_values(d.get("phones"))
        emails = _list_values(d.get("emails"))

        details: Dict[str, Any] = {
            "type": d.get("type"),  # LEGAL/INDIVIDUAL
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
            "ids": {
                "inn": d.get("inn"),
                "kpp": d.get("kpp"),
                "ogrn": d.get("ogrn"),
                "okpo": d.get("okpo"),
                "okato": d.get("okato"),
                "oktmo": d.get("oktmo"),
                "okogu": d.get("okogu"),
                "okfs": d.get("okfs"),
            },
            "okved": {
                "primary": {"code": okved_code, "name": None},  # DaData часто не даёт name для primary
                "list": okveds,
                "type": d.get("okved_type"),  # 2014 …
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
                "website": None,  # в party-сервисе DaData сайта обычно нет
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
            "capital": d.get("capital"),       # dict{value,type}, если есть
            "authorities": d.get("authorities"),
            "documents": d.get("documents"),
            "licenses": d.get("licenses"),
            "finance": d.get("finance"),
            "employee_count": d.get("employee_count"),
            "source": d.get("source"),
            "hid": d.get("hid"),
            "ogrn_date": _ms(d.get("ogrn_date")),
        }

        # Плоская сводка для быстрых сценариев
        summary = {
            "name": details["name"]["full_with_opf"] or s.get("value"),
            "name_short": details["name"]["short_with_opf"] or details["name"]["short"],
            "inn": details["ids"]["inn"],
            "kpp": details["ids"]["kpp"],
            "ogrn": details["ids"]["ogrn"],
            "address": details["address"]["unrestricted_value"] or details["address"]["value"],
            "management": (
                f"{details['persons']['management'].get('post')}: {details['persons']['management'].get('name')}"
                if details["persons"]["management"].get("name") else None
            ),
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
        }

        return {
            "found": True,
            "summary": summary,
            "details": details,
            "raw": s,  # для отладки/расширений
        }