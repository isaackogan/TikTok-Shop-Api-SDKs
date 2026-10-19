from enum import StrEnum


class SearchProductsResponseDataProductProductTagsItem(StrEnum):
    AUCTION = "AUCTION"
    LIVE_QUICK = "LIVE_QUICK"

    def __str__(self) -> str:
        return str(self.value)
