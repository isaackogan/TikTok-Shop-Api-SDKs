from enum import StrEnum


class SKUStatusChangeWebhookDataSkuDeactivationSource(StrEnum):
    COMBO_RELATION = "COMBO_RELATION"
    PLATFORM = "PLATFORM"
    SELLER = "SELLER"

    def __str__(self) -> str:
        return str(self.value)
