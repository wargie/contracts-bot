from enum import Enum


class PartySmbDocumentCategory(str, Enum):
    MEDIUM = "MEDIUM"
    MICRO = "MICRO"
    SMALL = "SMALL"

    def __str__(self) -> str:
        return str(self.value)
