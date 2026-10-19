from enum import StrEnum


class GetOrderListResponseDataOrderShippingType(StrEnum):
    SELLER = "SELLER"
    TIKTOK = "TIKTOK"
    TIKTOK_DIGITAL = "TIKTOK_DIGITAL"

    def __str__(self) -> str:
        return str(self.value)
