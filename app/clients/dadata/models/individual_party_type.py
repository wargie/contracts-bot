from enum import Enum


class IndividualPartyType(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    LEGAL = "LEGAL"

    def __str__(self) -> str:
        return str(self.value)
