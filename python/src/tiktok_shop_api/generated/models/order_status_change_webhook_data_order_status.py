from enum import StrEnum


class OrderStatusChangeWebhookDataOrderStatus(StrEnum):
    AWAITING_COLLECTION = "AWAITING_COLLECTION"
    AWAITING_SHIPMENT = "AWAITING_SHIPMENT"
    CANCEL = "CANCEL"
    COMPLETED = "COMPLETED"
    DELIVERED = "DELIVERED"
    IN_TRANSIT = "IN_TRANSIT"
    ON_HOLD = "ON_HOLD"
    UNPAID = "UNPAID"

    def __str__(self) -> str:
        return str(self.value)
