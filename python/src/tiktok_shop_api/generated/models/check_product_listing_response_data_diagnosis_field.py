from enum import StrEnum


class CheckProductListingResponseDataDiagnosisField(StrEnum):
    ATTRIBUTE = "ATTRIBUTE"
    DESCRIPTION = "DESCRIPTION"
    IMAGE = "IMAGE"
    SIZE_CHART = "SIZE_CHART"
    TITLE = "TITLE"

    def __str__(self) -> str:
        return str(self.value)
