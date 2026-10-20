from enum import StrEnum


class BxgyDiscountDiscountType(StrEnum):
    AMOUNT_OFF_EACH = "AMOUNT_OFF_EACH"
    FREE = "FREE"
    PERCENTAGE_OFF = "PERCENTAGE_OFF"

    def __str__(self) -> str:
        return str(self.value)
