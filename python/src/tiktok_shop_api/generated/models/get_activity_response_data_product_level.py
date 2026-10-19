from enum import StrEnum


class GetActivityResponseDataProductLevel(StrEnum):
    PRODUCT = "PRODUCT"
    SHOP = "SHOP"
    VARIATION = "VARIATION"

    def __str__(self) -> str:
        return str(self.value)
