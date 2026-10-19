from enum import StrEnum


class GetGlobalCategoriesResponseDataCategoryPermissionStatusesItem(StrEnum):
    AVAILABLE = "AVAILABLE"
    NON_MAIN_CATEGORY = "NON_MAIN_CATEGORY"

    def __str__(self) -> str:
        return str(self.value)
