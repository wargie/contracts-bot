from enum import Enum


class FounderPartyType(str, Enum):
    LEGAL = "LEGAL"
    PHYSICAL = "PHYSICAL"

    def __str__(self) -> str:
        return str(self.value)
