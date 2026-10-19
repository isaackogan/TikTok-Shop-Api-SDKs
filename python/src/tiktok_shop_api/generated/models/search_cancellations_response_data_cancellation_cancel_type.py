from enum import StrEnum


class SearchCancellationsResponseDataCancellationCancelType(StrEnum):
    BUYER_CANCEL = "BUYER_CANCEL"
    CANCEL = "CANCEL"

    def __str__(self) -> str:
        return str(self.value)
