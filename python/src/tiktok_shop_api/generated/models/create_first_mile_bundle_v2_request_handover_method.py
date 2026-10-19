from enum import StrEnum


class CreateFirstMileBundleV2RequestHandoverMethod(StrEnum):
    DROP_OFF = "DROP_OFF"
    PICKUP = "PICKUP"

    def __str__(self) -> str:
        return str(self.value)
