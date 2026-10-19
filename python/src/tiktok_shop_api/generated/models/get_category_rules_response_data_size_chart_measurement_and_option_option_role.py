from enum import StrEnum


class GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOptionRole(StrEnum):
    KEY = "KEY"
    RECOMMEND = "RECOMMEND"

    def __str__(self) -> str:
        return str(self.value)
