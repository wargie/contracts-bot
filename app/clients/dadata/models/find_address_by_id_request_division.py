from enum import Enum


class FindAddressByIdRequestDivision(str, Enum):
    ADMINISTRATIVE = "ADMINISTRATIVE"
    MUNICIPAL = "MUNICIPAL"

    def __str__(self) -> str:
        return str(self.value)
