from enum import StrEnum


class GetConversationsLocale(StrEnum):
    DE_DE = "de-DE"
    EN = "en"
    EN_GB = "en-GB"
    ES_ES = "es-ES"
    ES_MX = "es-MX"
    FR_FR = "fr-FR"
    ID_ID = "id-ID"
    IT_IT = "it-IT"
    JA_JP = "ja-JP"
    MS_MY = "ms-MY"
    PT_BR = "pt-BR"
    TH_TH = "th-TH"
    VI_VN = "vi-VN"
    ZH_CN = "zh-CN"

    def __str__(self) -> str:
        return str(self.value)
