from enum import StrEnum


class CombinedListingChangeWebhookDataStatus(StrEnum):
    DELETED = "DELETED"
    LIVE = "LIVE"
    SELLER_DEACTIVATED = "SELLER_DEACTIVATED"
    SYSTEM_DEACTIVATED = "SYSTEM_DEACTIVATED"

    def __str__(self) -> str:
        return str(self.value)
