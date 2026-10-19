from enum import StrEnum


class GetGlobalCategoryRulesResponseDataManufacturerOptionalRegionsItem(StrEnum):
    DE = "DE"
    ES = "ES"
    FR = "FR"
    IE = "IE"
    IT = "IT"

    def __str__(self) -> str:
        return str(self.value)
