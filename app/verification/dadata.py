import os
import aiohttp
from typing import Optional, Dict, Any
from .base import VerificationProvider

DADATA_URL = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party"


class DaDataProvider(VerificationProvider):
    """
    Возвращает одновременно:
      1) Нормализованный «удобный» слой (name, inn, kpp, ogrn, address, management, status, opf_*, okved и пр.)
      2) СЫРОЙ объект DaData в поле `dadata` (ровно как в ответе DaData внутри `suggestions[0].data`).

    Это позволяет в DOCX-шаблоне использовать плейсхолдеры напрямую по путям DaData, например:
      {{ DADATA.name.full_with_opf }}
      {{ DADATA.inn }}
      {{ DADATA.kpp }}
      {{ DADATA.ogrn }}
      {{ DADATA.opf.full }}
      {{ DADATA.address.unrestricted_value }}
      {{ DADATA.state.status }}
      {{ DADATA.state.registration_date }}           # мс от эпохи (можно отформатировать фильтром)
      {{ DADATA.state.liquidation_date }}
      {{ DADATA.okved }}                              # код ОКВЭД (расшифровки у DaData нет в этом методе)

    Примечание: даты в `state.*_date` приходят как миллисекунды от эпохи.
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
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(DADATA_URL, json=payload, headers=headers, timeout=20) as resp:
                resp.raise_for_status()
                raw = await resp.json()

        # Ничего не нашли
        if not raw.get("suggestions"):
            return {"found": False, "reason": "not_found"}

        suggestion = raw["suggestions"][0]
        d: Dict[str, Any] = suggestion.get("data") or {}

        # Распаковка удобных полей
        name = (d.get("name") or {})
        mgmt = d.get("management") or {}
        state = d.get("state") or {}
        opf = d.get("opf") or {}
        addr = (d.get("address") or {}).get("unrestricted_value")

        # У findById/party поле okved — это строковый код основного ОКВЭД.
        okved_code = d.get("okved")

        # Сформируем «плоский» слой (для сообщений в чате и т.п.)
        result: Dict[str, Any] = {
            "found": True,

            # «удобные» поля
            "name": name.get("full_with_opf") or suggestion.get("value"),
            "name_short": name.get("short_with_opf") or suggestion.get("value"),
            "inn": d.get("inn"),
            "kpp": d.get("kpp"),
            "ogrn": d.get("ogrn"),
            "address": addr,
            "management": f"{mgmt.get('post','')}: {mgmt.get('name','')}".strip(": "),
            "status": state.get("status"),  # ACTIVE | LIQUIDATING | LIQUIDATED
            "registration_date": state.get("registration_date"),  # мс от эпохи
            "liquidation_date": state.get("liquidation_date"),    # мс от эпохи

            # ОПФ — и как вложенный объект, и плоско
            "opf": {
                "full": opf.get("full"),
                "short": opf.get("short"),
                "code": opf.get("code"),      # код ОКОПФ, если есть
            },
            "opf_full": opf.get("full"),
            "opf_short": opf.get("short"),
            "okopf_code": opf.get("code"),

            # ОКВЭД (осн.)
            "okved": {
                "code": okved_code,
                "name": None,  # findById не отдаёт расшифровку; можно будет обогатить отдельно
            },

            # СЫРОЙ JSON DaData — чтобы плейсхолдеры совпадали «1 к 1» с их ответом
            "dadata": d,            # ← именно data из suggestions[0]
            "suggestion": suggestion,  # при желании — весь suggestion-элемент
        }

        return result