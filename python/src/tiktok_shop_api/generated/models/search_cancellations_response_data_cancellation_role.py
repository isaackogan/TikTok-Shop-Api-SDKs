from enum import StrEnum


class SearchCancellationsResponseDataCancellationRole(StrEnum):
    BUYER = "BUYER"
    OPERATOR = "OPERATOR"
    SELLER = "SELLER"
    SYSTEM = "SYSTEM"

    def __str__(self) -> str:
        return str(self.value)
