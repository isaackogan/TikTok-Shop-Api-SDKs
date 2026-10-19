from enum import StrEnum


class ProductAuditStatusChangeWebhookDataAuditPreApprovedReasonsItem(StrEnum):
    KYC_PENDING = "KYC_PENDING"
    RESTRICTED_CATEGORY_PENDING = "RESTRICTED_CATEGORY_PENDING"

    def __str__(self) -> str:
        return str(self.value)
