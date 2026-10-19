from enum import StrEnum


class SizeChartChangeWebhookDataEventType(StrEnum):
    CREATE = "CREATE"
    DELETE = "DELETE"
    EDIT = "EDIT"

    def __str__(self) -> str:
        return str(self.value)
