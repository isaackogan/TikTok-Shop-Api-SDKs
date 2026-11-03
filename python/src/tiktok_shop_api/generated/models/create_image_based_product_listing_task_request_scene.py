from enum import StrEnum

class CreateImageBasedProductListingTaskRequestScene(StrEnum):
    PROPERTY_RECOMMENDATION = "PROPERTY_RECOMMENDATION"

    def __str__(self) -> str:
        return str(self.value)
