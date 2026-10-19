from enum import StrEnum


class GetGlobalSellerWarehousesResponseDataGlobalWarehouseOwnership(StrEnum):
    PLATFORM_COOPERATION = "PLATFORM_COOPERATION"
    SELLER = "SELLER"

    def __str__(self) -> str:
        return str(self.value)
