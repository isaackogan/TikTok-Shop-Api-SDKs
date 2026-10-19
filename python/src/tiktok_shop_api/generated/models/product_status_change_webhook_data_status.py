from enum import StrEnum


class ProductStatusChangeWebhookDataStatus(StrEnum):
    PRODUCT_AUDIT_FAILURE = "PRODUCT_AUDIT_FAILURE"
    PRODUCT_FIRST_PASS_REVIEW = "PRODUCT_FIRST_PASS_REVIEW"
    PRODUCT_STATUS_CHANGED = "PRODUCT_STATUS_CHANGED"

    def __str__(self) -> str:
        return str(self.value)
