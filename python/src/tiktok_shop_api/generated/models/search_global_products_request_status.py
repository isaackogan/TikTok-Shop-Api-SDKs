from enum import StrEnum

class SearchGlobalProductsRequestStatus(StrEnum):
    DELETED = "DELETED"
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    UNPUBLISHED = "UNPUBLISHED"

    def __str__(self) -> str:
        return str(self.value)
