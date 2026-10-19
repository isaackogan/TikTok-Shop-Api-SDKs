from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFBTWarehouseListResponseDataWarehouseAddress")


@_attrs_define
class GetFBTWarehouseListResponseDataWarehouseAddress:
    """
    Attributes:
        postal_code (str | Unset): Warehouse address postal code (also known as zip code).
        region_code (str | Unset): Warehouse country or region code in two-character ISO 3166-1 alpha-2 format.
        state (str | Unset): Warehouse address state or province.
        district (str | Unset): Warehouse address district or county.
        city (str | Unset): Warehouse address city.
        address_line_1 (str | Unset): The detail address line 1.
        address_line_2 (str | Unset): The detail address line 2, additional address information(optional).
        address_line_3 (str | Unset): The detail address line 3, additional address information(optional).
    """

    postal_code: str | Unset = UNSET
    region_code: str | Unset = UNSET
    state: str | Unset = UNSET
    district: str | Unset = UNSET
    city: str | Unset = UNSET
    address_line_1: str | Unset = UNSET
    address_line_2: str | Unset = UNSET
    address_line_3: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        postal_code = self.postal_code

        region_code = self.region_code

        state = self.state

        district = self.district

        city = self.city

        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        address_line_3 = self.address_line_3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if region_code is not UNSET:
            field_dict["region_code"] = region_code
        if state is not UNSET:
            field_dict["state"] = state
        if district is not UNSET:
            field_dict["district"] = district
        if city is not UNSET:
            field_dict["city"] = city
        if address_line_1 is not UNSET:
            field_dict["address_line_1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["address_line_2"] = address_line_2
        if address_line_3 is not UNSET:
            field_dict["address_line_3"] = address_line_3

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        postal_code = d.pop("postal_code", UNSET)

        region_code = d.pop("region_code", UNSET)

        state = d.pop("state", UNSET)

        district = d.pop("district", UNSET)

        city = d.pop("city", UNSET)

        address_line_1 = d.pop("address_line_1", UNSET)

        address_line_2 = d.pop("address_line_2", UNSET)

        address_line_3 = d.pop("address_line_3", UNSET)

        get_fbt_warehouse_list_response_data_warehouse_address = cls(
            postal_code=postal_code,
            region_code=region_code,
            state=state,
            district=district,
            city=city,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            address_line_3=address_line_3,
        )

        get_fbt_warehouse_list_response_data_warehouse_address.additional_properties = d
        return get_fbt_warehouse_list_response_data_warehouse_address

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
