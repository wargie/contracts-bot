from enum import Enum


class LegalPartyBranchType(str, Enum):
    BRANCH = "BRANCH"
    MAIN = "MAIN"

    def __str__(self) -> str:
        return str(self.value)
