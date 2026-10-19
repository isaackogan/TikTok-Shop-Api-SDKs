from enum import StrEnum


class GetProductResponseDataPackageWeightUnit(StrEnum):
    KILOGRAM = "KILOGRAM"
    POUND = "POUND"

    def __str__(self) -> str:
        return str(self.value)
