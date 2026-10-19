from enum import StrEnum


class GetCouponResponseDataCouponTargetBuyerSegment(StrEnum):
    ALL = "ALL"
    EXISTING_ACTIVE_FOLLOWERS = "EXISTING_ACTIVE_FOLLOWERS"
    FREQUENT_CUSTOMERS = "FREQUENT_CUSTOMERS"
    LAPSED_CUSTOMERS = "LAPSED_CUSTOMERS"
    NEW = "NEW"
    NEW_FOLLOWERS = "NEW_FOLLOWERS"
    RECENT_CUSTOMERS = "RECENT_CUSTOMERS"
    REPEAT_CUSTOMERS = "REPEAT_CUSTOMERS"

    def __str__(self) -> str:
        return str(self.value)
