from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateFBTGoodsInfoRequestUpdateGoodsDtoBulkyItemAttribute")



@_attrs_define
class UpdateFBTGoodsInfoRequestUpdateGoodsDtoBulkyItemAttribute:
    """ 
        Attributes:
            is_bulky_item_accessories (bool | Unset): whether the goods is bulky accessories
     """

    is_bulky_item_accessories: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        is_bulky_item_accessories = self.is_bulky_item_accessories


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_bulky_item_accessories is not UNSET:
            field_dict["is_bulky_item_accessories"] = is_bulky_item_accessories

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_bulky_item_accessories = d.pop("is_bulky_item_accessories", UNSET)

        update_fbt_goods_info_request_update_goods_dto_bulky_item_attribute = cls(
            is_bulky_item_accessories=is_bulky_item_accessories,
        )


        update_fbt_goods_info_request_update_goods_dto_bulky_item_attribute.additional_properties = d
        return update_fbt_goods_info_request_update_goods_dto_bulky_item_attribute

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
