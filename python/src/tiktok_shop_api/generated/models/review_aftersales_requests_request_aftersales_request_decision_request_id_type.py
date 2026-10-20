from enum import StrEnum


class ReviewAftersalesRequestsRequestAftersalesRequestDecisionRequestIdType(StrEnum):
    AFTERSALES = "AFTERSALES"
    RMA = "RMA"

    def __str__(self) -> str:
        return str(self.value)
