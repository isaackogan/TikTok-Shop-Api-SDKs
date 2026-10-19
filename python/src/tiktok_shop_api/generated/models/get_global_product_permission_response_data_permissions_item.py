from enum import StrEnum


class GetGlobalProductPermissionResponseDataPermissionsItem(StrEnum):
    MANAGE_GLOBAL_PRODUCT = "MANAGE_GLOBAL_PRODUCT"

    def __str__(self) -> str:
        return str(self.value)
