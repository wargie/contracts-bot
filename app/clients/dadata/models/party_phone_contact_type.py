from enum import Enum


class PartyPhoneContactType(str, Enum):
    MANAGING_PARTY = "MANAGING_PARTY"
    TRUSTED_EMPLOYEE = "TRUSTED_EMPLOYEE"
    TRUSTED_FOREIGNER = "TRUSTED_FOREIGNER"

    def __str__(self) -> str:
        return str(self.value)
