from enum import StrEnum


class ShipPackageRequestHandoverMethod(StrEnum):
    DROP_OFF = "DROP_OFF"
    PICKUP = "PICKUP"

    def __str__(self) -> str:
        return str(self.value)
