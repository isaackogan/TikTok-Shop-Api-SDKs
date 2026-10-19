from enum import StrEnum


class GetOrderDetailResponseDataOrderCancellationInitiator(StrEnum):
    BUYER = "BUYER"
    SELLER = "SELLER"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
