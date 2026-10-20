from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.flammable_liquids_extra_info_flammable_liquids_type import FlammableLiquidsExtraInfoFlammableLiquidsType
from ..types import UNSET, Unset






T = TypeVar("T", bound="FlammableLiquidsExtraInfo")



@_attrs_define
class FlammableLiquidsExtraInfo:
    """ 
        Attributes:
            flammable_liquids_type (FlammableLiquidsExtraInfoFlammableLiquidsType): Flammable-liquid type.
                Possible values:
                - PAINT
                - PERFUMERY
                - ALCOHOLIC
                - OTHER
            flammable_liquids_volume (str): Volume of flammable liquid in the unit specified by volume_unit.
            volume_unit (str | Unset): Unit for flammable_liquids_volume, such as MILLILITERS.
     """

    flammable_liquids_type: FlammableLiquidsExtraInfoFlammableLiquidsType
    flammable_liquids_volume: str
    volume_unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        flammable_liquids_type = self.flammable_liquids_type.value

        flammable_liquids_volume = self.flammable_liquids_volume

        volume_unit = self.volume_unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "flammable_liquids_type": flammable_liquids_type,
            "flammable_liquids_volume": flammable_liquids_volume,
        })
        if volume_unit is not UNSET:
            field_dict["volume_unit"] = volume_unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        flammable_liquids_type = FlammableLiquidsExtraInfoFlammableLiquidsType(d.pop("flammable_liquids_type"))




        flammable_liquids_volume = d.pop("flammable_liquids_volume")

        volume_unit = d.pop("volume_unit", UNSET)

        flammable_liquids_extra_info = cls(
            flammable_liquids_type=flammable_liquids_type,
            flammable_liquids_volume=flammable_liquids_volume,
            volume_unit=volume_unit,
        )


        flammable_liquids_extra_info.additional_properties = d
        return flammable_liquids_extra_info

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
