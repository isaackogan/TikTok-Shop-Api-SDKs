from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_manufacturer_request_locale import CreateManufacturerRequestLocale
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.phone_number import PhoneNumber





T = TypeVar("T", bound="CreateManufacturerRequest")



@_attrs_define
class CreateManufacturerRequest:
    """ 
        Attributes:
            name (str): The manufacturer name. Chinese characters are not supported.
                Max length: 255 characters
            email (str): The manufacturer's email address. Use a valid email format such as `name@example.com`. Chinese
                characters are not supported.
            phone_number (PhoneNumber):
            address (str): The postal address of the manufacturer. Chinese characters are not supported.
                Max length: 500 characters
            registered_trade_name (str | Unset): The registered trade name of the manufacturer. Chinese characters are not
                supported.
                Max length: 200 characters
            locale (CreateManufacturerRequestLocale | Unset): The BCP-47 locale code representing the language used for
                specifying the manufacturer information.
                Possible values:
                - de-DE
                - en-IE
                - es-ES
                - fr-FR
                - it-IT
                Default: The locale of the seller's registered business address.

                **Note**: The information provided will be automatically translated into all EU languages supported by TikTok
                Shop. Ensure the locale matches the language used in field values to avoid inaccurate translations.
     """

    name: str
    email: str
    phone_number: PhoneNumber
    address: str
    registered_trade_name: str | Unset = UNSET
    locale: CreateManufacturerRequestLocale | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.phone_number import PhoneNumber # noqa: PLC0415
        name = self.name

        email = self.email

        phone_number = self.phone_number.to_dict()

        address = self.address

        registered_trade_name = self.registered_trade_name

        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
        })
        if registered_trade_name is not UNSET:
            field_dict["registered_trade_name"] = registered_trade_name
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phone_number import PhoneNumber # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        email = d.pop("email")

        phone_number = PhoneNumber.from_dict(d.pop("phone_number"))




        address = d.pop("address")

        registered_trade_name = d.pop("registered_trade_name", UNSET)

        _locale = d.pop("locale", UNSET)
        locale: CreateManufacturerRequestLocale | Unset
        if isinstance(_locale,  Unset):
            locale = UNSET
        else:
            locale = CreateManufacturerRequestLocale(_locale)




        create_manufacturer_request = cls(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            registered_trade_name=registered_trade_name,
            locale=locale,
        )


        create_manufacturer_request.additional_properties = d
        return create_manufacturer_request

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
