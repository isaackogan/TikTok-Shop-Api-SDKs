from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.partial_edit_manufacturer_request_locale import PartialEditManufacturerRequestLocale
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.phone_number import PhoneNumber


T = TypeVar("T", bound="PartialEditManufacturerRequest")


@_attrs_define
class PartialEditManufacturerRequest:
    """
    Attributes:
        name (str | Unset): The manufacturer name.
            Max length: 255 characters
        registered_trade_name (str | Unset): The registered trade name of the manufacturer.
            Max length: 200 characters
        email (str | Unset): The manufacturer's email address. Use a valid email format such as `name@example.com`.
        phone_number (PhoneNumber | Unset):
        address (str | Unset): The postal address of the manufacturer.
            Max length: 500 characters
        locale (PartialEditManufacturerRequestLocale | Unset): The BCP-47 locale code representing the language of the
            manufacturer information to update.
            Possible values:
            - de-DE
            - en-IE
            - es-ES
            - fr-FR
            - it-IT
            Default: The locale of the seller's registered business address.

            **Note**: Only the language version selected by this locale is updated; other language versions remain
            unchanged. Ensure the locale matches the language used in the supplied field values.
    """

    name: str | Unset = UNSET
    registered_trade_name: str | Unset = UNSET
    email: str | Unset = UNSET
    phone_number: PhoneNumber | Unset = UNSET
    address: str | Unset = UNSET
    locale: PartialEditManufacturerRequestLocale | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        registered_trade_name = self.registered_trade_name

        email = self.email

        phone_number: dict[str, Any] | Unset = UNSET
        if not isinstance(self.phone_number, Unset):
            phone_number = self.phone_number.to_dict()

        address = self.address

        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phone_number import PhoneNumber  # noqa: PLC0415

        d = dict(src_dict)
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

        _locale = d.pop("locale", UNSET)
        locale: PartialEditManufacturerRequestLocale | Unset
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = PartialEditManufacturerRequestLocale(_locale)

        partial_edit_manufacturer_request = cls(
            name=name,
            registered_trade_name=registered_trade_name,
            email=email,
            phone_number=phone_number,
            address=address,
            locale=locale,
        )

        partial_edit_manufacturer_request.additional_properties = d
        return partial_edit_manufacturer_request

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
