from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateCustomEngagementTaskRequestCustomMessage")



@_attrs_define
class CreateCustomEngagementTaskRequestCustomMessage:
    """ 
        Attributes:
            title (str | Unset): The message title.
                - Valid format: plain text, unicode emoji (UTF-8)
                - Valid length: 1–70 Unicode code points.
            body (str | Unset): The message body.
                - Valid format: plain text, unicode emoji (UTF-8)
                - Valid length: 1–500 Unicode code points.
     """

    title: str | Unset = UNSET
    body: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body = self.body


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        body = d.pop("body", UNSET)

        create_custom_engagement_task_request_custom_message = cls(
            title=title,
            body=body,
        )


        create_custom_engagement_task_request_custom_message.additional_properties = d
        return create_custom_engagement_task_request_custom_message

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
