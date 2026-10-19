from enum import StrEnum


class SkuReturnRequestReturnShippingDocumentType(StrEnum):
    QR_CODE = "QR_CODE"
    QR_CODE_NBNL = "QR_CODE_NBNL"
    SHIPPING_LABEL = "SHIPPING_LABEL"

    def __str__(self) -> str:
        return str(self.value)
