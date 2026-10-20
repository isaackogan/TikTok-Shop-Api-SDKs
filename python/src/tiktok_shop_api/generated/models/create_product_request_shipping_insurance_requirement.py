from enum import StrEnum

class CreateProductRequestShippingInsuranceRequirement(StrEnum):
    NOT_SUPPORTED = "NOT_SUPPORTED"
    OPTIONAL = "OPTIONAL"
    REQUIRED = "REQUIRED"

    def __str__(self) -> str:
        return str(self.value)
