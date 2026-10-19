from enum import StrEnum


class SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataUnitSystem(StrEnum):
    IMPERIAL = "IMPERIAL"
    METRIC = "METRIC"

    def __str__(self) -> str:
        return str(self.value)
