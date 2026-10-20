from enum import StrEnum


class UploadInvoiceRequestInvoiceFileType(StrEnum):
    XML = "XML"

    def __str__(self) -> str:
        return str(self.value)
