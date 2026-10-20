from enum import StrEnum

class GetShopVideoPerformanceListCurrency(StrEnum):
    LOCAL = "LOCAL"
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
