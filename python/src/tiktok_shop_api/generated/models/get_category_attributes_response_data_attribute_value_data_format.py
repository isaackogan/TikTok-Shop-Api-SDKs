from enum import StrEnum


class GetCategoryAttributesResponseDataAttributeValueDataFormat(StrEnum):
    POSITIVE_INT_OR_DECIMAL = "POSITIVE_INT_OR_DECIMAL"

    def __str__(self) -> str:
        return str(self.value)
