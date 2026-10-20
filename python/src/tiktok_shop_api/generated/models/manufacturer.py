from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Manufacturer")


@_attrs_define
class Manufacturer:
    """
    Attributes:
        name (str | Unset): The name of the manufacturer.
        address (str | Unset): The address of the manufacturer.
        phone_number (str | Unset): The phone number of the manufacturer, prefixed by a plus `+` symbol.
            There must be a space or hyphen between the country code and the local phone number.
        email (str | Unset): The email address of the manufacturer.
    """

    name: str | Unset = UNSET
    address: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        address = self.address

        phone_number = self.phone_number

        email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        address = d.pop("address", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        email = d.pop("email", UNSET)

        manufacturer = cls(
            name=name,
            address=address,
            phone_number=phone_number,
            email=email,
        )

        manufacturer.additional_properties = d
        return manufacturer

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
