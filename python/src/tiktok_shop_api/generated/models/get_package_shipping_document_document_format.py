from enum import StrEnum


class GetPackageShippingDocumentDocumentFormat(StrEnum):
    PDF = "PDF"
    ZPL = "ZPL"

    def __str__(self) -> str:
        return str(self.value)
