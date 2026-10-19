from enum import StrEnum


class GetRecommendedProductTitleAndDescriptionResponseDataProductSuggestionField(StrEnum):
    DESCRIPTION = "DESCRIPTION"
    TITLE = "TITLE"

    def __str__(self) -> str:
        return str(self.value)
