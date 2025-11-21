from enum import Enum


class IpLocateAddressRequestDivision(str, Enum):
    ADMINISTRATIVE = "ADMINISTRATIVE"
    MUNICIPAL = "MUNICIPAL"

    def __str__(self) -> str:
        return str(self.value)
