from enum import StrEnum

class SearchProductsRequestAuditStatusItem(StrEnum):
    APPROVED = "APPROVED"
    AUDITING = "AUDITING"
    FAILED = "FAILED"

    def __str__(self) -> str:
        return str(self.value)
