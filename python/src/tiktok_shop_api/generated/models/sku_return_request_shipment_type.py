from enum import StrEnum


class SkuReturnRequestShipmentType(StrEnum):
    BUYER_ARRANGE = "BUYER_ARRANGE"
    PLATFORM = "PLATFORM"

    def __str__(self) -> str:
        return str(self.value)
