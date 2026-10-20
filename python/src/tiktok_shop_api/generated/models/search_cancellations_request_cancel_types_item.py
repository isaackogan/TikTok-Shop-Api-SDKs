from enum import StrEnum

class SearchCancellationsRequestCancelTypesItem(StrEnum):
    BUYER_CANCEL = "BUYER_CANCEL"
    CANCEL = "CANCEL"

    def __str__(self) -> str:
        return str(self.value)
