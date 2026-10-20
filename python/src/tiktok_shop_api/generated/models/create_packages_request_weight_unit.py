from enum import StrEnum

class CreatePackagesRequestWeightUnit(StrEnum):
    GRAM = "GRAM"
    POUND = "POUND"

    def __str__(self) -> str:
        return str(self.value)
