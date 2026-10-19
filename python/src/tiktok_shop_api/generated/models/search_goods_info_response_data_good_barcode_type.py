from enum import StrEnum


class SearchGoodsInfoResponseDataGoodBarcodeType(StrEnum):
    ASIN_OR_FNSKU = "ASIN_OR_FNSKU"
    EAN = "EAN"
    FBT_SPECIFIC_BARCODE = "FBT_SPECIFIC_BARCODE"
    GTIN = "GTIN"
    MERCHANT_SKU_ID = "MERCHANT_SKU_ID"
    UPC = "UPC"

    def __str__(self) -> str:
        return str(self.value)
