from enum import StrEnum


class GetCouponResponseDataCouponProductScope(StrEnum):
    FULL_SHOP = "FULL_SHOP"
    SPECIFIC_PRODUCTS = "SPECIFIC_PRODUCTS"

    def __str__(self) -> str:
        return str(self.value)
