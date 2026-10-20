from enum import StrEnum

class ShipInboundOrderRequestShipmentOptionFreightType(StrEnum):
    FTL = "FTL"
    LTL = "LTL"

    def __str__(self) -> str:
        return str(self.value)
