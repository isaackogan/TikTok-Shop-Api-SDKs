from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWarehouseListResponseDataWarehouseAddressGeolocation")


@_attrs_define
class GetWarehouseListResponseDataWarehouseAddressGeolocation:
    """
    Attributes:
        latitude (str | Unset): The latitude of the address.
        longitude (str | Unset): The longitude of the address.
    """

    latitude: str | Unset = UNSET
    longitude: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        get_warehouse_list_response_data_warehouse_address_geolocation = cls(
            latitude=latitude,
            longitude=longitude,
        )

        get_warehouse_list_response_data_warehouse_address_geolocation.additional_properties = d
        return get_warehouse_list_response_data_warehouse_address_geolocation

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
