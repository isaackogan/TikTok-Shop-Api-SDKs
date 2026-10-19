from enum import StrEnum


class GetProductResponseDataSkuListPriceCurrency(StrEnum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
