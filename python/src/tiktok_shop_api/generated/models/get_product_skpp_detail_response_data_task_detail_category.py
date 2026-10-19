from enum import StrEnum


class GetProductSKPPDetailResponseDataTaskDetailCategory(StrEnum):
    ADS_SPEND = "ADS_SPEND"
    COMMISSION_RATE = "COMMISSION_RATE"
    CRM_HOSTING = "CRM_HOSTING"
    FOLLOWER_BENEFITS = "FOLLOWER_BENEFITS"
    FREE_SHIPING = "FREE_SHIPING"
    FULFILMENT = "FULFILMENT"
    INFORMATION_QUALITY = "INFORMATION_QUALITY"
    PRICING = "PRICING"
    SAMPLING = "SAMPLING"
    SHOPPABLE_VIDEOS = "SHOPPABLE_VIDEOS"
    STOCK = "STOCK"

    def __str__(self) -> str:
        return str(self.value)
