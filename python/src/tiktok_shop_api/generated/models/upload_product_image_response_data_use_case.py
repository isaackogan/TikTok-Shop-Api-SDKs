from enum import StrEnum


class UploadProductImageResponseDataUseCase(StrEnum):
    ATTRIBUTE_IMAGE = "ATTRIBUTE_IMAGE"
    CERTIFICATION_IMAGE = "CERTIFICATION_IMAGE"
    CUSTOMIZATION_IMAGE = "CUSTOMIZATION_IMAGE"
    DESCRIPTION_IMAGE = "DESCRIPTION_IMAGE"
    MAIN_IMAGE = "MAIN_IMAGE"
    SIZE_CHART_IMAGE = "SIZE_CHART_IMAGE"

    def __str__(self) -> str:
        return str(self.value)
