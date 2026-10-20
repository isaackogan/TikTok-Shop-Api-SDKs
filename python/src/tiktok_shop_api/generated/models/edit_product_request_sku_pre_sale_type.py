from enum import StrEnum

class EditProductRequestSkuPreSaleType(StrEnum):
    CUSTOM = "CUSTOM"
    MADE_TO_ORDER = "MADE_TO_ORDER"
    NONE = "NONE"
    PRE_ORDER = "PRE_ORDER"

    def __str__(self) -> str:
        return str(self.value)
