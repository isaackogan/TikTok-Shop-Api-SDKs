from enum import StrEnum


class GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOptionUnit(StrEnum):
    HEIGHT = "HEIGHT"
    LENGTH = "LENGTH"
    NONE = "NONE"
    WEIGHT = "WEIGHT"

    def __str__(self) -> str:
        return str(self.value)
