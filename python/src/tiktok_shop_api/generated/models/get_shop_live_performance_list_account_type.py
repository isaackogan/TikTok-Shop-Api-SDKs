from enum import StrEnum


class GetShopLivePerformanceListAccountType(StrEnum):
    AFFILIATE_ACCOUNTS = "AFFILIATE_ACCOUNTS"
    MARKETING_ACCOUNTS = "MARKETING_ACCOUNTS"
    OFFICIAL_ACCOUNTS = "OFFICIAL_ACCOUNTS"

    def __str__(self) -> str:
        return str(self.value)
