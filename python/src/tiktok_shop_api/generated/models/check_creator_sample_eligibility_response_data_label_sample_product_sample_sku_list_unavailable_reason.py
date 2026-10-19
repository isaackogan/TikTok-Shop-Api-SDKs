from enum import StrEnum


class CheckCreatorSampleEligibilityResponseDataLabelSampleProductSampleSkuListUnavailableReason(StrEnum):
    ALREADY_APPLYED = "ALREADY_APPLYED"
    EXCEED_CB_PRICE_THRESHOLD = "EXCEED_CB_PRICE_THRESHOLD"
    IS_GIFT = "IS_GIFT"
    IS_PREORDER = "IS_PREORDER"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
