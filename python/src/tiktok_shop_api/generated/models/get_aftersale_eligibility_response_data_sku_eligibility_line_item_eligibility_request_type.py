from enum import StrEnum


class GetAftersaleEligibilityResponseDataSkuEligibilityLineItemEligibilityRequestType(StrEnum):
    CANCEL = "CANCEL"
    REFUND = "REFUND"
    RETURN_AND_REFUND = "RETURN_AND_REFUND"

    def __str__(self) -> str:
        return str(self.value)
