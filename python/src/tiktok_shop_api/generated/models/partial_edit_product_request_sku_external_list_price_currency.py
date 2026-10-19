from enum import StrEnum


class PartialEditProductRequestSkuExternalListPriceCurrency(StrEnum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
