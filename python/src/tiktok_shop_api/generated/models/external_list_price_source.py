from enum import StrEnum

class ExternalListPriceSource(StrEnum):
    SHOPIFY_COMPARE_AT_PRICE = "SHOPIFY_COMPARE_AT_PRICE"

    def __str__(self) -> str:
        return str(self.value)
