from enum import StrEnum


class BoxMeasurementWeightUnit(StrEnum):
    GRAM = "GRAM"
    KILOGRAM = "KILOGRAM"
    MILLIGRAM = "MILLIGRAM"
    OUNCE = "OUNCE"
    POUNDS = "POUNDS"

    def __str__(self) -> str:
        return str(self.value)
