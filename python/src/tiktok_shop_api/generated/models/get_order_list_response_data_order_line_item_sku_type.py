from enum import StrEnum


class GetOrderListResponseDataOrderLineItemSkuType(StrEnum):
    MADE_TO_ORDER = "MADE_TO_ORDER"
    NORMAL = "NORMAL"
    PRE_ORDER = "PRE_ORDER"
    SHOP_PARTNER = "SHOP_PARTNER"
    ZERO_LOTTERY = "ZERO_LOTTERY"

    def __str__(self) -> str:
        return str(self.value)
