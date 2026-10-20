from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_activity_response_data_discount_gift_discount_gift_info import GetActivityResponseDataDiscountGiftDiscountGiftInfo





T = TypeVar("T", bound="GetActivityResponseDataDiscountGiftDiscount")



@_attrs_define
class GetActivityResponseDataDiscountGiftDiscount:
    """ 
        Attributes:
            gift_receiving_type (str | Unset): The receiving type of gift. Currently only supports one type: `ALL_RECEIVE`
            gift_infos (list[GetActivityResponseDataDiscountGiftDiscountGiftInfo] | Unset): Configurations regarding Gift
                With Purchase (GWP) promotions.
                A maximum of two `tier`s are permitted in SEA and UK. Only one `tier` is permitted in US.  And `threshold_type`
                must be the same across all `tier`s.
     """

    gift_receiving_type: str | Unset = UNSET
    gift_infos: list[GetActivityResponseDataDiscountGiftDiscountGiftInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_activity_response_data_discount_gift_discount_gift_info import GetActivityResponseDataDiscountGiftDiscountGiftInfo # noqa: PLC0415
        gift_receiving_type = self.gift_receiving_type

        gift_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gift_infos, Unset):
            gift_infos = []
            for gift_infos_item_data in self.gift_infos:
                gift_infos_item = gift_infos_item_data.to_dict()
                gift_infos.append(gift_infos_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if gift_receiving_type is not UNSET:
            field_dict["gift_receiving_type"] = gift_receiving_type
        if gift_infos is not UNSET:
            field_dict["gift_infos"] = gift_infos

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_activity_response_data_discount_gift_discount_gift_info import GetActivityResponseDataDiscountGiftDiscountGiftInfo # noqa: PLC0415
        d = dict(src_dict)
        gift_receiving_type = d.pop("gift_receiving_type", UNSET)

        _gift_infos = d.pop("gift_infos", UNSET)
        gift_infos: list[GetActivityResponseDataDiscountGiftDiscountGiftInfo] | Unset = UNSET
        if _gift_infos is not UNSET:
            gift_infos = []
            for gift_infos_item_data in _gift_infos:
                gift_infos_item = GetActivityResponseDataDiscountGiftDiscountGiftInfo.from_dict(gift_infos_item_data)



                gift_infos.append(gift_infos_item)


        get_activity_response_data_discount_gift_discount = cls(
            gift_receiving_type=gift_receiving_type,
            gift_infos=gift_infos,
        )


        get_activity_response_data_discount_gift_discount.additional_properties = d
        return get_activity_response_data_discount_gift_discount

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
