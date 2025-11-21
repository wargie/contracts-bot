from enum import Enum


class SuggestPartyRequestStatusType0Item(str, Enum):
    ACTIVE = "ACTIVE"
    BANKRUPT = "BANKRUPT"
    LIQUIDATED = "LIQUIDATED"
    LIQUIDATING = "LIQUIDATING"
    REORGANIZING = "REORGANIZING"

    def __str__(self) -> str:
        return str(self.value)
