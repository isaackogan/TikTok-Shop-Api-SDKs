from enum import StrEnum


class ActivityStatusChangeWebhookDataStatus(StrEnum):
    DEACTIVATED = "DEACTIVATED"
    EXPIRED = "EXPIRED"
    ONGOING = "ONGOING"

    def __str__(self) -> str:
        return str(self.value)
