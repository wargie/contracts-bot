from enum import Enum


class BankOpfType(str, Enum):
    BANK = "BANK"
    BANK_BRANCH = "BANK_BRANCH"
    CBR = "CBR"
    NKO = "NKO"
    NKO_BRANCH = "NKO_BRANCH"
    OTHER = "OTHER"
    RKC = "RKC"
    TREASURY = "TREASURY"

    def __str__(self) -> str:
        return str(self.value)
