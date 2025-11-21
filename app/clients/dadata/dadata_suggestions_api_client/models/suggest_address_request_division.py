from enum import Enum


class SuggestAddressRequestDivision(str, Enum):
    ADMINISTRATIVE = "ADMINISTRATIVE"
    MUNICIPAL = "MUNICIPAL"

    def __str__(self) -> str:
        return str(self.value)
