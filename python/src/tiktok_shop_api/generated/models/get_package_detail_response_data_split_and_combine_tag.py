from enum import StrEnum


class GetPackageDetailResponseDataSplitAndCombineTag(StrEnum):
    COMBINE = "COMBINE"
    DEFAULT = "DEFAULT"
    SPLIT = "SPLIT"

    def __str__(self) -> str:
        return str(self.value)
