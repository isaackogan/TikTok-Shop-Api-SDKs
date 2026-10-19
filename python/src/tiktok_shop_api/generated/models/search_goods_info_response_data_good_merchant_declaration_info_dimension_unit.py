from enum import StrEnum


class SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoDimensionUnit(StrEnum):
    CENTIMETER = "CENTIMETER"
    FOOT = "FOOT"
    INCH = "INCH"
    METER = "METER"
    MICROMETER = "MICROMETER"
    MILLIMETER = "MILLIMETER"

    def __str__(self) -> str:
        return str(self.value)
