from enum import StrEnum


class SearchGoodsInfoResponseDataGoodHazmatInfoHazmatType(StrEnum):
    AEROSOLS = "AEROSOLS"
    BATTERY = "BATTERY"
    FLAMMABLE_LIQUID = "FLAMMABLE_LIQUID"
    MAGNETIZED = "MAGNETIZED"

    def __str__(self) -> str:
        return str(self.value)
