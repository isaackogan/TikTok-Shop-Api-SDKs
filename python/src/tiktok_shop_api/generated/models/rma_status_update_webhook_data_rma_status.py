from enum import StrEnum


class RMAStatusUpdateWebhookDataRmaStatus(StrEnum):
    AWAITING_BUYER_SHIPPED = "AWAITING_BUYER_SHIPPED"
    INIT = "INIT"
    PACKAGE_REVIEW_COMPLETED = "PACKAGE_REVIEW_COMPLETED"
    PENDING_PACKAGE_REVIEW = "PENDING_PACKAGE_REVIEW"
    RETURN_IN_TRANSIT = "RETURN_IN_TRANSIT"

    def __str__(self) -> str:
        return str(self.value)
