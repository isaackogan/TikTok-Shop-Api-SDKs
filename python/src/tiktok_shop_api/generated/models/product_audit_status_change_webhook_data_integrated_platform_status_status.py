from enum import StrEnum


class ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusStatus(StrEnum):
    APPROVED = "APPROVED"
    AUDITING = "AUDITING"
    FAILED = "FAILED"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
