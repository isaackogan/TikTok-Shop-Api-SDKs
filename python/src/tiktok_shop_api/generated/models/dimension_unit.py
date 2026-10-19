from enum import StrEnum


class DimensionUnit(StrEnum):
    CM = "CM"
    INCH = "INCH"

    def __str__(self) -> str:
        return str(self.value)
