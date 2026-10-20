from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.send_im_message_request_msg_type import SendIMMessageRequestMsgType






T = TypeVar("T", bound="SendIMMessageRequest")



@_attrs_define
class SendIMMessageRequest:
    """ 
        Attributes:
            msg_type (SendIMMessageRequestMsgType): Message type. The value determines the decoded JSON object required in
                `content`. Possible values:
                - `TEXT`
                - `PRODUCT_CARD`
                - `TARGET_COLLABORATION_CARD`
                - `FREE_SAMPLE_CARD`
                - `IMAGE`
                - `CRM_TEXT_WITH_IMAGE_CARD`
                - `CRM_TEXT_WITH_PRODUCTS_CARD`
            content (str): Message content as a JSON-serialized string. The decoded JSON object depends on `msg_type`:

                - `TEXT`: `{"content": "simple text"}`. `content` is required, must not be empty, and supports up to 2,000
                Unicode characters.
                - `PRODUCT_CARD`: `{"product_id": "12345"}`. `product_id` is required.
                - `TARGET_COLLABORATION_CARD`: `{"target_collaboration_id": "1234"}`. `target_collaboration_id` is required and
                is the invitation group ID.
                - `FREE_SAMPLE_CARD`: `{"apply_id": "1234"}`. `apply_id` is required.
                - `IMAGE`: `{"url": "https://p16-oec-va.ibyteimg.com/tos-maliva-
                i-o3syd03w52-us/2ca53c34ad8443e6b39f4e0153d3aed4~tplv-o3syd03w52-origin-image.image?from=1320446476", "width":
                1280, "height": 720}`. `url`, `width`, and `height` are required; `width` and `height` must be integers. You can
                obtain `url` by calling [Upload Messages Image](https://partner.tiktokshop.com/docv2/page/upload-message-
                image-v2-202608).
                - `CRM_TEXT_WITH_PRODUCTS_CARD`: `{"product_ids": "12345,123456", "title": "abc", "content": "abc"}`.
                `product_ids` is required and contains one to five comma-separated positive product IDs. `content` is required,
                must not be empty, and supports up to 500 Unicode characters. `title` supports up to 50 Unicode characters.
                - `CRM_TEXT_WITH_IMAGE_CARD`: `{"image_url": "https://p16-oec-va.ibyteimg.com/tos-maliva-
                i-o3syd03w52-us/2ca53c34ad8443e6b39f4e0153d3aed4~tplv-o3syd03w52-origin-image.image?from=1320446476", "title":
                "abc", "content": "abc"}`. `image_url` and `content` are required. `content` must not be empty and supports up
                to 500 Unicode characters. `title` supports up to 50 Unicode characters.
     """

    msg_type: SendIMMessageRequestMsgType
    content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        msg_type = self.msg_type.value

        content = self.content


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "msg_type": msg_type,
            "content": content,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        msg_type = SendIMMessageRequestMsgType(d.pop("msg_type"))




        content = d.pop("content")

        send_im_message_request = cls(
            msg_type=msg_type,
            content=content,
        )


        send_im_message_request.additional_properties = d
        return send_im_message_request

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
