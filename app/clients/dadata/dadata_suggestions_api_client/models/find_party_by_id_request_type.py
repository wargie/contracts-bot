from enum import Enum


class FindPartyByIdRequestType(str, Enum):
    INDIVIDUAL = "INDIVIDUAL"
    LEGAL = "LEGAL"

    def __str__(self) -> str:
        return str(self.value)
