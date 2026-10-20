from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_message_templates_response_data_message_template import (
        GetMessageTemplatesResponseDataMessageTemplate,
    )


T = TypeVar("T", bound="GetMessageTemplatesResponseData")


@_attrs_define
class GetMessageTemplatesResponseData:
    """
    Attributes:
        message_templates (list[GetMessageTemplatesResponseDataMessageTemplate] | Unset): Customer engagement message
            templates predefined by TikTok Shop.
    """

    message_templates: list[GetMessageTemplatesResponseDataMessageTemplate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_templates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.message_templates, Unset):
            message_templates = []
            for message_templates_item_data in self.message_templates:
                message_templates_item = message_templates_item_data.to_dict()
                message_templates.append(message_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_templates is not UNSET:
            field_dict["message_templates"] = message_templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_message_templates_response_data_message_template import (
            GetMessageTemplatesResponseDataMessageTemplate,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _message_templates = d.pop("message_templates", UNSET)
        message_templates: list[GetMessageTemplatesResponseDataMessageTemplate] | Unset = UNSET
        if _message_templates is not UNSET:
            message_templates = []
            for message_templates_item_data in _message_templates:
                message_templates_item = GetMessageTemplatesResponseDataMessageTemplate.from_dict(
                    message_templates_item_data
                )

                message_templates.append(message_templates_item)

        get_message_templates_response_data = cls(
            message_templates=message_templates,
        )

        get_message_templates_response_data.additional_properties = d
        return get_message_templates_response_data

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
