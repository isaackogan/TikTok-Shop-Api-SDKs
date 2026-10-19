from enum import StrEnum


class GetProductResponseDataProductTagsItem(StrEnum):
    AUCTION = "AUCTION"

    def __str__(self) -> str:
        return str(self.value)
