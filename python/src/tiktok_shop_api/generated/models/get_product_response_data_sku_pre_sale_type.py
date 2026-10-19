from enum import StrEnum


class GetProductResponseDataSkuPreSaleType(StrEnum):
    CUSTOM = "CUSTOM"
    MADE_TO_ORDER = "MADE_TO_ORDER"
    PRE_ORDER = "PRE_ORDER"

    def __str__(self) -> str:
        return str(self.value)
