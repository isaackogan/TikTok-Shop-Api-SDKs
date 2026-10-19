from enum import StrEnum


class GetProductResponseDataStatus(StrEnum):
    ACTIVATE = "ACTIVATE"
    DELETED = "DELETED"
    DRAFT = "DRAFT"
    FAILED = "FAILED"
    FREEZE = "FREEZE"
    PENDING = "PENDING"
    PLATFORM_DEACTIVATED = "PLATFORM_DEACTIVATED"
    SCHEDULED = "SCHEDULED"
    SELLER_DEACTIVATED = "SELLER_DEACTIVATED"

    def __str__(self) -> str:
        return str(self.value)
