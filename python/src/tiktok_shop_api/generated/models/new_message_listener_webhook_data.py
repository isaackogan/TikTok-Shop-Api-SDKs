from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.new_message_listener_webhook_data_sender import NewMessageListenerWebhookDataSender





T = TypeVar("T", bound="NewMessageListenerWebhookData")



@_attrs_define
class NewMessageListenerWebhookData:
    """ 
        Attributes:
            index (str | Unset): Index of the message in the conversation. A large index number corresponds to newer
                message.
            message_id (str | Unset): Message ID.
            conversation_id (str | Unset): ID of the conversation to which the message belongs.
            msg_type (str | Unset): Message type, with possible values:

                 * TEXT
                 * PRODUCT_CARD
                 * TARGET_COLLABORATION_CARD
                 * FREE_SAMPLE_CARD
            content (str | Unset): Message content, in JSON serialized string.

                 * TEXT: {"content": "simple text"}
                 * PRODUCT_CARD: {"product_id": "12345"}
                 * TARGET_INVITATION_CARD: {"invitation_group_id": "1234"}
                 * FREE_SAMPLE_CARD: {"apply_id": "1234"}
            create_time (str | Unset): Message creation time, represented as a Unix timestamp (seconds).
            sender (NewMessageListenerWebhookDataSender | Unset):
     """

    index: str | Unset = UNSET
    message_id: str | Unset = UNSET
    conversation_id: str | Unset = UNSET
    msg_type: str | Unset = UNSET
    content: str | Unset = UNSET
    create_time: str | Unset = UNSET
    sender: NewMessageListenerWebhookDataSender | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.new_message_listener_webhook_data_sender import NewMessageListenerWebhookDataSender # noqa: PLC0415
        index = self.index

        message_id = self.message_id

        conversation_id = self.conversation_id

        msg_type = self.msg_type

        content = self.content

        create_time = self.create_time

        sender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if index is not UNSET:
            field_dict["index"] = index
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if msg_type is not UNSET:
            field_dict["msg_type"] = msg_type
        if content is not UNSET:
            field_dict["content"] = content
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if sender is not UNSET:
            field_dict["sender"] = sender

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_message_listener_webhook_data_sender import NewMessageListenerWebhookDataSender # noqa: PLC0415
        d = dict(src_dict)
        index = d.pop("index", UNSET)

        message_id = d.pop("message_id", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        msg_type = d.pop("msg_type", UNSET)

        content = d.pop("content", UNSET)

        create_time = d.pop("create_time", UNSET)

        _sender = d.pop("sender", UNSET)
        sender: NewMessageListenerWebhookDataSender | Unset
        if isinstance(_sender,  Unset):
            sender = UNSET
        else:
            sender = NewMessageListenerWebhookDataSender.from_dict(_sender)




        new_message_listener_webhook_data = cls(
            index=index,
            message_id=message_id,
            conversation_id=conversation_id,
            msg_type=msg_type,
            content=content,
            create_time=create_time,
            sender=sender,
        )


        new_message_listener_webhook_data.additional_properties = d
        return new_message_listener_webhook_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
