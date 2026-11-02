from enum import StrEnum

class GetOffSitePerformanceDetailsContentType(StrEnum):
    LIVE = "LIVE"
    PRODUCT = "PRODUCT"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
