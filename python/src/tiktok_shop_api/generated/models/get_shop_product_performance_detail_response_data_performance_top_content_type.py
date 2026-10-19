from enum import StrEnum


class GetShopProductPerformanceDetailResponseDataPerformanceTopContentType(StrEnum):
    LIVE = "LIVE"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
