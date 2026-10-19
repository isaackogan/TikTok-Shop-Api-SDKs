from enum import StrEnum


class GetGlobalAttributesResponseDataAttributeType(StrEnum):
    PRODUCT_PROPERTY = "PRODUCT_PROPERTY"
    SALES_PROPERTY = "SALES_PROPERTY"

    def __str__(self) -> str:
        return str(self.value)
