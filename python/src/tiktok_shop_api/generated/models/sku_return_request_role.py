from enum import StrEnum


class SkuReturnRequestRole(StrEnum):
    BUYER = "BUYER"
    OPERATOR = "OPERATOR"
    SELLER = "SELLER"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
