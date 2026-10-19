from enum import StrEnum


class GetProductResponseDataAuditStatus(StrEnum):
    APPROVED = "APPROVED"
    AUDITING = "AUDITING"
    FAILED = "FAILED"
    NONE = "NONE"
    PRE_APPROVED = "PRE_APPROVED"

    def __str__(self) -> str:
        return str(self.value)
