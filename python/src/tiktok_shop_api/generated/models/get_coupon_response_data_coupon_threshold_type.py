from enum import StrEnum


class GetCouponResponseDataCouponThresholdType(StrEnum):
    MIN_SPEND = "MIN_SPEND"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
