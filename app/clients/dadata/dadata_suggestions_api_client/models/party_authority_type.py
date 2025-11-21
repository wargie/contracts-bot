from enum import Enum


class PartyAuthorityType(str, Enum):
    FEDERAL_TAX_SERVICE = "FEDERAL_TAX_SERVICE"
    PENSION_FUND = "PENSION_FUND"
    SOCIAL_INSURANCE_FUND = "SOCIAL_INSURANCE_FUND"

    def __str__(self) -> str:
        return str(self.value)
