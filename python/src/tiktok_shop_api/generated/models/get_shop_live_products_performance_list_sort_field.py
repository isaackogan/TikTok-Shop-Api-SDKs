from enum import StrEnum


class GetShopLiveProductsPerformanceListSortField(StrEnum):
    CREATED_SKU_ORDERS = "created_sku_orders"
    CUSTOMERS = "customers"
    GMV = "gmv"
    ITEMS_SOLD = "items_sold"
    MAIN_ORDERS = "main_orders"
    PRODUCT_CLICKS = "product_clicks"
    PRODUCT_IMPRESSIONS = "product_impressions"
    SKU_ORDERS = "sku_orders"

    def __str__(self) -> str:
        return str(self.value)
