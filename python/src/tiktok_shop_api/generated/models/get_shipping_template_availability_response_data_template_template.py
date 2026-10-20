from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShippingTemplateAvailabilityResponseDataTemplateTemplate")


@_attrs_define
class GetShippingTemplateAvailabilityResponseDataTemplateTemplate:
    """
    Attributes:
        template_name (str | Unset): The template name
        template_id (str | Unset): The template_id
        is_default (bool | Unset): Is default template or not
        template_party (int | Unset): 1 for shipping by platform template
            2 for shipping by seller template
    """

    template_name: str | Unset = UNSET
    template_id: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    template_party: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_name = self.template_name

        template_id = self.template_id

        is_default = self.is_default

        template_party = self.template_party

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_name is not UNSET:
            field_dict["template_name"] = template_name
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if template_party is not UNSET:
            field_dict["template_party"] = template_party

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_name = d.pop("template_name", UNSET)

        template_id = d.pop("template_id", UNSET)

        is_default = d.pop("is_default", UNSET)

        template_party = d.pop("template_party", UNSET)

        get_shipping_template_availability_response_data_template_template = cls(
            template_name=template_name,
            template_id=template_id,
            is_default=is_default,
            template_party=template_party,
        )

        get_shipping_template_availability_response_data_template_template.additional_properties = d
        return get_shipping_template_availability_response_data_template_template

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
