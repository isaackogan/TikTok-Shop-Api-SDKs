from enum import StrEnum

class GetShopProductsSortField(StrEnum):
    PRICE = "PRICE"
    PRODUCT_ID = "PRODUCT_ID"
    SALE = "SALE"

    def __str__(self) -> str:
        return str(self.value)
