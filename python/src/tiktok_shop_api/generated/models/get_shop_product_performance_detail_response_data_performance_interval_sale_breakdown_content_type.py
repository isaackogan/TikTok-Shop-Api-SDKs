from enum import StrEnum


class GetShopProductPerformanceDetailResponseDataPerformanceIntervalSaleBreakdownContentType(StrEnum):
    LIVE = "LIVE"
    PRODUCT_CARD = "PRODUCT_CARD"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
