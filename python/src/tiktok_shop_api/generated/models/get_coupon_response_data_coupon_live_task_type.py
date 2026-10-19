from enum import StrEnum


class GetCouponResponseDataCouponLiveTaskType(StrEnum):
    FOLLOW_HOST = "FOLLOW_HOST"
    NONE = "NONE"
    WATCH_FOR_MIN_TIME = "WATCH_FOR_MIN_TIME"

    def __str__(self) -> str:
        return str(self.value)
