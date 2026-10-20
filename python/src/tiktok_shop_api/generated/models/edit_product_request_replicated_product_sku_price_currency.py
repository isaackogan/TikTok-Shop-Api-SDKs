from enum import StrEnum

class EditProductRequestReplicatedProductSkuPriceCurrency(StrEnum):
    EUR = "EUR"
    GBP = "GBP"
    IDR = "IDR"
    JPY = "JPY"
    MYR = "MYR"
    PHP = "PHP"
    SGD = "SGD"
    THB = "THB"
    USD = "USD"
    VND = "VND"

    def __str__(self) -> str:
        return str(self.value)
