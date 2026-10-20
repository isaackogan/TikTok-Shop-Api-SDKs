from enum import StrEnum


class SearchReturnsRequestSellerProposedReturnTypeItem(StrEnum):
    PARTIAL_REFUND = "PARTIAL_REFUND"

    def __str__(self) -> str:
        return str(self.value)
