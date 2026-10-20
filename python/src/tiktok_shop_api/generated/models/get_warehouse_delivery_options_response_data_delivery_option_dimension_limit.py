from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetWarehouseDeliveryOptionsResponseDataDeliveryOptionDimensionLimit")



@_attrs_define
class GetWarehouseDeliveryOptionsResponseDataDeliveryOptionDimensionLimit:
    """ 
        Attributes:
            max_height (int | Unset): Maximum height limit.
            max_length (int | Unset): Maximum length limit.
            max_width (int | Unset): Maximum width limit.
            unit (str | Unset): The unit of measurement for the dimensions, with possible values:
                - CM
                - INCH
     """

    max_height: int | Unset = UNSET
    max_length: int | Unset = UNSET
    max_width: int | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        max_height = self.max_height

        max_length = self.max_length

        max_width = self.max_width

        unit = self.unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if max_height is not UNSET:
            field_dict["max_height"] = max_height
        if max_length is not UNSET:
            field_dict["max_length"] = max_length
        if max_width is not UNSET:
            field_dict["max_width"] = max_width
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_height = d.pop("max_height", UNSET)

        max_length = d.pop("max_length", UNSET)

        max_width = d.pop("max_width", UNSET)

        unit = d.pop("unit", UNSET)

        get_warehouse_delivery_options_response_data_delivery_option_dimension_limit = cls(
            max_height=max_height,
            max_length=max_length,
            max_width=max_width,
            unit=unit,
        )


        get_warehouse_delivery_options_response_data_delivery_option_dimension_limit.additional_properties = d
        return get_warehouse_delivery_options_response_data_delivery_option_dimension_limit

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
