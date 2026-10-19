from enum import StrEnum


class GetOpportunityDetailResponseDataOpportunityActionType(StrEnum):
    LIST_SAME = "LIST_SAME"
    LIST_SIMILAR = "LIST_SIMILAR"

    def __str__(self) -> str:
        return str(self.value)
