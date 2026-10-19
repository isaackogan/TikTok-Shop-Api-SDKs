from enum import StrEnum


class OpportunityMatchingStatusChangeWebhookDataOpportunityMatchingStatus(StrEnum):
    MATCHED = "MATCHED"
    NOT_MATCHED = "NOT_MATCHED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
