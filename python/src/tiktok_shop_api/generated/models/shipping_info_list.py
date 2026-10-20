from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ShippingInfoList")



@_attrs_define
class ShippingInfoList:
    """ 
        Attributes:
            tracking_number (str | Unset): Tracking number.​
            shipping_provider_id (str | Unset): Use Get Shipping Provider API to retrieve the shipping_provider_id for
                shipping providers.​
            note (str | Unset): "Only available for a part of white list merchants.This applies to scenarios where a large
                single item needs to be shipped in multiple packages.Merchants not on the whitelist who upload this field will
                have it automatically ignored by the platform.
                For example, where Package 1 is marked with ""headboard"" and Package 2 is marked with ""bed frame"".
                This field will be displayed to buyers, so please fill it in carefully."
     """

    tracking_number: str | Unset = UNSET
    shipping_provider_id: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tracking_number = self.tracking_number

        shipping_provider_id = self.shipping_provider_id

        note = self.note


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if shipping_provider_id is not UNSET:
            field_dict["shipping_provider_id"] = shipping_provider_id
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tracking_number = d.pop("tracking_number", UNSET)

        shipping_provider_id = d.pop("shipping_provider_id", UNSET)

        note = d.pop("note", UNSET)

        shipping_info_list = cls(
            tracking_number=tracking_number,
            shipping_provider_id=shipping_provider_id,
            note=note,
        )


        shipping_info_list.additional_properties = d
        return shipping_info_list

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
