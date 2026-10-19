from enum import StrEnum


class GetProductPackageRecommendationsResponseDataProductAbnormalityTypesItem(StrEnum):
    DIMENSION = "Dimension"
    NONE = "None"
    WEIGHT = "Weight"

    def __str__(self) -> str:
        return str(self.value)
