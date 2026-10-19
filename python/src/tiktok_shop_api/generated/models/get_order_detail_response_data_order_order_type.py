from enum import StrEnum


class GetOrderDetailResponseDataOrderOrderType(StrEnum):
    AUCTION = "AUCTION"
    BACK_ORDER = "BACK_ORDER"
    MADE_TO_ORDER = "MADE_TO_ORDER"
    NORMAL = "NORMAL"
    PRE_ORDER = "PRE_ORDER"
    VIRTUAL_ORDER = "VIRTUAL_ORDER"
    ZERO_LOTTERY = "ZERO_LOTTERY"

    def __str__(self) -> str:
        return str(self.value)
