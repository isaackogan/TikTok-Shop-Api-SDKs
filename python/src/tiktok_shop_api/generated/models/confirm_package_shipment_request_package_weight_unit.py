from enum import StrEnum

class ConfirmPackageShipmentRequestPackageWeightUnit(StrEnum):
    GRAM = "GRAM"
    KILOGRAM = "KILOGRAM"
    MILLIGRAM = "MILLIGRAM"
    OUNCE = "OUNCE"
    POUND = "POUND"

    def __str__(self) -> str:
        return str(self.value)
