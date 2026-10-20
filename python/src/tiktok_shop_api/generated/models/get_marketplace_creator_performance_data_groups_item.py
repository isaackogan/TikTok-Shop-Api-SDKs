from enum import StrEnum

class GetMarketplaceCreatorPerformanceDataGroupsItem(StrEnum):
    BASIC_CREATOR_INFORMATION = "BASIC_CREATOR_INFORMATION"
    COLLABORATION = "COLLABORATION"
    CONTENT_PERFORMANCE = "CONTENT_PERFORMANCE"
    FOLLOWER_INFORMATION = "FOLLOWER_INFORMATION"
    SALES_AND_GMV = "SALES_AND_GMV"

    def __str__(self) -> str:
        return str(self.value)
