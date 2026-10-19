from enum import StrEnum


class AftersalesRequestStatusUpdateWebhookDataReturnRole(StrEnum):
    BUYER = "BUYER"
    SELLER = "SELLER"

    def __str__(self) -> str:
        return str(self.value)
