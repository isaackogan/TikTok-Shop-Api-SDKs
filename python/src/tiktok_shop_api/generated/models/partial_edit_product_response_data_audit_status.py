from enum import StrEnum


class PartialEditProductResponseDataAuditStatus(StrEnum):
    APPROVED = "APPROVED"
    AUDITING = "AUDITING"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
