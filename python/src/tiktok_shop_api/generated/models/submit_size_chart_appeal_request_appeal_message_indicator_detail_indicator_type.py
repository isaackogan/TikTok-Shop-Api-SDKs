from enum import StrEnum

class SubmitSizeChartAppealRequestAppealMessageIndicatorDetailIndicatorType(StrEnum):
    CONTAINS_ALL_SALE_PROPERTY = "CONTAINS_ALL_SALE_PROPERTY"
    REQUIRED_DIMENSION = "REQUIRED_DIMENSION"
    VALUE_RANGE_OUT_OF_RANGE = "VALUE_RANGE_OUT_OF_RANGE"

    def __str__(self) -> str:
        return str(self.value)
