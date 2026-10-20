from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.phone_number import PhoneNumber


T = TypeVar("T", bound="SearchManufacturersResponseDataManufacturerRegionalProfile")


@_attrs_define
class SearchManufacturersResponseDataManufacturerRegionalProfile:
    """
    Attributes:
        locale (str | Unset): The BCP-47 locale code representing the language used for specifying the manufacturer
            information.
            Possible values:
            - de-DE
            - en-IE
            - es-ES
            - fr-FR
            - it-IT
        name (str | Unset): The manufacturer name.
            Max length: 255 characters
        registered_trade_name (str | Unset): The registered trade name of the manufacturer.
            Max length: 200 characters
        email (str | Unset): The email address of the manufacturer.
        phone_number (PhoneNumber | Unset):
        address (str | Unset): The postal address of the manufacturer.
            Max length: 500 characters
    """

    locale: str | Unset = UNSET
    name: str | Unset = UNSET
    registered_trade_name: str | Unset = UNSET
    email: str | Unset = UNSET
    phone_number: PhoneNumber | Unset = UNSET
    address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        name = self.name

        registered_trade_name = self.registered_trade_name

        email = self.email

        phone_number: dict[str, Any] | Unset = UNSET
        if not isinstance(self.phone_number, Unset):
            phone_number = self.phone_number.to_dict()

        address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if name is not UNSET:
            field_dict["name"] = name
        if registered_trade_name is not UNSET:
            field_dict["registered_trade_name"] = registered_trade_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phone_number import PhoneNumber  # noqa: PLC0415

        d = dict(src_dict)
        locale = d.pop("locale", UNSET)

        name = d.pop("name", UNSET)

        registered_trade_name = d.pop("registered_trade_name", UNSET)

        email = d.pop("email", UNSET)

        _phone_number = d.pop("phone_number", UNSET)
        phone_number: PhoneNumber | Unset
        if isinstance(_phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = PhoneNumber.from_dict(_phone_number)

        address = d.pop("address", UNSET)

        search_manufacturers_response_data_manufacturer_regional_profile = cls(
            locale=locale,
            name=name,
            registered_trade_name=registered_trade_name,
            email=email,
            phone_number=phone_number,
            address=address,
        )

        search_manufacturers_response_data_manufacturer_regional_profile.additional_properties = d
        return search_manufacturers_response_data_manufacturer_regional_profile

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
