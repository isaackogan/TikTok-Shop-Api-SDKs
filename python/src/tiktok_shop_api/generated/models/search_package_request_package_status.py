from enum import StrEnum


class SearchPackageRequestPackageStatus(StrEnum):
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    FULFILLING = "FULFILLING"
    PROCESSING = "PROCESSING"
    TO_FULFILL = "TO_FULFILL"

    def __str__(self) -> str:
        return str(self.value)
