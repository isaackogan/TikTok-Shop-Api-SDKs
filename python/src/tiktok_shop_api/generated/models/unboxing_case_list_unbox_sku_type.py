from enum import StrEnum


class UnboxingCaseListUnboxSkuType(StrEnum):
    GIFT = "GIFT"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
