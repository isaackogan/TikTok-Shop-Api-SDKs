from enum import StrEnum


class RecommendCategoryRequestLocale(StrEnum):
    CS_CZ = "cs-CZ"
    DE_AT = "de-AT"
    DE_BE = "de-BE"
    DE_DE = "de-DE"
    EL_GR = "el-GR"
    EN_GB = "en-GB"
    EN_IE = "en-IE"
    EN_US = "en-US"
    ES_ES = "es-ES"
    ES_MX = "es-MX"
    FR_BE = "fr-BE"
    FR_FR = "fr-FR"
    HU_HU = "hu-HU"
    ID_ID = "id-ID"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    MS_MY = "ms-MY"
    NL_BE = "nl-BE"
    NL_NL = "nl-NL"
    PL_PL = "pl-PL"
    PT_BR = "pt-BR"
    PT_PT = "pt-PT"
    TH_TH = "th-TH"
    VI_VN = "vi-VN"
    ZH_CN = "zh-CN"

    def __str__(self) -> str:
        return str(self.value)
