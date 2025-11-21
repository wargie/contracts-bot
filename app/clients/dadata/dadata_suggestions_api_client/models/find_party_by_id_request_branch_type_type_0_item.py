from enum import Enum


class FindPartyByIdRequestBranchTypeType0Item(str, Enum):
    BRANCH = "BRANCH"
    MAIN = "MAIN"

    def __str__(self) -> str:
        return str(self.value)
