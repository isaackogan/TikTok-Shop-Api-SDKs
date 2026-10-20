from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AerosolExtraInfo")



@_attrs_define
class AerosolExtraInfo:
    """ 
        Attributes:
            volume (str | Unset): Aerosol volume. Required when `hazmat_type` is `AEROSOLS`. The value must be a numeric
                string greater than 0.
            volume_unit (str | Unset): aeroslo volume unit
     """

    volume: str | Unset = UNSET
    volume_unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        volume = self.volume

        volume_unit = self.volume_unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if volume is not UNSET:
            field_dict["volume"] = volume
        if volume_unit is not UNSET:
            field_dict["volume_unit"] = volume_unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        volume = d.pop("volume", UNSET)

        volume_unit = d.pop("volume_unit", UNSET)

        aerosol_extra_info = cls(
            volume=volume,
            volume_unit=volume_unit,
        )


        aerosol_extra_info.additional_properties = d
        return aerosol_extra_info

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
