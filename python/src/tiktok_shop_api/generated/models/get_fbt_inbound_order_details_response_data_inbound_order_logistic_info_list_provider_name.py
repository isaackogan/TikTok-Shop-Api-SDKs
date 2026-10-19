from enum import StrEnum


class GetFBTInboundOrderDetailsResponseDataInboundOrderLogisticInfoListProviderName(StrEnum):
    DHL = "DHL"
    FEDEX = "FEDEX"
    OTHER = "OTHER"
    UPS = "UPS"
    USPS = "USPS"

    def __str__(self) -> str:
        return str(self.value)
