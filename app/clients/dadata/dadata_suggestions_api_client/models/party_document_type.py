from enum import Enum


class PartyDocumentType(str, Enum):
    FTS_REGISTRATION = "FTS_REGISTRATION"
    FTS_REPORT = "FTS_REPORT"
    PF_REGISTRATION = "PF_REGISTRATION"
    SIF_REGISTRATION = "SIF_REGISTRATION"
    SMB = "SMB"

    def __str__(self) -> str:
        return str(self.value)
