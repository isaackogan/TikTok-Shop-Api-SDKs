from enum import StrEnum

class HazmatInfoHazmatType(StrEnum):
    AEROSOLS = "AEROSOLS"
    BATTERY = "BATTERY"
    FLAMMABLE_LIQUID = "FLAMMABLE_LIQUID"
    MAGNETIZED = "MAGNETIZED"

    def __str__(self) -> str:
        return str(self.value)
