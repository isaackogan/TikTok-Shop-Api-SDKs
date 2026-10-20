from enum import StrEnum

class EditAffiliatePartnerCampaignRequestTargetSellerTypesItem(StrEnum):
    CROSS_BORDER = "CROSS_BORDER"
    LOCAL = "LOCAL"

    def __str__(self) -> str:
        return str(self.value)
