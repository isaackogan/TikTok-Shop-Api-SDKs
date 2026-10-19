from enum import StrEnum


class RecommendRequiredProductPropertiesResponseDataRecommendedPropertyType(StrEnum):
    KEY_PROPERTY = "KEY_PROPERTY"
    PRODUCT_PROPERTY = "PRODUCT_PROPERTY"
    SALES_PROPERTY = "SALES_PROPERTY"
    UNSPECIFIED = "UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
