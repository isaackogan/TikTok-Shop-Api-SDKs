from enum import StrEnum


class GetPackageDetailResponseDataPackageSubStatus(StrEnum):
    CANCELLED = "CANCELLED"
    CREATED = "CREATED"
    DELIVERED = "DELIVERED"
    HBW = "HBW"
    HBWING = "HBWING"
    ISSUE = "ISSUE"
    PART_DELIVERED_AND_EXCEPTION = "PART_DELIVERED_AND_EXCEPTION"
    RTS = "RTS"
    RTSING = "RTSING"
    SHIP_EXCEPTION = "SHIP_EXCEPTION"
    STOCKING = "STOCKING"
    TSP_PENDING = "TSP_PENDING"
    TTS = "TTS"

    def __str__(self) -> str:
        return str(self.value)
