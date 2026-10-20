from enum import StrEnum

class UploadReturnShippingInformationReturnIdType(StrEnum):
    RMA = "RMA"
    SKU_RETURN_ORDER = "SKU_RETURN_ORDER"

    def __str__(self) -> str:
        return str(self.value)
