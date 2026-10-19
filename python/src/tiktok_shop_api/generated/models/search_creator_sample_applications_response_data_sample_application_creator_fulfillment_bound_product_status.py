from enum import StrEnum


class SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillmentBoundProductStatus(StrEnum):
    LIVE = "LIVE"
    NO_PLAN = "NO_PLAN"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    PERMANENT_DELETED = "PERMANENT_DELETED"
    PLATFORM_DEACTIVATE = "PLATFORM_DEACTIVATE"
    SELLER_DEACTIVATE = "SELLER_DEACTIVATE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
