from enum import StrEnum


class SearchPromotionActivitiesRequestStatus(StrEnum):
    DEACTIVATED = "DEACTIVATED"
    EXPIRED = "EXPIRED"
    NOT_START = "NOT_START"
    ONGOING = "ONGOING"

    def __str__(self) -> str:
        return str(self.value)
