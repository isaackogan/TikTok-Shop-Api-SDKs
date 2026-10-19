from enum import StrEnum


class InvoiceStatusChangeWebhookDataInvoiceStatus(StrEnum):
    FAILED = "FAILED"
    INVALID = "INVALID"
    PROCESSING = "PROCESSING"
    SUCCESS = "SUCCESS"

    def __str__(self) -> str:
        return str(self.value)
