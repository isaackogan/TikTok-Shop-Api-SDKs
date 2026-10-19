from enum import StrEnum


class GetProductResponseDataAuditNotSubmittedReasonsItem(StrEnum):
    PAYMENT_ACCOUNT_NOT_LINKED = "PAYMENT_ACCOUNT_NOT_LINKED"
    SHOP_INACTIVE = "SHOP_INACTIVE"
    W8_NOT_CONFIGURED = "W8_NOT_CONFIGURED"

    def __str__(self) -> str:
        return str(self.value)
