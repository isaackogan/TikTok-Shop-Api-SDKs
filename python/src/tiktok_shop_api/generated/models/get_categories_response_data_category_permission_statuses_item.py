from enum import StrEnum


class GetCategoriesResponseDataCategoryPermissionStatusesItem(StrEnum):
    AVAILABLE = "AVAILABLE"
    INVITE_ONLY = "INVITE_ONLY"
    NON_MAIN_CATEGORY = "NON_MAIN_CATEGORY"
    PROHIBITED = "PROHIBITED"

    def __str__(self) -> str:
        return str(self.value)
