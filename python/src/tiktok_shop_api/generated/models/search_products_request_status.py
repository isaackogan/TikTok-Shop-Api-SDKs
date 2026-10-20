from enum import StrEnum

class SearchProductsRequestStatus(StrEnum):
    ACTIVATE = "ACTIVATE"
    ALL = "ALL"
    DELETED = "DELETED"
    DRAFT = "DRAFT"
    FAILED = "FAILED"
    FREEZE = "FREEZE"
    PENDING = "PENDING"
    PLATFORM_DEACTIVATED = "PLATFORM_DEACTIVATED"
    SELLER_DEACTIVATED = "SELLER_DEACTIVATED"

    def __str__(self) -> str:
        return str(self.value)
