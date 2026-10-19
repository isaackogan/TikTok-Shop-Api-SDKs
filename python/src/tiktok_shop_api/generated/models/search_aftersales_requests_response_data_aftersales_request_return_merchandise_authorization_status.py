from enum import StrEnum


class SearchAftersalesRequestsResponseDataAftersalesRequestReturnMerchandiseAuthorizationStatus(StrEnum):
    AWAITING_BUYER_RETURN = "AWAITING_BUYER_RETURN"
    INIT = "INIT"
    PACKAGE_REVIEW_COMPLETED = "PACKAGE_REVIEW_COMPLETED"
    PENDING_PACKAGE_REVIEW = "PENDING_PACKAGE_REVIEW"
    RETURN_IN_TRANSIT = "RETURN_IN_TRANSIT"

    def __str__(self) -> str:
        return str(self.value)
