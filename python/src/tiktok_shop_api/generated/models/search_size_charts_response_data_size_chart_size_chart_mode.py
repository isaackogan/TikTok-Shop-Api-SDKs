from enum import StrEnum


class SearchSizeChartsResponseDataSizeChartSizeChartMode(StrEnum):
    PRODUCT_SCOPED = "PRODUCT_SCOPED"
    REUSABLE_TEMPLATE = "REUSABLE_TEMPLATE"

    def __str__(self) -> str:
        return str(self.value)
