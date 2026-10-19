from enum import StrEnum


class GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownContentType(StrEnum):
    LIVE = "LIVE"
    PRODUCT_CARD = "PRODUCT_CARD"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
