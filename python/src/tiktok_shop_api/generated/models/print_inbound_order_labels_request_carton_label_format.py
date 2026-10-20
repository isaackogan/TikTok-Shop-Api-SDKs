from enum import StrEnum


class PrintInboundOrderLabelsRequestCartonLabelFormat(StrEnum):
    A4_4UP = "A4_4UP"
    DEFAULT_1UP = "DEFAULT_1UP"

    def __str__(self) -> str:
        return str(self.value)
