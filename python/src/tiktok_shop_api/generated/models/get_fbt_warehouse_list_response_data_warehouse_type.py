from enum import StrEnum


class GetFBTWarehouseListResponseDataWarehouseType(StrEnum):
    OTHER_WAREHOUSE = "OTHER_WAREHOUSE"
    PLATFORM_WAREHOUSE = "PLATFORM_WAREHOUSE"

    def __str__(self) -> str:
        return str(self.value)
