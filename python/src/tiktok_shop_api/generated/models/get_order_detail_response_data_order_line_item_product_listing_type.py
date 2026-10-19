from enum import StrEnum


class GetOrderDetailResponseDataOrderLineItemProductListingType(StrEnum):
    TEMPORARY_LISTING = "TEMPORARY_LISTING"

    def __str__(self) -> str:
        return str(self.value)
