from enum import StrEnum

class GetShopLivePerformanceListSortField(StrEnum):
    ATTRIBUTED_CUSTOMERS = "attributed_customers"
    LIVE_ATTRIBUTED_GMV = "live_attributed_gmv"
    LIVE_ATTRIBUTED_ITEMS_SOLD = "live_attributed_items_sold"
    LIVE_ATTRIBUTED_SKU_ORDERS = "live_attributed_sku_orders"
    PRODUCTS_ADDED = "products_added"
    PRODUCTS_SOLD = "products_sold"

    def __str__(self) -> str:
        return str(self.value)
