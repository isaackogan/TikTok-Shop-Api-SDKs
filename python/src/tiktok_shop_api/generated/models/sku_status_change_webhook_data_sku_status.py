from enum import StrEnum


class SKUStatusChangeWebhookDataSkuStatus(StrEnum):
    ACTIVATED = "ACTIVATED"
    CREATED = "CREATED"
    DEACTIVATED = "DEACTIVATED"
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
