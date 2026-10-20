from enum import StrEnum

class GetShopVideoPerformanceListSortField(StrEnum):
    AVG_CUSTOMERS = "avg_customers"
    CLICK_THROUGH_RATE = "click_through_rate"
    GMV = "gmv"
    GPM = "gpm"
    ITEMS_SOLD = "items_sold"
    POST_TIME = "post_time"
    SKU_ORDERS = "sku_orders"
    VIEWS = "views"

    def __str__(self) -> str:
        return str(self.value)
