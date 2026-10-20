from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_conversations_response_data_conversation_latest_message_sender import GetConversationsResponseDataConversationLatestMessageSender





T = TypeVar("T", bound="GetConversationsResponseDataConversationLatestMessage")



@_attrs_define
class GetConversationsResponseDataConversationLatestMessage:
    """ 
        Attributes:
            id (str | Unset): Message ID.
            type_ (str | Unset): Message type.
                Possible enumerations:
                - TEXT
                - IMAGE
                - ALLOCATED_SERVICE - A customer service agent joins the conversation.
                - NOTIFICATION - Notification from the system.
                - BUYER_ENTER_FROM_TRANSFER : The conversation is transferred to another customer service agent.
                - BUYER_ENTER_FROM_PRODUCT : The buyer is viewing a product before sending this message.
                - BUYER_ENTER_FROM_ORDER : The buyer is viewing an order before sending this message.
                - PRODUCT_CARD
                - EMOTICONS
                - ORDER_CARD
                - VIDEO
                - RETURN_REFUND_CARD: Return/refund card.
                - COUPON_CARD
                - OTHER: Messages of types not supported in this API.
            content (str | Unset): Message content, in JSON serialized string.
                Examples of content for each type of message are listed below:
                - TEXT:
                ```
                {
                    "content": "simple text"
                }
                ```

                - IMAGE:
                ```
                {
                    "height": "290",
                    "url": "https://tosv.boei18n.byted.org/obj/temai-im/FszkJ53nSapYG6KDaJQmqR3jjoZGwww304-290",
                    "width": "304"
                }
                ```

                - PRODUCT_CARD, BUYER_ENTER_FROM_PRODUCT:
                ```
                {
                    "product_id": "12345"
                }
                ```

                - ORDER_CARD, BUYER_ENTER_FROM_ORDER :
                ```
                {
                    "order_id": "12345"
                }
                ```

                - RETURN_REFUND_CARD:
                ```
                {
                    "order_id": "12345",
                    "sku_id": "45678"
                }
                ```

                - VIDEO:
                ```
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
                ```

                - ALLOCATED_SERVICE, NOTIFICATION, BUYER_ENTER_FROM_TRANSFER, OTHER:
                ```
                {
                    "content": "simple text"
                }
                ```

                - COUPON_CARD:
                ```
                {
                    "coupon_id": "7262992004278206762"
                }
                ```
                Note: Use [Get Coupon](6699dce0de15e502ed219e37) for the details of the coupon.
            create_time (int | Unset): Unix timestamp for creating the message in seconds.
            is_visible (bool | Unset): Whether this message should be displayed to customer service.
                For example, the buyer will receive a rating request message at the end of the conversation from the system. You
                should not present this type of message to the seller or the customer support agents.
            sender (GetConversationsResponseDataConversationLatestMessageSender | Unset):
            index (str | Unset): Message index. This field can be used to sort messages.
                "index" means the order of the message in the conversation. This value is unique for every message in a
                conversation. This value is time-related, meaning a newer message will get a larger "index". But it is not
                strictly increasing.
     """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    content: str | Unset = UNSET
    create_time: int | Unset = UNSET
    is_visible: bool | Unset = UNSET
    sender: GetConversationsResponseDataConversationLatestMessageSender | Unset = UNSET
    index: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_conversations_response_data_conversation_latest_message_sender import GetConversationsResponseDataConversationLatestMessageSender # noqa: PLC0415
        id = self.id

        type_ = self.type_

        content = self.content

        create_time = self.create_time

        is_visible = self.is_visible

        sender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender, Unset):
            sender = self.sender.to_dict()

        index = self.index


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
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
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_conversations_response_data_conversation_latest_message_sender import GetConversationsResponseDataConversationLatestMessageSender # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        content = d.pop("content", UNSET)

        create_time = d.pop("create_time", UNSET)

        is_visible = d.pop("is_visible", UNSET)

        _sender = d.pop("sender", UNSET)
        sender: GetConversationsResponseDataConversationLatestMessageSender | Unset
        if isinstance(_sender,  Unset):
            sender = UNSET
        else:
            sender = GetConversationsResponseDataConversationLatestMessageSender.from_dict(_sender)




        index = d.pop("index", UNSET)

        get_conversations_response_data_conversation_latest_message = cls(
            id=id,
            type_=type_,
            content=content,
            create_time=create_time,
            is_visible=is_visible,
            sender=sender,
            index=index,
        )


        get_conversations_response_data_conversation_latest_message.additional_properties = d
        return get_conversations_response_data_conversation_latest_message

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
