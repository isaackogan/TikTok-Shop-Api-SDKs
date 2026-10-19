from enum import StrEnum


class GetShopSKUPerformanceDetailResponseDataPerformanceIntervalItemsSoldBreakdownType(StrEnum):
    LIVE = "LIVE"
    PRODUCT_CARD = "PRODUCT_CARD"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
