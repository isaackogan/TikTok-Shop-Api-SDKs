from enum import StrEnum


class CreateImageTranslationTasksRequestImageTargetLanguagesItem(StrEnum):
    CS_CZ = "cs-CZ"
    DA_DK = "da-DK"
    DE_AT = "de-AT"
    DE_BE = "de-BE"
    DE_DE = "de-DE"
    EL_GR = "el-GR"
    EN_GB = "en-GB"
    EN_IE = "en-IE"
    ES_ES = "es-ES"
    FI_FI = "fi-FI"
    FR_BE = "fr-BE"
    FR_FR = "fr-FR"
    HU_HU = "hu-HU"
    IT_IT = "it-IT"
    NL_BE = "nl-BE"
    NL_NL = "nl-NL"
    PL_PL = "pl-PL"
    PT_PT = "pt-PT"
    SV_SE = "sv-SE"

    def __str__(self) -> str:
        return str(self.value)
