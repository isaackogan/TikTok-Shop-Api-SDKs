from enum import StrEnum


class ProductAuditStatusChangeWebhookDataIntegratedPlatformStatusPlatform(StrEnum):
    TOKOPEDIA = "TOKOPEDIA"

    def __str__(self) -> str:
        return str(self.value)
