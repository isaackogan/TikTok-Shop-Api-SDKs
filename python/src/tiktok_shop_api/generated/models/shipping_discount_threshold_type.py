from enum import StrEnum

class ShippingDiscountThresholdType(StrEnum):
    MINIMAL_ITEM_QUANTITY = "MINIMAL_ITEM_QUANTITY"
    MINIMAL_ORDER_AMOUNT = "MINIMAL_ORDER_AMOUNT"
    NO_THRESHOLD = "NO_THRESHOLD"

    def __str__(self) -> str:
        return str(self.value)
