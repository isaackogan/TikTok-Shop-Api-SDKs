from enum import StrEnum

class EditProductRequestSaveMode(StrEnum):
    AS_DRAFT = "AS_DRAFT"
    LISTING = "LISTING"

    def __str__(self) -> str:
        return str(self.value)
