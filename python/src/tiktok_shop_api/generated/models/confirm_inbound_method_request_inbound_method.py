from enum import StrEnum

class ConfirmInboundMethodRequestInboundMethod(StrEnum):
    D2FC = "D2FC"
    ONE_HUB = "ONE_HUB"

    def __str__(self) -> str:
        return str(self.value)
