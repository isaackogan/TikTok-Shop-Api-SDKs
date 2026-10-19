from enum import StrEnum


class GetFBTInboundOrderDetailsResponseDataInboundOrderWarehouseType(StrEnum):
    FC = "FC"
    HUB = "HUB"

    def __str__(self) -> str:
        return str(self.value)
