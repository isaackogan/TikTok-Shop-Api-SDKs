from enum import StrEnum

class CreateGlobalProductRequestSkuPriceCurrency(StrEnum):
    EUR = "EUR"
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
