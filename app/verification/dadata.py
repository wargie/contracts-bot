import os
from typing import Optional, Dict, Any, List

from .base import VerificationProvider

# Используем сгенерированный openapi-python-client (Client),
# но без автогенерируемых operation-функций — напрямую через httpx.AsyncClient,
# который Client предоставляет (get_async_httpx_client()).
from app.clients.dadata.client import Client as OpenApiClient

# Базовый URL для Suggestions API
DADATA_BASE_URL = "https://suggestions.dadata.ru/suggestions/api"
# Конечная точка поиска по ИНН/ОГРН: /4_1/rs/findById/party
FIND_BY_ID_PARTY_PATH = "/4_1/rs/findById/party"


def _first_str(items: Optional[List[dict]]) -> Optional[str]:
    """ Берём первый элемент из списка объектов вида {'value': '...'} """
    if not items:
        return None
    # В DaData в phones/emails элементы могут быть строками или объектами с полем 'value'
    first = items[0]
    if isinstance(first, dict):
        return first.get("value") or first.get("unrestricted_value") or None
    if isinstance(first, str):
        return first
    return None


class DaDataProvider(VerificationProvider):
    def __init__(self, token: Optional[str] = None, base_url: str = DADATA_BASE_URL):
        """
        token — DADATA_API_TOKEN из .env
        """
        self.token = token or os.getenv("DADATA_API_TOKEN")
        if not self.token:
            raise RuntimeError("DADATA_API_TOKEN not set")

        # В клиент передаём заголовки (apiKey в header)
        self.client = OpenApiClient(
            base_url=base_url,
            headers={
                "Authorization": f"Token {self.token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            # таймаут/SSL — по умолчанию
        )

    async def verify(self, *, inn: str, kpp: Optional[str] = None) -> Dict[str, Any]:
        """
        Ищет юрлицо/ИП по ИНН (и опционально по КПП) в DaData Suggestions.
        Возвращает расширенный словарь (совместим с текущей логикой бота).
        """
        payload: Dict[str, Any] = {"query": inn}
        if kpp:
            payload["kpp"] = kpp

        async with self.client.get_async_httpx_client() as httpx_client:
            resp = await httpx_client.post(FIND_BY_ID_PARTY_PATH, json=payload)
            resp.raise_for_status()
            data = resp.json()

        suggestions = data.get("suggestions") or []
        if not suggestions:
            return {"found": False, "reason": "not_found"}

        s = suggestions[0]
        d = s.get("data") or {}

        # Менеджмент / статус
        mgmt = d.get("management") or {}
        state = d.get("state") or {}
        addr = d.get("address") or {}

        # Контакты (могут отсутствовать)
        phones = d.get("phones")
        emails = d.get("emails")

        # ОПФ и ОКВЭД
        opf = d.get("opf") or {}
        okved_code = d.get("okved")
        okved_name = None
        if isinstance(d.get("okveds"), list) and d["okveds"]:
            # если в списке есть осн. код — берём первый элемент с признаком main
            main = next((x for x in d["okveds"] if x.get("main")), d["okveds"][0])
            okved_code = main.get("code") or okved_code
            okved_name = main.get("name")

        result: Dict[str, Any] = {
            "found": True,
            "name": (d.get("name") or {}).get("full_with_opf") or s.get("value"),
            "name_short": (d.get("name") or {}).get("short_with_opf"),
            "inn": d.get("inn"),
            "kpp": d.get("kpp"),
            "ogrn": d.get("ogrn"),
            "address": addr.get("unrestricted_value") or addr.get("value"),
            "management": ", ".join(x for x in [mgmt.get("post"), mgmt.get("name")] if x),
            "status": state.get("status"),  # ACTIVE / LIQUIDATING / LIQUIDATED
            "registration_date": state.get("registration_date"),
            "liquidation_date": state.get("liquidation_date"),
            "opf": {
                "full": opf.get("full"),
                "short": opf.get("short"),
                "code": opf.get("code"),
            },
            "opf_full": opf.get("full"),
            "opf_short": opf.get("short"),
            "okopf_code": opf.get("code"),
            "okved": {"code": okved_code, "name": okved_name},
            # Контакты (первые попавшиеся)
            "phone": _first_str(phones),
            "email": _first_str(emails),
            # Исходные данные DaData (пригодятся для отчёта/отладки)
            "dadata": d,
            "suggestion": s,
        }

        return result