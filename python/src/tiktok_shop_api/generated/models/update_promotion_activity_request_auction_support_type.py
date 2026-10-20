from enum import StrEnum

class UpdatePromotionActivityRequestAuctionSupportType(StrEnum):
    ALL = "ALL"
    EXCLUDE_AUCTION = "EXCLUDE_AUCTION"

    def __str__(self) -> str:
        return str(self.value)
