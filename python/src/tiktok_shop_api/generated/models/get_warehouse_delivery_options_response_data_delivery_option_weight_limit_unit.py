from enum import StrEnum


class GetWarehouseDeliveryOptionsResponseDataDeliveryOptionWeightLimitUnit(StrEnum):
    GRAM = "GRAM"
    KILOGRAM = "KILOGRAM"
    OUNCE = "OUNCE"
    POUND = "POUND"

    def __str__(self) -> str:
        return str(self.value)
