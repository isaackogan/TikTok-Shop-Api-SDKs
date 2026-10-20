from enum import StrEnum


class GetShopSkuPerformanceListSortField(StrEnum):
    GMV = "gmv"
    SKU_ORDERS = "sku_orders"
    UNITS_SOLD = "units_sold"

    def __str__(self) -> str:
        return str(self.value)
