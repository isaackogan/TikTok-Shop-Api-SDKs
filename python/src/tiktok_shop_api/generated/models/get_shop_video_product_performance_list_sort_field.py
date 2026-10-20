from enum import StrEnum


class GetShopVideoProductPerformanceListSortField(StrEnum):
    DAILY_AVG_BUYERS = "daily_avg_buyers"
    GMV = "gmv"
    UNITS_SOLD = "units_sold"

    def __str__(self) -> str:
        return str(self.value)
