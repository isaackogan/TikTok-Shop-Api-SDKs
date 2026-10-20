from enum import StrEnum


class SearchReturnMerchandiseAuthorizationsRequestWhitelistedDataFieldsItem(StrEnum):
    LINE_ITEMS = "LINE_ITEMS"
    SKU_RETURN_REQUESTS = "SKU_RETURN_REQUESTS"

    def __str__(self) -> str:
        return str(self.value)
