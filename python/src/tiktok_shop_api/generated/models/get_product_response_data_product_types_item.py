from enum import StrEnum


class GetProductResponseDataProductTypesItem(StrEnum):
    COMBINED_PRODUCT = "COMBINED_PRODUCT"
    GPR_TARGET_PRODUCT = "GPR_TARGET_PRODUCT"
    IN_COMBINED_PRODUCT = "IN_COMBINED_PRODUCT"

    def __str__(self) -> str:
        return str(self.value)
