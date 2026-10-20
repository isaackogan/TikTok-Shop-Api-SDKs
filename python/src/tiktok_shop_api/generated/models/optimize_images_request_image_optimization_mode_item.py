from enum import StrEnum


class OptimizeImagesRequestImageOptimizationModeItem(StrEnum):
    WHITE_BACKGROUND = "WHITE_BACKGROUND"

    def __str__(self) -> str:
        return str(self.value)
