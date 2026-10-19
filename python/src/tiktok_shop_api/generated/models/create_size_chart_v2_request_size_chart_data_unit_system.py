from enum import StrEnum


class CreateSizeChartV2RequestSizeChartDataUnitSystem(StrEnum):
    IMPERIAL = "IMPERIAL"
    METRIC = "METRIC"

    def __str__(self) -> str:
        return str(self.value)
