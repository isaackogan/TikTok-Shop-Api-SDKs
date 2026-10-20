from enum import StrEnum

class SearchPromotionActivitiesRequestActivityType(StrEnum):
    BUY_MORE_SAVE_MORE = "BUY_MORE_SAVE_MORE"
    BUY_X_GET_Y = "BUY_X_GET_Y"
    DIRECT_DISCOUNT = "DIRECT_DISCOUNT"
    FIXED_PRICE = "FIXED_PRICE"
    FLASHSALE = "FLASHSALE"
    GIFT_WITH_PURCHASE = "GIFT_WITH_PURCHASE"
    SHIPPING_DISCOUNT = "SHIPPING_DISCOUNT"

    def __str__(self) -> str:
        return str(self.value)
