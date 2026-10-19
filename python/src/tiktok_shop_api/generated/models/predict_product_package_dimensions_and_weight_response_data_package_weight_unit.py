from enum import StrEnum


class PredictProductPackageDimensionsAndWeightResponseDataPackageWeightUnit(StrEnum):
    GRAM = "GRAM"
    KILOGRAM = "KILOGRAM"
    OUNCE = "OUNCE"
    POUND = "POUND"

    def __str__(self) -> str:
        return str(self.value)
