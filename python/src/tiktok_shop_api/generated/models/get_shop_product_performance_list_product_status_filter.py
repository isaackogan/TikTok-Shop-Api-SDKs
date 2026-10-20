from enum import StrEnum

class GetShopProductPerformanceListProductStatusFilter(StrEnum):
    ALL = "ALL"
    INACTIVE = "INACTIVE"
    LIVE = "LIVE"

    def __str__(self) -> str:
        return str(self.value)
