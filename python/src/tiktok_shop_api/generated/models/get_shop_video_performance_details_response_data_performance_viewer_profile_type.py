from enum import StrEnum


class GetShopVideoPerformanceDetailsResponseDataPerformanceViewerProfileType(StrEnum):
    NEW_FOLLOWER = "NEW_FOLLOWER"
    VIEWERS = "VIEWERS"

    def __str__(self) -> str:
        return str(self.value)
