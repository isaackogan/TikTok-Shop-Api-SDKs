from enum import StrEnum

class SearchAftersalesRequestsRequestWhitelistedDataFieldsItem(StrEnum):
    LINE_ITEMS = "LINE_ITEMS"
    RETURN_MERCHANDISE_AUTHORIZATIONS = "RETURN_MERCHANDISE_AUTHORIZATIONS"
    SKU_RETURN_REQUESTS = "SKU_RETURN_REQUESTS"

    def __str__(self) -> str:
        return str(self.value)
