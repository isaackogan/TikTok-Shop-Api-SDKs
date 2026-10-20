from enum import StrEnum


class GeneratePublisherSharingLinksInBatchRequestMaterialType(StrEnum):
    CAMPAIGN = "CAMPAIGN"
    PRODUCT = "PRODUCT"

    def __str__(self) -> str:
        return str(self.value)
