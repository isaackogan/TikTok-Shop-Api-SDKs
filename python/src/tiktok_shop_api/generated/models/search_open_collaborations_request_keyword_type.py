from enum import StrEnum

class SearchOpenCollaborationsRequestKeywordType(StrEnum):
    PRODUCT_ID = "PRODUCT_ID"
    PRODUCT_NAME = "PRODUCT_NAME"

    def __str__(self) -> str:
        return str(self.value)
