from enum import StrEnum


class SearchProductsResponseDataProductStatus(StrEnum):
    ACTIVATE = "ACTIVATE"
    DELETED = "DELETED"
    DRAFT = "DRAFT"
    FAILED = "FAILED"
    FREEZE = "FREEZE"
    PENDING = "PENDING"
    PLATFORM_DEACTIVATED = "PLATFORM_DEACTIVATED"
    SELLER_DEACTIVATED = "SELLER_DEACTIVATED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
