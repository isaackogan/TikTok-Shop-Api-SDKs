from enum import StrEnum


class SearchProductsResponseDataProductSkuExternalListPriceCurrency(StrEnum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
