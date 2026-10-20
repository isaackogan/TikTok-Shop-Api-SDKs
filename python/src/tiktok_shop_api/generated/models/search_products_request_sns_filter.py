from enum import StrEnum

class SearchProductsRequestSnsFilter(StrEnum):
    CONFIGURED = "CONFIGURED"
    ELIGIBLE = "ELIGIBLE"

    def __str__(self) -> str:
        return str(self.value)
