from enum import StrEnum


class CreateProductRequestSaveMode(StrEnum):
    AS_DRAFT = "AS_DRAFT"
    LISTING = "LISTING"

    def __str__(self) -> str:
        return str(self.value)
