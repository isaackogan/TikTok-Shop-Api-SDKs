from enum import StrEnum


class PredictProductPackageDimensionsAndWeightResponseDataPackageDimensionUnit(StrEnum):
    CENTIMETER = "CENTIMETER"
    FOOT = "FOOT"
    INCH = "INCH"
    METER = "METER"
    MILLIMETER = "MILLIMETER"

    def __str__(self) -> str:
        return str(self.value)
