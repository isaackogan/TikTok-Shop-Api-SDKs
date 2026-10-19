from enum import StrEnum


class GetMessageTemplatesResponseDataMessageTemplateCouponCardRuleCouponTypeItem(StrEnum):
    REGULAR_ALL = "REGULAR_ALL"
    REGULAR_REPEAT = "REGULAR_REPEAT"

    def __str__(self) -> str:
        return str(self.value)
