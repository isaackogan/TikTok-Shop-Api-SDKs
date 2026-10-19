from enum import StrEnum


class GetLiveRoomInteractiveTrendsResponseDataInteractiveTrendPerformanceStatsType(StrEnum):
    TREND_COMMENT_PV = "TREND_COMMENT_PV"
    TREND_SHARE_PV = "TREND_SHARE_PV"
    TREND_WATCH_PV = "TREND_WATCH_PV"

    def __str__(self) -> str:
        return str(self.value)
