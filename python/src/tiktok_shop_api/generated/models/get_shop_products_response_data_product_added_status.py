from enum import StrEnum


class GetShopProductsResponseDataProductAddedStatus(StrEnum):
    ADDABLE = "ADDABLE"
    ADDED = "ADDED"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
