from enum import StrEnum


class ListPriceCurrency(StrEnum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
