from enum import StrEnum


class GetPackageDetailResponseDataHandoverMethod(StrEnum):
    DROP_OFF = "DROP_OFF"
    PICKUP = "PICKUP"

    def __str__(self) -> str:
        return str(self.value)
