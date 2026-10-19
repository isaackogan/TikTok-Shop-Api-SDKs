from enum import StrEnum


class SubItemInfoDisplayStatus(StrEnum):
    AWAITING_COLLECTION = "AWAITING_COLLECTION"
    AWAITING_SHIPMENT = "AWAITING_SHIPMENT"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    DELIVERED = "DELIVERED"
    IN_TRANSIT = "IN_TRANSIT"
    UNPAID = "UNPAID"

    def __str__(self) -> str:
        return str(self.value)
