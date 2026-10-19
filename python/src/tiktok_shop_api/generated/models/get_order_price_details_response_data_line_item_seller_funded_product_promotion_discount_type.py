from enum import StrEnum


class GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotionDiscountType(StrEnum):
    ACTIVITY = "ACTIVITY"
    COUPON = "COUPON"

    def __str__(self) -> str:
        return str(self.value)
