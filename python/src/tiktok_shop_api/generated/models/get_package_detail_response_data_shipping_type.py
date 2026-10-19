from enum import StrEnum


class GetPackageDetailResponseDataShippingType(StrEnum):
    SELLER = "SELLER"
    TIKTOK = "TIKTOK"

    def __str__(self) -> str:
        return str(self.value)
