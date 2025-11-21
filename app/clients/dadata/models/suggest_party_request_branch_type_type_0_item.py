from enum import Enum


class SuggestPartyRequestBranchTypeType0Item(str, Enum):
    BRANCH = "BRANCH"
    MAIN = "MAIN"

    def __str__(self) -> str:
        return str(self.value)
