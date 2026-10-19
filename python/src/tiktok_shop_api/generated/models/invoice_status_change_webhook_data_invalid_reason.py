from enum import StrEnum


class InvoiceStatusChangeWebhookDataInvalidReason(StrEnum):
    ACCESS_KEY_DUPLICATE = "ACCESS_KEY_DUPLICATE"
    CNPJ_NOT_MATCH = "CNPJ_NOT_MATCH"
    FAILED = "FAILED"
    NOT_AUTHORIZED = "NOT_AUTHORIZED"
    NOT_FOUND = "NOT_FOUND"
    UF_INCONSISTENT_DISMISSED_RETIRADA_INCONSISTENT = "UF_Inconsistent_Dismissed_Retirada_Inconsistent"
    UF_INCONSISTENT_DISMISSE_RETIRADA_MISSING = "UF_Inconsistent_Dismisse_Retirada_missing"
    UF_INCONSISTENT_REQUIRED = "UF_Inconsistent_Required"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
