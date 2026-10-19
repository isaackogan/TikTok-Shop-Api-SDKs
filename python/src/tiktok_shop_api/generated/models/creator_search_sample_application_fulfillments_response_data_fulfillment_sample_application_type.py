from enum import StrEnum


class CreatorSearchSampleApplicationFulfillmentsResponseDataFulfillmentSampleApplicationType(StrEnum):
    FREE_SAMPLE = "FREE_SAMPLE"
    PLATFORM_FREE_SAMPLE = "PLATFORM_FREE_SAMPLE"
    REFUNDABLE_SAMPLE = "REFUNDABLE_SAMPLE"
    SAMPLE_CAMPAIGN = "SAMPLE_CAMPAIGN"
    SAMPLE_COUPON = "SAMPLE_COUPON"
    UNSPECIFIED = "UNSPECIFIED"

    def __str__(self) -> str:
        return str(self.value)
