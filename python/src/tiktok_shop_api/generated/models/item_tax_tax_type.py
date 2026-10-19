from enum import StrEnum


class ItemTaxTaxType(StrEnum):
    SALES_TAX = "SALES_TAX"

    def __str__(self) -> str:
        return str(self.value)
