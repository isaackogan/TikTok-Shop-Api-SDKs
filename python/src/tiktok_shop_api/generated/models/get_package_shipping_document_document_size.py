from enum import StrEnum

class GetPackageShippingDocumentDocumentSize(StrEnum):
    A5 = "A5"
    A6 = "A6"

    def __str__(self) -> str:
        return str(self.value)
