from enum import StrEnum


class SearchPackageResponseDataPackageStatus(StrEnum):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FULFILLING = "FULFILLING"
    PROCESSING = "PROCESSING"
    TO_FULFILL = "TO_FULFILL"

    def __str__(self) -> str:
        return str(self.value)
