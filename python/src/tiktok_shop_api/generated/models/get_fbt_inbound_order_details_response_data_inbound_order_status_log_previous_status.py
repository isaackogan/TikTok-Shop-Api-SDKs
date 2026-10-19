from enum import StrEnum


class GetFBTInboundOrderDetailsResponseDataInboundOrderStatusLogPreviousStatus(StrEnum):
    ARRIVED_HUB = "ARRIVED_HUB"
    CANCELLED = "CANCELLED"
    DELIVERED = "DELIVERED"
    INTERNAL_TRANSFER = "INTERNAL_TRANSFER"
    PARTIALLY_RECEIVED = "PARTIALLY_RECEIVED"
    READY_TO_SHIP = "READY_TO_SHIP"
    RECEIVED = "RECEIVED"
    RECEIVING = "RECEIVING"
    TO_BE_RECEIVED = "TO_BE_RECEIVED"
    WORKING = "WORKING"

    def __str__(self) -> str:
        return str(self.value)
