from enum import StrEnum

class PartialEditGlobalProductRequestSkuSalePriceRegion(StrEnum):
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    ID = "ID"
    IE = "IE"
    IT = "IT"
    JP = "JP"
    MY = "MY"
    PH = "PH"
    SG = "SG"
    TH = "TH"
    US = "US"
    VN = "VN"

    def __str__(self) -> str:
        return str(self.value)
