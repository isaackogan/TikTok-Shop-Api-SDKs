from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.phone_number_availability import PhoneNumberAvailability
from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneNumber")


@_attrs_define
class PhoneNumber:
    """
    Attributes:
        availability (PhoneNumberAvailability | Unset): Indicates the availability of the phone number.
            Possible values:
            - `AVAILABLE`: The phone number is available and required.
            - `UNAVAILABLE`: No phone number is available.

            Default: AVAILABLE
        country_code (str | Unset): The country code of the phone number, prefixed by a plus `+` symbol. E.g. +353 for
            Ireland.
            Max digits: 4
            Required if `availability=AVAILABLE`.
        local_number (str | Unset): The local number.
            Length: 7 - 20 digits
            Required if `availability=AVAILABLE`.
    """

    availability: PhoneNumberAvailability | Unset = UNSET
    country_code: str | Unset = UNSET
    local_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        availability: str | Unset = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value

        country_code = self.country_code

        local_number = self.local_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability is not UNSET:
            field_dict["availability"] = availability
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if local_number is not UNSET:
            field_dict["local_number"] = local_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _availability = d.pop("availability", UNSET)
        availability: PhoneNumberAvailability | Unset
        if isinstance(_availability, Unset):
            availability = UNSET
        else:
            availability = PhoneNumberAvailability(_availability)

        country_code = d.pop("country_code", UNSET)

        local_number = d.pop("local_number", UNSET)

        phone_number = cls(
            availability=availability,
            country_code=country_code,
            local_number=local_number,
        )

        phone_number.additional_properties = d
        return phone_number

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
