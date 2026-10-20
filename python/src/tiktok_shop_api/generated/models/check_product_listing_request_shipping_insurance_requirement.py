from enum import StrEnum


class CheckProductListingRequestShippingInsuranceRequirement(StrEnum):
    NOT_SUPPORTED = "NOT_SUPPORTED"
    OPTIONAL = "OPTIONAL"
    REQUIRED = "REQUIRED"

    def __str__(self) -> str:
        return str(self.value)
