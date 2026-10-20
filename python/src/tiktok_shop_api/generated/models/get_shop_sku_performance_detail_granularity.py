from enum import StrEnum


class GetShopSkuPerformanceDetailGranularity(StrEnum):
    ALL = "ALL"
    VALUE_1 = "1D"

    def __str__(self) -> str:
        return str(self.value)
