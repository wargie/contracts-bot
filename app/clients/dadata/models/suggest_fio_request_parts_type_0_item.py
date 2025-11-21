from enum import Enum


class SuggestFioRequestPartsType0Item(str, Enum):
    NAME = "NAME"
    PATRONYMIC = "PATRONYMIC"
    SURNAME = "SURNAME"

    def __str__(self) -> str:
        return str(self.value)
