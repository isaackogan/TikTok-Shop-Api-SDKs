from enum import StrEnum


class BxgyDiscountThresholdType(StrEnum):
    MINIMAL_ITEM_QUANTITY = "MINIMAL_ITEM_QUANTITY"
    MINIMAL_ORDER_AMOUNT = "MINIMAL_ORDER_AMOUNT"

    def __str__(self) -> str:
        return str(self.value)
