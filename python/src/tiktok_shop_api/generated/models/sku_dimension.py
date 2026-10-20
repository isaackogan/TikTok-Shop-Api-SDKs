from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SkuDimension")



@_attrs_define
class SkuDimension:
    """ 
        Attributes:
            length (str): The package length. A positive whole number.
                Note: For the BR market, decimal values using . or , as separators are also accepted but will be rounded to the
                nearest whole number.
            width (str): The package width. A positive whole number.
                Note: For the BR market, decimal values using . or , as separators are also accepted but will be rounded to the
                nearest whole number.
            height (str): The package height. A positive whole number.
                Note: For the BR market, decimal values using . or , as separators are also accepted but will be rounded to the
                nearest whole number.
            unit (str): The unit for the SKU dimensions.
                Possible values based on region:
                - US: CENTIMETER, INCH
                - Other regions: CENTIMETER

                Note: Use the same measurement system (metric or imperial) for `sku_weight` and `sku_dimensions`. For example,
                use `KILOGRAM` with `CENTIMETER`.
     """

    length: str
    width: str
    height: str
    unit: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        length = self.length

        width = self.width

        height = self.height

        unit = self.unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "length": length,
            "width": width,
            "height": height,
            "unit": unit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        length = d.pop("length")

        width = d.pop("width")

        height = d.pop("height")

        unit = d.pop("unit")

        sku_dimension = cls(
            length=length,
            width=width,
            height=height,
            unit=unit,
        )


        sku_dimension.additional_properties = d
        return sku_dimension

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
