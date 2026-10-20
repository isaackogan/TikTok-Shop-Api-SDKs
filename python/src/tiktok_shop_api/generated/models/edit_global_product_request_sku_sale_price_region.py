from enum import StrEnum

class EditGlobalProductRequestSkuSalePriceRegion(StrEnum):
    AT = "AT"
    BE = "BE"
    CZ = "CZ"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    GR = "GR"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    MY = "MY"
    NL = "NL"
    PH = "PH"
    PO = "PO"
    PT = "PT"
    SG = "SG"
    TH = "TH"
    US = "US"
    VN = "VN"

    def __str__(self) -> str:
        return str(self.value)
