from enum import StrEnum


class GetOrderDetailResponseDataOrderStatus(StrEnum):
    AWAITING_COLLECTION = "AWAITING_COLLECTION"
    AWAITING_SHIPMENT = "AWAITING_SHIPMENT"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    DELIVERED = "DELIVERED"
    IN_TRANSIT = "IN_TRANSIT"
    ON_HOLD = "ON_HOLD"
    PARTIALLY_SHIPPING = "PARTIALLY_SHIPPING"
    UNPAID = "UNPAID"

    def __str__(self) -> str:
        return str(self.value)
