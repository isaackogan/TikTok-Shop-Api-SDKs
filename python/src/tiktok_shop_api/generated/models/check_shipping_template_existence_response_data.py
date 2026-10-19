from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckShippingTemplateExistenceResponseData")


@_attrs_define
class CheckShippingTemplateExistenceResponseData:
    """
    Attributes:
        template_exist (bool | Unset): if template exists, return true
    """

    template_exist: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_exist = self.template_exist

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_exist is not UNSET:
            field_dict["template_exist"] = template_exist

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template_exist = d.pop("template_exist", UNSET)

        check_shipping_template_existence_response_data = cls(
            template_exist=template_exist,
        )

        check_shipping_template_existence_response_data.additional_properties = d
        return check_shipping_template_existence_response_data

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
