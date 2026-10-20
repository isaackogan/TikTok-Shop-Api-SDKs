from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCategoryAttributesResponseDataAttributeValue")


@_attrs_define
class GetCategoryAttributesResponseDataAttributeValue:
    """
    Attributes:
        id (str | Unset): The ID of the built-in attribute value.
        name (str | Unset): The name of the built-in attribute value.
        icon_url (str | Unset): The icon url value of the built-in attribute value.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        icon_url = self.icon_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        icon_url = d.pop("icon_url", UNSET)

        get_category_attributes_response_data_attribute_value = cls(
            id=id,
            name=name,
            icon_url=icon_url,
        )

        get_category_attributes_response_data_attribute_value.additional_properties = d
        return get_category_attributes_response_data_attribute_value

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
