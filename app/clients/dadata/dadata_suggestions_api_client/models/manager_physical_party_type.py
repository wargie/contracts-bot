from enum import Enum


class ManagerPhysicalPartyType(str, Enum):
    EMPLOYEE = "EMPLOYEE"
    FOREIGNER = "FOREIGNER"
    LEGAL = "LEGAL"

    def __str__(self) -> str:
        return str(self.value)
