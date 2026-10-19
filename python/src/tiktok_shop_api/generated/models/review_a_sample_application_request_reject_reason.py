from enum import StrEnum


class ReviewASampleApplicationRequestRejectReason(StrEnum):
    NOT_MATCH = "NOT_MATCH"
    OFFLINE = "OFFLINE"
    OTHER = "OTHER"
    OUT_OF_STOCK = "OUT_OF_STOCK"

    def __str__(self) -> str:
        return str(self.value)
