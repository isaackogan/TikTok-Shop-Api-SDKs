from enum import StrEnum

class ConfirmPackageShipmentRequestPackageDimensionUnit(StrEnum):
    CENTIMETER = "CENTIMETER"
    FOOT = "FOOT"
    INCH = "INCH"
    METER = "METER"
    MICRON = "MICRON"
    MILLIMETER = "MILLIMETER"

    def __str__(self) -> str:
        return str(self.value)
