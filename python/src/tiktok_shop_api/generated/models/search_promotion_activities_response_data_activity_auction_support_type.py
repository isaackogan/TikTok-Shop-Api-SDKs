from enum import StrEnum


class SearchPromotionActivitiesResponseDataActivityAuctionSupportType(StrEnum):
    ALL = "ALL"
    EXCLUDE_AUCTION = "EXCLUDE_AUCTION"

    def __str__(self) -> str:
        return str(self.value)
