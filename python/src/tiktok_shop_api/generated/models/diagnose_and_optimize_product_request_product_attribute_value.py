from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagnoseAndOptimizeProductRequestProductAttributeValue")


@_attrs_define
class DiagnoseAndOptimizeProductRequestProductAttributeValue:
    """
    Attributes:
        id (str | Unset): The ID of a built-in product attribute value, retrieved from the [Get Attributes
            API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8).
        name (str | Unset): A self-defined custom product attribute value if the built-in values do not satisfy your
            needs. The system will auto-generate an ID after listing.
            **Note**:
            - No duplicates allowed under the same attribute.
            - Max length: 500 characters
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        diagnose_and_optimize_product_request_product_attribute_value = cls(
            id=id,
            name=name,
        )

        diagnose_and_optimize_product_request_product_attribute_value.additional_properties = d
        return diagnose_and_optimize_product_request_product_attribute_value

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
