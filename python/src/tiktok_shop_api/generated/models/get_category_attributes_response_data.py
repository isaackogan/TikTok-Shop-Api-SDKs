from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_category_attributes_response_data_attribute import GetCategoryAttributesResponseDataAttribute


T = TypeVar("T", bound="GetCategoryAttributesResponseData")


@_attrs_define
class GetCategoryAttributesResponseData:
    """
    Attributes:
        attributes (list[GetCategoryAttributesResponseDataAttribute] | Unset): The list of standard built-in product and
            sales attributes that are bound to the specified category, based on your shop's location.
    """

    attributes: list[GetCategoryAttributesResponseDataAttribute] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()
                attributes.append(attributes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_category_attributes_response_data_attribute import (
            GetCategoryAttributesResponseDataAttribute,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _attributes = d.pop("attributes", UNSET)
        attributes: list[GetCategoryAttributesResponseDataAttribute] | Unset = UNSET
        if _attributes is not UNSET:
            attributes = []
            for attributes_item_data in _attributes:
                attributes_item = GetCategoryAttributesResponseDataAttribute.from_dict(attributes_item_data)

                attributes.append(attributes_item)

        get_category_attributes_response_data = cls(
            attributes=attributes,
        )

        get_category_attributes_response_data.additional_properties = d
        return get_category_attributes_response_data

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
