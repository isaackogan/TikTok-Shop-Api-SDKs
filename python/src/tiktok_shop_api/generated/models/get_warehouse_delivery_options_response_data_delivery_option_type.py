from enum import StrEnum


class GetWarehouseDeliveryOptionsResponseDataDeliveryOptionType(StrEnum):
    CARGO = "CARGO"
    ECONOMY = "ECONOMY"
    EXPRESS = "EXPRESS"
    INSTANT = "INSTANT"
    NEXTDAY = "NEXTDAY"
    SAMEDAY = "SAMEDAY"
    SEND_BY_SELLER = "SEND_BY_SELLER"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
