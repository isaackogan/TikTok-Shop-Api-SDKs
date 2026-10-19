from enum import StrEnum


class SearchAffiliateOrdersByCreatorResponseDataOrderStatus(StrEnum):
    DEDUCTED = "DEDUCTED"
    FROZEN = "FROZEN"
    ORDERED = "ORDERED"
    REFUNDED = "REFUNDED"
    SETTLED = "SETTLED"
    UNSPECIFIED = "UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
