from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetOrderListResponseDataOrderRecipientAddressDeliveryPreference")



@_attrs_define
class GetOrderListResponseDataOrderRecipientAddressDeliveryPreference:
    """ 
        Attributes:
            drop_off_location (str | Unset): Drop-off location selected by the recipient.
     """

    drop_off_location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        drop_off_location = self.drop_off_location


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if drop_off_location is not UNSET:
            field_dict["drop_off_location"] = drop_off_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        drop_off_location = d.pop("drop_off_location", UNSET)

        get_order_list_response_data_order_recipient_address_delivery_preference = cls(
            drop_off_location=drop_off_location,
        )


        get_order_list_response_data_order_recipient_address_delivery_preference.additional_properties = d
        return get_order_list_response_data_order_recipient_address_delivery_preference

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
