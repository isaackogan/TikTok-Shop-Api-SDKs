from enum import StrEnum


class GetCouponResponseDataCouponDiscountType(StrEnum):
    AMOUNT_OFF = "AMOUNT_OFF"
    PERCENT_OFF = "PERCENT_OFF"

    def __str__(self) -> str:
        return str(self.value)
