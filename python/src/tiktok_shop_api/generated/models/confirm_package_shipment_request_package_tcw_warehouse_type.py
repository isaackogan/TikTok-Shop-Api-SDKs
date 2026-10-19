from enum import StrEnum


class ConfirmPackageShipmentRequestPackageTcwWarehouseType(StrEnum):
    STANDARD = "STANDARD"
    TIKTOK_CERTIFIED_WAREHOUSE_FULFILLMENT = "TIKTOK_CERTIFIED_WAREHOUSE_FULFILLMENT"

    def __str__(self) -> str:
        return str(self.value)
