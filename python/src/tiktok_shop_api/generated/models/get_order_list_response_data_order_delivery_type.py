from enum import StrEnum


class GetOrderListResponseDataOrderDeliveryType(StrEnum):
    COLLECTION_POINT = "COLLECTION_POINT"
    HOME_DELIVERY = "HOME_DELIVERY"

    def __str__(self) -> str:
        return str(self.value)
