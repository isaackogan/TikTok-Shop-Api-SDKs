from enum import StrEnum


class GetCategoryRulesResponseDataSizeChartMeasurementAndOptionMeasurementType(StrEnum):
    BODY_MEASUREMENTS = "BODY_MEASUREMENTS"
    GENERIC_MEASUREMENTS = "GENERIC_MEASUREMENTS"
    PRODUCT_MEASUREMENTS = "PRODUCT_MEASUREMENTS"

    def __str__(self) -> str:
        return str(self.value)
