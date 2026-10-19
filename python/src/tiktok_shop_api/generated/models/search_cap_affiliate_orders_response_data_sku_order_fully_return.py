from enum import StrEnum


class SearchCAPAffiliateOrdersResponseDataSkuOrderFullyReturn(StrEnum):
    NO = "No"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)
