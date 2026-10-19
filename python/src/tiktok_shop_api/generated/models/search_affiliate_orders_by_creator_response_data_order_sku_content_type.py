from enum import StrEnum


class SearchAffiliateOrdersByCreatorResponseDataOrderSkuContentType(StrEnum):
    LINKSHARE = "LINKSHARE"
    LIVE = "LIVE"
    PRE_LIVE = "PRE_LIVE"
    PROMOTION_PAGE = "PROMOTION_PAGE"
    SHOP = "SHOP"
    VIDEO = "VIDEO"

    def __str__(self) -> str:
        return str(self.value)
