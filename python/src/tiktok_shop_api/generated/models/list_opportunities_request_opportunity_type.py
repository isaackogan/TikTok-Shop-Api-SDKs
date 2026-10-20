from enum import StrEnum

class ListOpportunitiesRequestOpportunityType(StrEnum):
    CATEGORY = "CATEGORY"
    KEYWORD = "KEYWORD"
    PRODUCT = "PRODUCT"

    def __str__(self) -> str:
        return str(self.value)
