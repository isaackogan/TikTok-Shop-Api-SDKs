from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_warehouse_list_response_data_warehouse_address_geolocation import (
        GetWarehouseListResponseDataWarehouseAddressGeolocation,
    )


T = TypeVar("T", bound="GetWarehouseListResponseDataWarehouseAddress")


@_attrs_define
class GetWarehouseListResponseDataWarehouseAddress:
    """
    Attributes:
        region (str | Unset): The country or region of the warehouse address.
        state (str | Unset): Warehouse state or province.
        city (str | Unset): Warehouse city.
        distict (str | Unset): Warehouse district.
        town (str | Unset): Warehouse town.
        contact_person (str | Unset): Warehouse contact person name.
        first_name (str | Unset): Kanji first name
            Applicable only for the JP market.
        last_name (str | Unset): Kanji last name
            Applicable only for the JP market.
        first_name_local_script (str | Unset): Hiragana or Katakana first name
            Applicable only for the JP market.
        last_name_local_script (str | Unset): Hiragana or Katakana last name
            Applicable only for the JP market.
        postal_code (str | Unset): Warehouse address postal code (also known as zip code)
        full_address (str | Unset): The combined warehouse address, including the street address and other address
            information such as apartment number, building, floor..etc (optional)
        region_code (str | Unset): The country or region code of the warehouse address.
        phone_number (str | Unset): Warehouse phone number.
        address_line1 (str | Unset): The first line of the warehouse address, like street name and street number.
            Note:
            - For Brazilian market, this represents the neighborhood or district.
            - For the JP market, this represents the district (Chome), block (Banchi), building number (Go).
        address_line2 (str | Unset): The second line of the warehouse address, like flat, apartment, or suit.
            Note: For the Brazilian market, this represents the street name.
        address_line3 (str | Unset): The street number. The literal value `s/n` indicates that no street number is
            available. Available only in the Brazilian market.
        address_line4 (str | Unset): This represents supplement information, like flat, apartment, or suit (optional).
            Note: Available only in the Brazilian market.
        geolocation (GetWarehouseListResponseDataWarehouseAddressGeolocation | Unset):
    """

    region: str | Unset = UNSET
    state: str | Unset = UNSET
    city: str | Unset = UNSET
    distict: str | Unset = UNSET
    town: str | Unset = UNSET
    contact_person: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    first_name_local_script: str | Unset = UNSET
    last_name_local_script: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    full_address: str | Unset = UNSET
    region_code: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    address_line1: str | Unset = UNSET
    address_line2: str | Unset = UNSET
    address_line3: str | Unset = UNSET
    address_line4: str | Unset = UNSET
    geolocation: GetWarehouseListResponseDataWarehouseAddressGeolocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region

        state = self.state

        city = self.city

        distict = self.distict

        town = self.town

        contact_person = self.contact_person

        first_name = self.first_name

        last_name = self.last_name

        first_name_local_script = self.first_name_local_script

        last_name_local_script = self.last_name_local_script

        postal_code = self.postal_code

        full_address = self.full_address

        region_code = self.region_code

        phone_number = self.phone_number

        address_line1 = self.address_line1

        address_line2 = self.address_line2

        address_line3 = self.address_line3

        address_line4 = self.address_line4

        geolocation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geolocation, Unset):
            geolocation = self.geolocation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city
        if distict is not UNSET:
            field_dict["distict"] = distict
        if town is not UNSET:
            field_dict["town"] = town
        if contact_person is not UNSET:
            field_dict["contact_person"] = contact_person
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if first_name_local_script is not UNSET:
            field_dict["first_name_local_script"] = first_name_local_script
        if last_name_local_script is not UNSET:
            field_dict["last_name_local_script"] = last_name_local_script
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if full_address is not UNSET:
            field_dict["full_address"] = full_address
        if region_code is not UNSET:
            field_dict["region_code"] = region_code
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if address_line1 is not UNSET:
            field_dict["address_line1"] = address_line1
        if address_line2 is not UNSET:
            field_dict["address_line2"] = address_line2
        if address_line3 is not UNSET:
            field_dict["address_line3"] = address_line3
        if address_line4 is not UNSET:
            field_dict["address_line4"] = address_line4
        if geolocation is not UNSET:
            field_dict["geolocation"] = geolocation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_warehouse_list_response_data_warehouse_address_geolocation import (
            GetWarehouseListResponseDataWarehouseAddressGeolocation,  # noqa: PLC0415
        )

        d = dict(src_dict)
        region = d.pop("region", UNSET)

        state = d.pop("state", UNSET)

        city = d.pop("city", UNSET)

        distict = d.pop("distict", UNSET)

        town = d.pop("town", UNSET)

        contact_person = d.pop("contact_person", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        first_name_local_script = d.pop("first_name_local_script", UNSET)

        last_name_local_script = d.pop("last_name_local_script", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        full_address = d.pop("full_address", UNSET)

        region_code = d.pop("region_code", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        address_line1 = d.pop("address_line1", UNSET)

        address_line2 = d.pop("address_line2", UNSET)

        address_line3 = d.pop("address_line3", UNSET)

        address_line4 = d.pop("address_line4", UNSET)

        _geolocation = d.pop("geolocation", UNSET)
        geolocation: GetWarehouseListResponseDataWarehouseAddressGeolocation | Unset
        if isinstance(_geolocation, Unset):
            geolocation = UNSET
        else:
            geolocation = GetWarehouseListResponseDataWarehouseAddressGeolocation.from_dict(_geolocation)

        get_warehouse_list_response_data_warehouse_address = cls(
            region=region,
            state=state,
            city=city,
            distict=distict,
            town=town,
            contact_person=contact_person,
            first_name=first_name,
            last_name=last_name,
            first_name_local_script=first_name_local_script,
            last_name_local_script=last_name_local_script,
            postal_code=postal_code,
            full_address=full_address,
            region_code=region_code,
            phone_number=phone_number,
            address_line1=address_line1,
            address_line2=address_line2,
            address_line3=address_line3,
            address_line4=address_line4,
            geolocation=geolocation,
        )

        get_warehouse_list_response_data_warehouse_address.additional_properties = d
        return get_warehouse_list_response_data_warehouse_address

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
