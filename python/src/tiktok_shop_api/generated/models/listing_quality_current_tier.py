from enum import StrEnum


class ListingQualityCurrentTier(StrEnum):
    FAIR = "FAIR"
    GOOD = "GOOD"
    POOR = "POOR"

    def __str__(self) -> str:
        return str(self.value)
