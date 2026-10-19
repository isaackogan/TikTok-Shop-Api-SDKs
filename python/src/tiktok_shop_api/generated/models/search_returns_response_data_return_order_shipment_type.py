from enum import StrEnum


class SearchReturnsResponseDataReturnOrderShipmentType(StrEnum):
    BUYER_ARRANGE = "BUYER_ARRANGE"
    PLATFORM = "PLATFORM"

    def __str__(self) -> str:
        return str(self.value)
