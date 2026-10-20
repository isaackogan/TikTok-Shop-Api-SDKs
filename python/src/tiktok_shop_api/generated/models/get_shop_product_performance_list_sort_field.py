from enum import StrEnum

class GetShopProductPerformanceListSortField(StrEnum):
    GMV = "gmv"
    ITEMS_SOLD = "items_sold"
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
