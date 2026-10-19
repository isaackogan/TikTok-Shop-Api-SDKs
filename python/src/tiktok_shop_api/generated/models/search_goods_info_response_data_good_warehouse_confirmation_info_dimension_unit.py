from enum import StrEnum


class SearchGoodsInfoResponseDataGoodWarehouseConfirmationInfoDimensionUnit(StrEnum):
    CENTIMETER = "CENTIMETER"
    FOOT = "FOOT"
    INCH = "INCH"
    METER = "METER"
    MICRO = "MICRO"
    MILLIMETER = "MILLIMETER"

    def __str__(self) -> str:
        return str(self.value)
