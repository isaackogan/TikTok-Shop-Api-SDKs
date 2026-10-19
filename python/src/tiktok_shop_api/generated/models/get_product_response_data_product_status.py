from enum import StrEnum


class GetProductResponseDataProductStatus(StrEnum):
    ACTIVATE = "ACTIVATE"
    DELETED = "DELETED"
    DRAFT = "DRAFT"
    FREEZE = "FREEZE"
    INITIAL = "INITIAL"
    PLATFORM_DEACTIVATED = "PLATFORM_DEACTIVATED"
    SELLER_DEACTIVATED = "SELLER_DEACTIVATED"

    def __str__(self) -> str:
        return str(self.value)
