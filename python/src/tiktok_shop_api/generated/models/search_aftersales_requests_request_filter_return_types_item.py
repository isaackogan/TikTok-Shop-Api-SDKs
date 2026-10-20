from enum import StrEnum

class SearchAftersalesRequestsRequestFilterReturnTypesItem(StrEnum):
    EXCHANGE = "EXCHANGE"
    REFUND = "REFUND"
    REPLACEMENT = "REPLACEMENT"
    RETURN_AND_REFUND = "RETURN_AND_REFUND"

    def __str__(self) -> str:
        return str(self.value)
