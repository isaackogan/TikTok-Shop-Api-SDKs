from enum import StrEnum


class SellerSearchOpenCollaborationProductsSortField(StrEnum):
    COMMISSION = "commission"
    COMMISSION_RATE = "commission_rate"
    PRODUCT_SALES_PRICE = "product_sales_price"
    UNITS_SOLD = "units_sold"

    def __str__(self) -> str:
        return str(self.value)
