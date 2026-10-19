from enum import StrEnum


class GetOrderPriceDetailsResponseDataLineItemSellerFundedShippingPromotionDiscountType(StrEnum):
    ACTIVITY = "ACTIVITY"
    COUPON = "COUPON"

    def __str__(self) -> str:
        return str(self.value)
