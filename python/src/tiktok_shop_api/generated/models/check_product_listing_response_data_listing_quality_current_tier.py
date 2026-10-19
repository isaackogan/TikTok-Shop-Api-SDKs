from enum import StrEnum


class CheckProductListingResponseDataListingQualityCurrentTier(StrEnum):
    EXCELLENT = "EXCELLENT"
    FAIR = "FAIR"
    GOOD = "GOOD"
    POOR = "POOR"

    def __str__(self) -> str:
        return str(self.value)
