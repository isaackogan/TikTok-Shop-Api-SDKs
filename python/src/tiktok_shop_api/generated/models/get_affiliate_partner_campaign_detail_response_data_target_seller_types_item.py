from enum import StrEnum


class GetAffiliatePartnerCampaignDetailResponseDataTargetSellerTypesItem(StrEnum):
    CROSS_BORDER = "CROSS_BORDER"
    LOCAL = "LOCAL"

    def __str__(self) -> str:
        return str(self.value)
