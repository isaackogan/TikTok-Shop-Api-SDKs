from enum import StrEnum


class SearchGoodsInfoResponseDataGoodHazmatInfoBatteryExtraInfoBatteryPackagingType(StrEnum):
    IN_EQUIPMENT = "IN_EQUIPMENT"
    OTHER = "OTHER"
    STANDALONE = "STANDALONE"
    WITH_EQUIPMENT = "WITH_EQUIPMENT"

    def __str__(self) -> str:
        return str(self.value)
