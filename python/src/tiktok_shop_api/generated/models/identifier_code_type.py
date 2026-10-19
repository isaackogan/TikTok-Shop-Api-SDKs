from enum import StrEnum


class IdentifierCodeType(StrEnum):
    EAN = "EAN"
    GTIN = "GTIN"
    ISBN = "ISBN"
    JAN = "JAN"
    UPC = "UPC"

    def __str__(self) -> str:
        return str(self.value)
