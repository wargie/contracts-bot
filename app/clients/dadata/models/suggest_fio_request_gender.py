from enum import Enum


class SuggestFioRequestGender(str, Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
