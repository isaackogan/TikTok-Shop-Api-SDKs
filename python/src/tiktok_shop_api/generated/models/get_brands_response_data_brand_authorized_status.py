from enum import StrEnum


class GetBrandsResponseDataBrandAuthorizedStatus(StrEnum):
    AUTHORIZED = "AUTHORIZED"
    UNAUTHORIEZD = "UNAUTHORIEZD"

    def __str__(self) -> str:
        return str(self.value)
