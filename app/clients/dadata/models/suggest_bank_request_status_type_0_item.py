from enum import Enum


class SuggestBankRequestStatusType0Item(str, Enum):
    ACTIVE = "ACTIVE"
    BANKRUPT = "BANKRUPT"
    LIQUIDATED = "LIQUIDATED"
    LIQUIDATING = "LIQUIDATING"
    REORGANIZING = "REORGANIZING"

    def __str__(self) -> str:
        return str(self.value)
