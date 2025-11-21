from enum import Enum


class FounderPhysicalPartyType(str, Enum):
    LEGAL = "LEGAL"
    PHYSICAL = "PHYSICAL"

    def __str__(self) -> str:
        return str(self.value)
