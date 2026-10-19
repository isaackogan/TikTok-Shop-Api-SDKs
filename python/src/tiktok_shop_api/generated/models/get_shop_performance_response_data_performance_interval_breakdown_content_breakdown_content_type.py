from enum import StrEnum


class GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownContentType(StrEnum):
    LIVE = "LIVE"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
