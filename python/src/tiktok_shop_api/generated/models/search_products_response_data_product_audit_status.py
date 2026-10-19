from enum import StrEnum


class SearchProductsResponseDataProductAuditStatus(StrEnum):
    APPROVED = "APPROVED"
    AUDITING = "AUDITING"
    FAILED = "FAILED"
    NONE = "NONE"
    PRE_APPROVED = "PRE_APPROVED"

    def __str__(self) -> str:
        return str(self.value)
