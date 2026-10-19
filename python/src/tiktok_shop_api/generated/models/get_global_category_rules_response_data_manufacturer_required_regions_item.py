from enum import StrEnum


class GetGlobalCategoryRulesResponseDataManufacturerRequiredRegionsItem(StrEnum):
    AT = "AT"
    BE = "BE"
    CZ = "CZ"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GR = "GR"
    HU = "HU"
    IE = "IE"
    IT = "IT"
    NL = "NL"
    PL = "PL"
    PT = "PT"

    def __str__(self) -> str:
        return str(self.value)
