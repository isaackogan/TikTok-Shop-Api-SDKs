from enum import StrEnum


class GetProductResponseDataSkuFeeAdditionalAttribute(StrEnum):
    NOT_APPLICABLE = "NOT_APPLICABLE"
    REUSABLE = "REUSABLE"
    SINGLE_USE = "SINGLE_USE"

    def __str__(self) -> str:
        return str(self.value)
