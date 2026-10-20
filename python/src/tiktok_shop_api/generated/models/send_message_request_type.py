from enum import StrEnum

class SendMessageRequestType(StrEnum):
    COUPON_CARD = "COUPON_CARD"
    IMAGE = "IMAGE"
    LOGISTICS_CARD = "LOGISTICS_CARD"
    ORDER_CARD = "ORDER_CARD"
    PRODUCT_CARD = "PRODUCT_CARD"
    RETURN_REFUND_CARD = "RETURN_REFUND_CARD"
    TEXT = "TEXT"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
