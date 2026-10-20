from enum import StrEnum


class ReplicateProductRequestInventoryMode(StrEnum):
    EXCLUSIVE = "EXCLUSIVE"
    SHARED = "SHARED"

    def __str__(self) -> str:
        return str(self.value)
