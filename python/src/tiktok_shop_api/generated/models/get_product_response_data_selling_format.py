from enum import StrEnum


class GetProductResponseDataSellingFormat(StrEnum):
    FIXED_PRICE = "FIXED_PRICE"
    FIXED_PRICE_AND_LIVE_AUCTION = "FIXED_PRICE_AND_LIVE_AUCTION"
    LIVE_AUCTION = "LIVE_AUCTION"

    def __str__(self) -> str:
        return str(self.value)
