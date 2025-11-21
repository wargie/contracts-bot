from enum import Enum


class FounderShareType(str, Enum):
    DECIMAL = "DECIMAL"
    FRACTION = "FRACTION"
    PERCENT = "PERCENT"

    def __str__(self) -> str:
        return str(self.value)
