from enum import StrEnum


class CreatePromotionActivityRequestProductLevel(StrEnum):
    PRODUCT = "PRODUCT"
    SHOP = "SHOP"
    VARIATION = "VARIATION"

    def __str__(self) -> str:
        return str(self.value)
