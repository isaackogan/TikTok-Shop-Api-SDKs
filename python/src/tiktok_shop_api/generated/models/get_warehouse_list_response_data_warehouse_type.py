from enum import StrEnum


class GetWarehouseListResponseDataWarehouseType(StrEnum):
    RETURN_WAREHOUSE = "RETURN_WAREHOUSE"
    SALES_WAREHOUSE = "SALES_WAREHOUSE"

    def __str__(self) -> str:
        return str(self.value)
