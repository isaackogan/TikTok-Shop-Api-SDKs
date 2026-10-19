from enum import StrEnum


class ActivityStatusChangeWebhookDataActivityType(StrEnum):
    BUY_MORE_SAVE_MORE = "BUY_MORE_SAVE_MORE"
    DIRECT_DISCOUNT = "DIRECT_DISCOUNT"
    FIXED_PRICE = "FIXED_PRICE"
    FLASHSALE = "FLASHSALE"
    SHIPPING_DISCOUNT = "SHIPPING_DISCOUNT"

    def __str__(self) -> str:
        return str(self.value)
