from enum import StrEnum


class GetShopSkuPerformanceListProductStatusFilter(StrEnum):
    ALL = "ALL"
    INACTIVE = "INACTIVE"
    LIVE = "LIVE"

    def __str__(self) -> str:
        return str(self.value)
