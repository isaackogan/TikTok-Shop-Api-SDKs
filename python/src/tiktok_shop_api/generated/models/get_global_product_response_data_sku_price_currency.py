from enum import StrEnum


class GetGlobalProductResponseDataSkuPriceCurrency(StrEnum):
    EUR = "EUR"
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
