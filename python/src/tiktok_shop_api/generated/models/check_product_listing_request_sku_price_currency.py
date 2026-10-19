from enum import StrEnum


class CheckProductListingRequestSkuPriceCurrency(StrEnum):
    BRL = "BRL"
    CZK = "CZK"
    EUR = "EUR"
    GBP = "GBP"
    HUF = "HUF"
    IDR = "IDR"
    JPY = "JPY"
    MXN = "MXN"
    MYR = "MYR"
    PHP = "PHP"
    PLN = "PLN"
    SGD = "SGD"
    THB = "THB"
    USD = "USD"
    VND = "VND"

    def __str__(self) -> str:
        return str(self.value)
