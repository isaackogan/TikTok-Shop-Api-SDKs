from enum import StrEnum


class SearchProductsForComplianceAuditingResponseDataProductCountry(StrEnum):
    BR = "BR"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    ID = "ID"
    IE = "IE"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    MY = "MY"
    PH = "PH"
    SG = "SG"
    TH = "TH"
    US = "US"
    VN = "VN"

    def __str__(self) -> str:
        return str(self.value)
