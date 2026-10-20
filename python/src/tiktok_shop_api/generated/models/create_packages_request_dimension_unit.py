from enum import StrEnum

class CreatePackagesRequestDimensionUnit(StrEnum):
    CM = "CM"
    INCH = "INCH"

    def __str__(self) -> str:
        return str(self.value)
