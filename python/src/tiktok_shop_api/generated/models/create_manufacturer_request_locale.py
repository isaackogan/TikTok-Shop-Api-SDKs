from enum import StrEnum

class CreateManufacturerRequestLocale(StrEnum):
    DE_DE = "de-DE"
    EN_IE = "en-IE"
    ES_ES = "es-ES"
    FR_FR = "fr-FR"
    IT_IT = "it-IT"

    def __str__(self) -> str:
        return str(self.value)
