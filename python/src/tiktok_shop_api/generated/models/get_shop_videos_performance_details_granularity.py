from enum import StrEnum

class GetShopVideosPerformanceDetailsGranularity(StrEnum):
    ALL = "ALL"
    VALUE_1 = "1D"

    def __str__(self) -> str:
        return str(self.value)
