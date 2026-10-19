from enum import StrEnum


class GetOrderDetailResponseDataOrderFulfillmentType(StrEnum):
    FULFILLMENT_BY_DILAYANI_TOKOPEDIA = "FULFILLMENT_BY_DILAYANI_TOKOPEDIA"
    FULFILLMENT_BY_SELLER = "FULFILLMENT_BY_SELLER"
    FULFILLMENT_BY_TIKTOK = "FULFILLMENT_BY_TIKTOK"

    def __str__(self) -> str:
        return str(self.value)
