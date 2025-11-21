from enum import Enum


class PartyFinanceTaxSystem(str, Enum):
    AUSN = "AUSN"
    ENVD = "ENVD"
    ENVD_ESHN = "ENVD_ESHN"
    ESHN = "ESHN"
    SRP = "SRP"
    USN = "USN"
    USN_ENVD = "USN_ENVD"

    def __str__(self) -> str:
        return str(self.value)
