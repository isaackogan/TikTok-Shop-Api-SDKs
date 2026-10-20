from enum import StrEnum


class UpdatePackageDeliveryStatusRequestPackageDeliveryType(StrEnum):
    DELIVERY_FAILED = "DELIVERY_FAILED"
    DELIVERY_SUCCESS = "DELIVERY_SUCCESS"
    UPDATE_POD = "UPDATE_POD"

    def __str__(self) -> str:
        return str(self.value)
