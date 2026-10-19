from enum import StrEnum


class CurSessionPhase(StrEnum):
    ASSIGNED = "ASSIGNED"
    AUTO_REPLY = "AUTO_REPLY"
    QUEUED = "QUEUED"

    def __str__(self) -> str:
        return str(self.value)
