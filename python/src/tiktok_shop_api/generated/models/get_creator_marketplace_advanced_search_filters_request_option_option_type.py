from enum import StrEnum


class GetCreatorMarketplaceAdvancedSearchFiltersRequestOptionOptionType(StrEnum):
    OPTION_BRAND = "OPTION_BRAND"
    OPTION_CREATOR_LEVEL = "OPTION_CREATOR_LEVEL"
    OPTION_LANGUAGE = "OPTION_LANGUAGE"
    OPTION_SORTER = "OPTION_SORTER"
    OPTION_VERTICAL_PRO = "OPTION_VERTICAL_PRO"

    def __str__(self) -> str:
        return str(self.value)
