from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetEligibleShippingServicesResponseDataDimension")



@_attrs_define
class GetEligibleShippingServicesResponseDataDimension:
    """ 
        Attributes:
            length (str | Unset): The length of the package.
            width (str | Unset): The width of the package.
            height (str | Unset): The height of the package.
            unit (str | Unset): The unit of measurement for the package dimensions.
                - CM
                - INCH
     """

    length: str | Unset = UNSET
    width: str | Unset = UNSET
    height: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        length = self.length

        width = self.width

        height = self.height

        unit = self.unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        unit = d.pop("unit", UNSET)

        get_eligible_shipping_services_response_data_dimension = cls(
            length=length,
            width=width,
            height=height,
            unit=unit,
        )


        get_eligible_shipping_services_response_data_dimension.additional_properties = d
        return get_eligible_shipping_services_response_data_dimension

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
