from enum import StrEnum


class CreateFirstMileBundleRequestHandoverMethod(StrEnum):
    DROP_OFF = "DROP_OFF"
    PICKUP = "PICKUP"

    def __str__(self) -> str:
        return str(self.value)
