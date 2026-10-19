from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileAddress")


@_attrs_define
class SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileAddress:
    """
    Attributes:
        street_address_line1 (str | Unset): The detailed street address of the location, including the building number,
            street name, district, city, province, and any relevant details.
            Max length: 500 characters
        street_address_line2 (str | Unset): (**Deprecated**: This field is deprecated and will return an empty string.
            Please refer to `street_address_line1` instead for the relevant details.)

            An optional secondary line for additional address details, if necessary.
            Max length: 500 characters
        district (str | Unset): (**Deprecated**: This field is deprecated and will return an empty string. Please refer
            to `street_address_line1` instead for the district name.)

            The district name.
            Max length: 500 characters
        city (str | Unset): **Deprecated**: This field returns an empty string. Use `street_address_line1` for the city
            name.
        postal_code (str | Unset): The postal code.
            Max length: 500 characters
        province (str | Unset): **Deprecated**: This field returns an empty string. Use `street_address_line1` for the
            province, state, or region name.
        country (str | Unset): The two letter ISO 3166 country code representing the country of the address. It must be
            an EU country.
    """

    street_address_line1: str | Unset = UNSET
    street_address_line2: str | Unset = UNSET
    district: str | Unset = UNSET
    city: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    province: str | Unset = UNSET
    country: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        street_address_line1 = self.street_address_line1

        street_address_line2 = self.street_address_line2

        district = self.district

        city = self.city

        postal_code = self.postal_code

        province = self.province

        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street_address_line1 is not UNSET:
            field_dict["street_address_line1"] = street_address_line1
        if street_address_line2 is not UNSET:
            field_dict["street_address_line2"] = street_address_line2
        if district is not UNSET:
            field_dict["district"] = district
        if city is not UNSET:
            field_dict["city"] = city
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if province is not UNSET:
            field_dict["province"] = province
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        street_address_line1 = d.pop("street_address_line1", UNSET)

        street_address_line2 = d.pop("street_address_line2", UNSET)

        district = d.pop("district", UNSET)

        city = d.pop("city", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        province = d.pop("province", UNSET)

        country = d.pop("country", UNSET)

        search_responsible_persons_response_data_responsible_person_regional_profile_address = cls(
            street_address_line1=street_address_line1,
            street_address_line2=street_address_line2,
            district=district,
            city=city,
            postal_code=postal_code,
            province=province,
            country=country,
        )

        search_responsible_persons_response_data_responsible_person_regional_profile_address.additional_properties = d
        return search_responsible_persons_response_data_responsible_person_regional_profile_address

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
