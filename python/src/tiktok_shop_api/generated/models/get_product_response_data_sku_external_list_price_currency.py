from enum import StrEnum


class GetProductResponseDataSkuExternalListPriceCurrency(StrEnum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
