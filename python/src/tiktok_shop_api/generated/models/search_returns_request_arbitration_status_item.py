from enum import StrEnum

class SearchReturnsRequestArbitrationStatusItem(StrEnum):
    CLOSED = "CLOSED"
    IN_PROGRESS = "IN_PROGRESS"
    SUPPORT_BUYER = "SUPPORT_BUYER"
    SUPPORT_SELLER = "SUPPORT_SELLER"

    def __str__(self) -> str:
        return str(self.value)
