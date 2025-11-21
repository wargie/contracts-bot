from enum import Enum


class SuggestAddressRequestLanguage(str, Enum):
    EN = "EN"
    RU = "RU"

    def __str__(self) -> str:
        return str(self.value)
