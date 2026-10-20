from enum import StrEnum

class ShelfLifeAttributeInfoHandlingMethodExpiredGoods(StrEnum):
    DISPOSE = "DISPOSE"
    RETURN_TO_SELLER = "RETURN_TO_SELLER"
    STORE_UNITS = "STORE_UNITS"

    def __str__(self) -> str:
        return str(self.value)
