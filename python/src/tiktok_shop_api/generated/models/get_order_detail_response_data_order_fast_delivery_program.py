from enum import StrEnum


class GetOrderDetailResponseDataOrderFastDeliveryProgram(StrEnum):
    VALUE_0 = "3_DAY_DELIVERY"
    VALUE_1 = "3_DAY_POTENTIAL_SHIPPING"
    VALUE_2 = "3_DAY_POTENTIAL_TRANSIT"

    def __str__(self) -> str:
        return str(self.value)
