from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_message_webhook_data_sender import NewMessageWebhookDataSender


T = TypeVar("T", bound="NewMessageWebhookData")


@_attrs_define
class NewMessageWebhookData:
    """
    Attributes:
        message_id (str | Unset): The identification of the message
        index (str | Unset): The message index that can be used to sort messages.
             Newer messages have a larger index.
        conversation_id (str | Unset): The identification of the conversation
        type_ (str | Unset): Message type, with possible values:
             * TEXT
             * IMAGE
             * ALLOCATED_SERVICE
             * NOTIFICATION
             * BUYER_ENTER_FROM_TRANSFER
             * BUYER_ENTER_FROM_PRODUCT
             * BUYER_ENTER_FROM_ORDER
             * PRODUCT_CARD
             * ORDER_CARD
             * EMOTICONS
             * VIDEO
             * COUPON_CARD
             *LOGISTICS_CARD
             * OTHER
        content (str | Unset): Message content, in JSON serialized string.
             Examples:

             * TEXT:
             {"content": "simple text"}

             * IMAGE:
             {
                  "height": "290",
                  "url": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290",
                  "width": "304"
              }

             * PRODUCT_CARD, BUYER_ENTER_FROM_PRODUCT:
              {"product_id": "12345"}

             * ORDER_CARD, BUYER_ENTER_FROM_ORDER :
              {"order_id": "12345"}

             * VIDEO:
              {
                  "url": "https://video-boei18n.byted.org/storage/v1/tos-
            boei18n-v-c72c01/e8240f35244646428df9c3244d1a7408?x-tos-algorithm=v2&x-tos-
            authkey=5bf25627da095a5cba28ace592de46cc&x-tos-expires=1681980481&x-tos-signature=r_bRxtrvGhXAuZgMmNhlZ_Upqzg",
                  "cover": "https://p-boei18n.byted.org/tos-boei18n-v-c72c01/o8keEOhzTcNCcJyAbkWZwpLIyTfkJxcGbRBvLP~tplv-
            jvtte31kaf-origin-jpeg.jpeg?",
                  "width": 640,
                  "height": 360,
                  "duration": "20.504",
                  "vid": "v0e30cg700f7cgcmu8jc77u9e2bdp95g",
                  "expire_time": "1681980481",
                  "format": "mp4",
                  "size": 400000,
                  "bit_rate": 156067,
                  "quality": "original",
                  "codec_type": "h264"
              }

             * LOGISTICS_CARD:
             {
                 "order_id": "580874485811283206",
                 "package_id": "123456"  // Optional  (recommended for one order with multiple packages; not required for
            one order with one package)
             }

             * COUPON_CARD:
              {"coupon_id": "7262992004278206762"}


             Note: Use Get Coupon for the details of the coupon.

             * ALLOCATED_SERVICE, NOTIFICATION, BUYER_ENTER_FROM_TRANSFER, OTHER:
             {"content": "simple text"}
        create_time (int | Unset): Message creation time, represented as a Unix timestamp (seconds).
        is_visible (bool | Unset): Whether this message should be displayed to customer service.
        sender (NewMessageWebhookDataSender | Unset):
    """

    message_id: str | Unset = UNSET
    index: str | Unset = UNSET
    conversation_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    content: str | Unset = UNSET
    create_time: int | Unset = UNSET
    is_visible: bool | Unset = UNSET
    sender: NewMessageWebhookDataSender | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        index = self.index

        conversation_id = self.conversation_id

        type_ = self.type_

        content = self.content

        create_time = self.create_time

        is_visible = self.is_visible

        sender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if index is not UNSET:
            field_dict["index"] = index
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if content is not UNSET:
            field_dict["content"] = content
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if is_visible is not UNSET:
            field_dict["is_visible"] = is_visible
        if sender is not UNSET:
            field_dict["sender"] = sender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_message_webhook_data_sender import NewMessageWebhookDataSender  # noqa: PLC0415

        d = dict(src_dict)
        message_id = d.pop("message_id", UNSET)

        index = d.pop("index", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        type_ = d.pop("type", UNSET)

        content = d.pop("content", UNSET)

        create_time = d.pop("create_time", UNSET)

        is_visible = d.pop("is_visible", UNSET)

        _sender = d.pop("sender", UNSET)
        sender: NewMessageWebhookDataSender | Unset
        if isinstance(_sender, Unset):
            sender = UNSET
        else:
            sender = NewMessageWebhookDataSender.from_dict(_sender)

        new_message_webhook_data = cls(
            message_id=message_id,
            index=index,
            conversation_id=conversation_id,
            type_=type_,
            content=content,
            create_time=create_time,
            is_visible=is_visible,
            sender=sender,
        )

        new_message_webhook_data.additional_properties = d
        return new_message_webhook_data

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
