from enum import StrEnum


class GetEngagementTaskPerformancesResponseDataTaskPerformanceStatus(StrEnum):
    CANCELED = "CANCELED"
    DELETED = "DELETED"
    DRAFT = "DRAFT"
    FAILED = "FAILED"
    SENDING = "SENDING"
    SUCCESS = "SUCCESS"
    UNKNOWN = "UNKNOWN"
    WAITING = "WAITING"

    def __str__(self) -> str:
        return str(self.value)
