from enum import StrEnum


class DeactivateProductsRequestListingPlatformsItem(StrEnum):
    TIKTOK_SHOP = "TIKTOK_SHOP"
    TOKOPEDIA = "TOKOPEDIA"

    def __str__(self) -> str:
        return str(self.value)
