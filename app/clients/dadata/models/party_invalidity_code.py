from enum import Enum


class PartyInvalidityCode(str, Enum):
    COURT = "COURT"
    FTS = "FTS"
    OTHER = "OTHER"
    PARTY = "PARTY"

    def __str__(self) -> str:
        return str(self.value)
