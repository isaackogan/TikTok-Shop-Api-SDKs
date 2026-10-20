from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductResponseDataPackageDimension")



@_attrs_define
class GetProductResponseDataPackageDimension:
    """ 
        Attributes:
            height (str | Unset): The package height.
            length (str | Unset): The package length.
            unit (str | Unset): The unit for the package dimensions.
            width (str | Unset): The package width.
     """

    height: str | Unset = UNSET
    length: str | Unset = UNSET
    unit: str | Unset = UNSET
    width: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        height = self.height

        length = self.length

        unit = self.unit

        width = self.width


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if height is not UNSET:
            field_dict["height"] = height
        if length is not UNSET:
            field_dict["length"] = length
        if unit is not UNSET:
            field_dict["unit"] = unit
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        length = d.pop("length", UNSET)

        unit = d.pop("unit", UNSET)

        width = d.pop("width", UNSET)

        get_product_response_data_package_dimension = cls(
            height=height,
            length=length,
            unit=unit,
            width=width,
        )


        get_product_response_data_package_dimension.additional_properties = d
        return get_product_response_data_package_dimension

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
