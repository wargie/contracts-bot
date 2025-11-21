from enum import Enum


class BankStateStatus(str, Enum):
    ACTIVE = "ACTIVE"
    LIQUIDATED = "LIQUIDATED"
    LIQUIDATING = "LIQUIDATING"

    def __str__(self) -> str:
        return str(self.value)
