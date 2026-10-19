from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_goods_info_response_data_good_hazmat_info_flammable_liquids_extra_info_flammable_liquids_type import (
    SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfoFlammableLiquidsType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfo")


@_attrs_define
class SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfo:
    """
    Attributes:
        flammable_liquids_type (SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfoFlammableLiquidsType |
            Unset): Flammable liquid type, possible values
            -PAINT
            -PERFUMERY
            -ALCOHOLIC
            -OTHER
        flammable_liquids_volume (str | Unset): Volume of flammable liquid in the unit specified by volume_unit.
        volume_unit (str | Unset): Unit for `flammable_liquids_volume`, such as `MILLILITER`.
    """

    flammable_liquids_type: (
        SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfoFlammableLiquidsType | Unset
    ) = UNSET
    flammable_liquids_volume: str | Unset = UNSET
    volume_unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        flammable_liquids_type: str | Unset = UNSET
        if not isinstance(self.flammable_liquids_type, Unset):
            flammable_liquids_type = self.flammable_liquids_type.value

        flammable_liquids_volume = self.flammable_liquids_volume

        volume_unit = self.volume_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flammable_liquids_type is not UNSET:
            field_dict["flammable_liquids_type"] = flammable_liquids_type
        if flammable_liquids_volume is not UNSET:
            field_dict["flammable_liquids_volume"] = flammable_liquids_volume
        if volume_unit is not UNSET:
            field_dict["volume_unit"] = volume_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _flammable_liquids_type = d.pop("flammable_liquids_type", UNSET)
        flammable_liquids_type: (
            SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfoFlammableLiquidsType | Unset
        )
        if isinstance(_flammable_liquids_type, Unset):
            flammable_liquids_type = UNSET
        else:
            flammable_liquids_type = (
                SearchGoodsInfoResponseDataGoodHazmatInfoFlammableLiquidsExtraInfoFlammableLiquidsType(
                    _flammable_liquids_type
                )
            )

        flammable_liquids_volume = d.pop("flammable_liquids_volume", UNSET)

        volume_unit = d.pop("volume_unit", UNSET)

        search_goods_info_response_data_good_hazmat_info_flammable_liquids_extra_info = cls(
            flammable_liquids_type=flammable_liquids_type,
            flammable_liquids_volume=flammable_liquids_volume,
            volume_unit=volume_unit,
        )

        search_goods_info_response_data_good_hazmat_info_flammable_liquids_extra_info.additional_properties = d
        return search_goods_info_response_data_good_hazmat_info_flammable_liquids_extra_info

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
