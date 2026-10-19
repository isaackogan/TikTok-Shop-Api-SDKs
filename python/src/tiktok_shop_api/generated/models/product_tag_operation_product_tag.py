from enum import StrEnum


class ProductTagOperationProductTag(StrEnum):
    AUCTION = "AUCTION"

    def __str__(self) -> str:
        return str(self.value)
