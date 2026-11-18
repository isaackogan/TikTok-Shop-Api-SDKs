from enum import StrEnum

class ListShopMaterialsMaterialStatus(StrEnum):
    LIVE = "LIVE"
    REJECTED = "REJECTED"
    UNDER_REVIEW = "UNDER_REVIEW"

    def __str__(self) -> str:
        return str(self.value)
