from enum import StrEnum


class GetLiveRoomUserPortraitsResponseDataAllAdsGenderIndicatorType(StrEnum):
    USER_PORTRAIT_GENDER_F = "USER_PORTRAIT_GENDER_F"
    USER_PORTRAIT_GENDER_M = "USER_PORTRAIT_GENDER_M"
    USER_PORTRAIT_GENDER_UNKNOWN = "USER_PORTRAIT_GENDER_UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
