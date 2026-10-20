from enum import StrEnum


class EditProductRequestListingPlatformsItem(StrEnum):
    TIKTOK_SHOP = "TIKTOK_SHOP"
    TOKOPEDIA = "TOKOPEDIA"

    def __str__(self) -> str:
        return str(self.value)
