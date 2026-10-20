from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetPackageDetailResponseDataSenderAddress")



@_attrs_define
class GetPackageDetailResponseDataSenderAddress:
    """ 
        Attributes:
            full_address (str | Unset): The complete sender address, including geographic address components and address
                details.
            phone_number (str | Unset): The telephone number of the sender.
            name (str | Unset): The name of the sender.
            postal_code (str | Unset): The postal code of the sender.
            address_detail (str | Unset): The detailed street-address portion of the sender's address.
            region_code (str | Unset): Region code of the sender.
            address_line1 (str | Unset): The first line of the sender's street address.
            address_line2 (str | Unset): The second line of the sender's street address.
            address_line3 (str | Unset): The third line of the sender's street address. Usually only for the Brazilian
                market.
            address_line4 (str | Unset): The fourth line of the sender's street address. Usually only for the Brazilian
                market.
     """

    full_address: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    name: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    address_detail: str | Unset = UNSET
    region_code: str | Unset = UNSET
    address_line1: str | Unset = UNSET
    address_line2: str | Unset = UNSET
    address_line3: str | Unset = UNSET
    address_line4: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        full_address = self.full_address

        phone_number = self.phone_number

        name = self.name

        postal_code = self.postal_code

        address_detail = self.address_detail

        region_code = self.region_code

        address_line1 = self.address_line1

        address_line2 = self.address_line2

        address_line3 = self.address_line3

        address_line4 = self.address_line4


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if full_address is not UNSET:
            field_dict["full_address"] = full_address
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if name is not UNSET:
            field_dict["name"] = name
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if address_detail is not UNSET:
            field_dict["address_detail"] = address_detail
        if region_code is not UNSET:
            field_dict["region_code"] = region_code
        if address_line1 is not UNSET:
            field_dict["address_line1"] = address_line1
        if address_line2 is not UNSET:
            field_dict["address_line2"] = address_line2
        if address_line3 is not UNSET:
            field_dict["address_line3"] = address_line3
        if address_line4 is not UNSET:
            field_dict["address_line4"] = address_line4

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_address = d.pop("full_address", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        name = d.pop("name", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        address_detail = d.pop("address_detail", UNSET)

        region_code = d.pop("region_code", UNSET)

        address_line1 = d.pop("address_line1", UNSET)

        address_line2 = d.pop("address_line2", UNSET)

        address_line3 = d.pop("address_line3", UNSET)

        address_line4 = d.pop("address_line4", UNSET)

        get_package_detail_response_data_sender_address = cls(
            full_address=full_address,
            phone_number=phone_number,
            name=name,
            postal_code=postal_code,
            address_detail=address_detail,
            region_code=region_code,
            address_line1=address_line1,
            address_line2=address_line2,
            address_line3=address_line3,
            address_line4=address_line4,
        )


        get_package_detail_response_data_sender_address.additional_properties = d
        return get_package_detail_response_data_sender_address

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
