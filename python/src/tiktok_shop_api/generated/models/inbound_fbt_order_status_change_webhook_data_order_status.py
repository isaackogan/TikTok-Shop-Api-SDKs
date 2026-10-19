from enum import StrEnum


class InboundFBTOrderStatusChangeWebhookDataOrderStatus(StrEnum):
    ARRIVE_HUB = "ARRIVE_HUB"
    CANCELLED = "CANCELLED"
    PARTIALLY_RECEIVED = "PARTIALLY_RECEIVED"
    RECEIVED = "RECEIVED"
    RECEIVING = "RECEIVING"
    TO_BE_RECEIVED = "TO_BE_RECEIVED"

    def __str__(self) -> str:
        return str(self.value)
