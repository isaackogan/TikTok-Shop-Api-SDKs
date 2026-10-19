from enum import StrEnum


class SearchProductsResponseDataProductListingQualityTier(StrEnum):
    EXCELLENT = "EXCELLENT"
    FAIR = "FAIR"
    GOOD = "GOOD"
    POOR = "POOR"

    def __str__(self) -> str:
        return str(self.value)
