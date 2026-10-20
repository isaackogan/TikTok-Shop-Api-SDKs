from enum import StrEnum


class GetAftersaleEligibilityInitiateAftersaleUser(StrEnum):
    BUYER = "BUYER"
    SELLER = "SELLER"

    def __str__(self) -> str:
        return str(self.value)
