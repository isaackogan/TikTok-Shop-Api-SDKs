from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GoodsSafetyAttribute")



@_attrs_define
class GoodsSafetyAttribute:
    """ 
        Attributes:
            is_fragile (bool | Unset): where fragile
            is_liquid (bool | Unset): Whether the goods are liquid.
            is_sharp (bool | Unset): where sharp
     """

    is_fragile: bool | Unset = UNSET
    is_liquid: bool | Unset = UNSET
    is_sharp: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        is_fragile = self.is_fragile

        is_liquid = self.is_liquid

        is_sharp = self.is_sharp


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_fragile is not UNSET:
            field_dict["is_fragile"] = is_fragile
        if is_liquid is not UNSET:
            field_dict["is_liquid"] = is_liquid
        if is_sharp is not UNSET:
            field_dict["is_sharp"] = is_sharp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_fragile = d.pop("is_fragile", UNSET)

        is_liquid = d.pop("is_liquid", UNSET)

        is_sharp = d.pop("is_sharp", UNSET)

        goods_safety_attribute = cls(
            is_fragile=is_fragile,
            is_liquid=is_liquid,
            is_sharp=is_sharp,
        )


        goods_safety_attribute.additional_properties = d
        return goods_safety_attribute

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
