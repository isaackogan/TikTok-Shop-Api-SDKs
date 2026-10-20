from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.send_message_request_type import SendMessageRequestType
from ..types import UNSET, Unset






T = TypeVar("T", bound="SendMessageRequest")



@_attrs_define
class SendMessageRequest:
    """ 
        Attributes:
            type_ (SendMessageRequestType): Message type. Possible enumerations:
                - `TEXT`
                - `IMAGE`
                - `VIDEO`
                - `PRODUCT_CARD`
                - `ORDER_CARD`
                - `RETURN_REFUND_CARD`
                - `COUPON_CARD`
                - `LOGISTICS_CARD`
            content (str): Message content, in JSON serialized string.

                Examples of content for each type of message are listed below:
                ​
                - TEXT:
                {
                    "content": "hi, I want to get refunded."
                }
                (Note: Max 2000 characters. Do not use sensitive words that violate TikTok Shop terms & policies.)

                - VIDEO
                {
                    "vid": "v10394g5000cd499vc7og65mqn3r3dg0"
                }

                - LOGISTICS_CARD
                {
                    "order_id": "580874485811283206",
                    "package_id": "123456"  // Optional  (recommended for one order with multiple packages; not required for one
                order with one package)
                }
                ​
                - PRODUCT_CARD
                {
                    "product_id": "7494560109732334265"
                }
                ​
                - ORDER_CARD:
                {
                    "order_id": "7494560109732334267"
                }

                - RETURN_REFUND_CARD:
                {
                    "order_id": "7494560109732334267",
                    "sku_id": "7494560109732363423"
                }
                Note: The order of the RETURN_REFUND_CARD to send must meet after-sale conditions. To check the eligibility, use
                [Get Aftersale Eligibility](650ab645c16ffe02b8f2e1c1).
                ​
                - IMAGE:
                {
                    "url":"https://p16-oec-va.ibyteimg.com/tos-maliva-
                i-o3syd03w52-us/2ca53c34ad8443e6b39f4e0153d3aed4~tplv-o3syd03w52-origin-image.image?from=1320446476",
                    "width": 1280,
                    "height": 720
                }

                Note: You can get the value of `url` by calling [Upload Buyer Messages Image](650a599d0fcef602bf2a1dc8).

                - COUPON_CARD:
                {
                    "coupon_id": "7262992004278206762"
                }
                Note: Coupons that can be sent in  a message must meet all the following conditions:
                1. `display_type==CHAT` or `display_type==REGULAR`
                2. `status==ONGOING`
                3. `creation_source==SELLER_CENTER`
                4. `target_buyer_segment!=REPEAT_CUSTOMERS`
            sender_role (str | Unset): Message sending role.
                - 'CUSTOMER_SERVICE' : Messages replied by real customer service
                - 'SYSTEM': Replies automatically triggered by the system, such as welcome messages and timeout replies
                - 'ROBOT': Messages replied by intelligent robot
     """

    type_: SendMessageRequestType
    content: str
    sender_role: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        content = self.content

        sender_role = self.sender_role


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "content": content,
        })
        if sender_role is not UNSET:
            field_dict["sender_role"] = sender_role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SendMessageRequestType(d.pop("type"))




        content = d.pop("content")

        sender_role = d.pop("sender_role", UNSET)

        send_message_request = cls(
            type_=type_,
            content=content,
            sender_role=sender_role,
        )


        send_message_request.additional_properties = d
        return send_message_request

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
