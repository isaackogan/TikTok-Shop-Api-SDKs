from enum import StrEnum

class CartonCartonType(StrEnum):
    MULTI_SKU = "MULTI_SKU"
    SINGLE_SKU = "SINGLE_SKU"

    def __str__(self) -> str:
        return str(self.value)
