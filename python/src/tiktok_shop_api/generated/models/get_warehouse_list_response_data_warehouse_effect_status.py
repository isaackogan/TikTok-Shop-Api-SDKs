from enum import StrEnum


class GetWarehouseListResponseDataWarehouseEffectStatus(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    RESTRICTED = "RESTRICTED"

    def __str__(self) -> str:
        return str(self.value)
