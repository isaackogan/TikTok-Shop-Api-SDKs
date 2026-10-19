from enum import StrEnum


class GetShopVideosPerformanceDetailsResponseDataVideoPerformanceViewerProfileType(StrEnum):
    NEW_FOLLOWER = "NEW_FOLLOWER"
    VIEWERS = "VIEWERS"

    def __str__(self) -> str:
        return str(self.value)
