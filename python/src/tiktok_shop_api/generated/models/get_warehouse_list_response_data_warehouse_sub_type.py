from enum import StrEnum


class GetWarehouseListResponseDataWarehouseSubType(StrEnum):
    CB_DIRECT_SHIPPING_WAREHOUSE = "CB_DIRECT_SHIPPING_WAREHOUSE"
    CB_OVERSEA_WAREHOUSE = "CB_OVERSEA_WAREHOUSE"
    DOMESTIC_WAREHOUSE = "DOMESTIC_WAREHOUSE"

    def __str__(self) -> str:
        return str(self.value)
