from enum import StrEnum


class GetInboundMethodDetailResponseDataInfoPlacementFeeEstimateCurrency(StrEnum):
    CNY = "CNY"
    EUR = "EUR"
    GBP = "GBP"
    SAR = "SAR"
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
