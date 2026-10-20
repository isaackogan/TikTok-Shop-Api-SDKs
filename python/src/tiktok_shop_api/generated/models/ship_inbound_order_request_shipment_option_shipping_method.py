from enum import StrEnum

class ShipInboundOrderRequestShipmentOptionShippingMethod(StrEnum):
    FREIGHT = "FREIGHT"
    SMALL_PARCEL = "SMALL_PARCEL"

    def __str__(self) -> str:
        return str(self.value)
