from enum import StrEnum


class GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownChannel(StrEnum):
    CREATOR = "CREATOR"
    SELLER = "SELLER"

    def __str__(self) -> str:
        return str(self.value)
