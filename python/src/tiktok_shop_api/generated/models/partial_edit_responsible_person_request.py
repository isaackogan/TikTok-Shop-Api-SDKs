from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.partial_edit_responsible_person_request_locale import PartialEditResponsiblePersonRequestLocale
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.address import Address
  from ..models.create_responsible_person_request_phone_number import CreateResponsiblePersonRequestPhoneNumber





T = TypeVar("T", bound="PartialEditResponsiblePersonRequest")



@_attrs_define
class PartialEditResponsiblePersonRequest:
    """ 
        Attributes:
            name (str | Unset): The responsible person name to update. Chinese characters are not supported when this field
                is provided.
                Max length: 200 characters
            email (str | Unset): The email address of the responsible person to update. Chinese characters are not supported
                when this field is provided.
            phone_number (CreateResponsiblePersonRequestPhoneNumber | Unset):
            address (Address | Unset):
            locale (PartialEditResponsiblePersonRequestLocale | Unset): The BCP-47 locale code representing the language of
                the responsible person information to update.
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
    email: str | Unset = UNSET
    phone_number: CreateResponsiblePersonRequestPhoneNumber | Unset = UNSET
    address: Address | Unset = UNSET
    locale: PartialEditResponsiblePersonRequestLocale | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.address import Address # noqa: PLC0415
        from ..models.create_responsible_person_request_phone_number import CreateResponsiblePersonRequestPhoneNumber # noqa: PLC0415
        name = self.name

        email = self.email

        phone_number: dict[str, Any] | Unset = UNSET
        if not isinstance(self.phone_number, Unset):
            phone_number = self.phone_number.to_dict()

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.address import Address # noqa: PLC0415
        from ..models.create_responsible_person_request_phone_number import CreateResponsiblePersonRequestPhoneNumber # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        _phone_number = d.pop("phone_number", UNSET)
        phone_number: CreateResponsiblePersonRequestPhoneNumber | Unset
        if isinstance(_phone_number,  Unset):
            phone_number = UNSET
        else:
            phone_number = CreateResponsiblePersonRequestPhoneNumber.from_dict(_phone_number)




        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)




        _locale = d.pop("locale", UNSET)
        locale: PartialEditResponsiblePersonRequestLocale | Unset
        if isinstance(_locale,  Unset):
            locale = UNSET
        else:
            locale = PartialEditResponsiblePersonRequestLocale(_locale)




        partial_edit_responsible_person_request = cls(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            locale=locale,
        )


        partial_edit_responsible_person_request.additional_properties = d
        return partial_edit_responsible_person_request

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
