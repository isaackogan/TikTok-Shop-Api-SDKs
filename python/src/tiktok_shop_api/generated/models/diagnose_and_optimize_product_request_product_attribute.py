from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diagnose_and_optimize_product_request_product_attribute_value import (
        DiagnoseAndOptimizeProductRequestProductAttributeValue,
    )


T = TypeVar("T", bound="DiagnoseAndOptimizeProductRequestProductAttribute")


@_attrs_define
class DiagnoseAndOptimizeProductRequestProductAttribute:
    """
    Attributes:
        id (str | Unset): The ID of the product attribute, retrieved from the [Get Attributes
            API](https://partner.tiktokshop.com/docv2/page/6509c5784a0bb702c0561cc8).
        values (list[DiagnoseAndOptimizeProductRequestProductAttributeValue] | Unset): A list of selectable values for
            the product attribute.
            **Note**: Provide either a built-in ID or a custom name; if both are provided, the ID takes priority.
    """

    id: str | Unset = UNSET
    values: list[DiagnoseAndOptimizeProductRequestProductAttributeValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnose_and_optimize_product_request_product_attribute_value import (
            DiagnoseAndOptimizeProductRequestProductAttributeValue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _values = d.pop("values", UNSET)
        values: list[DiagnoseAndOptimizeProductRequestProductAttributeValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = DiagnoseAndOptimizeProductRequestProductAttributeValue.from_dict(values_item_data)

                values.append(values_item)

        diagnose_and_optimize_product_request_product_attribute = cls(
            id=id,
            values=values,
        )

        diagnose_and_optimize_product_request_product_attribute.additional_properties = d
        return diagnose_and_optimize_product_request_product_attribute

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
