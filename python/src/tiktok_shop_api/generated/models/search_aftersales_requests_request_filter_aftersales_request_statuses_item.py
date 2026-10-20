from enum import StrEnum

class SearchAftersalesRequestsRequestFilterAftersalesRequestStatusesItem(StrEnum):
    INIT = "INIT"
    PENDING_REQUEST_REVIEW = "PENDING_REQUEST_REVIEW"
    REQUEST_REVIEW_COMPLETED = "REQUEST_REVIEW_COMPLETED"

    def __str__(self) -> str:
        return str(self.value)
