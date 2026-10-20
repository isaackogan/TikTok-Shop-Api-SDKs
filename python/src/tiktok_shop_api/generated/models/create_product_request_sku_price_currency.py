from enum import StrEnum

class CreateProductRequestSkuPriceCurrency(StrEnum):
    BRL = "BRL"
    EUR = "EUR"
    GBP = "GBP"
    IDR = "IDR"
    JPY = "JPY"
    MXN = "MXN"
    MYR = "MYR"
    PHP = "PHP"
    SGD = "SGD"
    THB = "THB"
    USD = "USD"
    VND = "VND"

    def __str__(self) -> str:
        return str(self.value)
