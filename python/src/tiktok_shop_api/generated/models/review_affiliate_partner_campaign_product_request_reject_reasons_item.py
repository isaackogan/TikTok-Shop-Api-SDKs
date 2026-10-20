from enum import StrEnum


class ReviewAffiliatePartnerCampaignProductRequestRejectReasonsItem(StrEnum):
    COMMISSION_TOO_LOW = "COMMISSION_TOO_LOW"
    NO_SUITABLE_CREATOR = "NO_SUITABLE_CREATOR"
    PRODUCT_HARD_TO_PROMOTE = "PRODUCT_HARD_TO_PROMOTE"
    PRODUCT_TOO_EXPENSIVE = "PRODUCT_TOO_EXPENSIVE"

    def __str__(self) -> str:
        return str(self.value)
