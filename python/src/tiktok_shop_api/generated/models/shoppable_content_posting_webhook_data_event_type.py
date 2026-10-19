from enum import StrEnum


class ShoppableContentPostingWebhookDataEventType(StrEnum):
    ADD = "ADD"
    REMOVE = "REMOVE"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
