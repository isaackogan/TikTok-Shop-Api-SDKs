from enum import StrEnum

class GetShopProductPerformanceDetailCurrency(StrEnum):
    LOCAL = "LOCAL"
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
