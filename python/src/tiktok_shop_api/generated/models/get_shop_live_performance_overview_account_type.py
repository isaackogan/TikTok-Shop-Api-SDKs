from enum import StrEnum


class GetShopLivePerformanceOverviewAccountType(StrEnum):
    AFFILIATE_ACCOUNTS = "AFFILIATE_ACCOUNTS"
    ALL = "ALL"
    LINKED_ACCOUNTS = "LINKED_ACCOUNTS"

    def __str__(self) -> str:
        return str(self.value)
