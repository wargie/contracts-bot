from enum import Enum


class FindAffiliatedPartyRequestScopeType0Item(str, Enum):
    FOUNDERS = "FOUNDERS"
    MANAGERS = "MANAGERS"

    def __str__(self) -> str:
        return str(self.value)
