from enum import StrEnum

class SizeChartDataUnitSystem(StrEnum):
    IMPERIAL = "IMPERIAL"
    METRIC = "METRIC"

    def __str__(self) -> str:
        return str(self.value)
