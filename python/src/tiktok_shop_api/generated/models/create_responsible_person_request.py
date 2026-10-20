from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_responsible_person_request_locale import CreateResponsiblePersonRequestLocale
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.address import Address
  from ..models.create_responsible_person_request_phone_number import CreateResponsiblePersonRequestPhoneNumber





T = TypeVar("T", bound="CreateResponsiblePersonRequest")



@_attrs_define
class CreateResponsiblePersonRequest:
    """ 
        Attributes:
            name (str): The responsible person name. Chinese characters are not supported.
                Max length: 200 characters
            email (str): The email address of the responsible person. Chinese characters are not supported.
            phone_number (CreateResponsiblePersonRequestPhoneNumber):
            address (Address):
            locale (CreateResponsiblePersonRequestLocale | Unset): The BCP-47 locale code representing the language used for
                specifying the responsible person information.
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
    phone_number: CreateResponsiblePersonRequestPhoneNumber
    address: Address
    locale: CreateResponsiblePersonRequestLocale | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.address import Address # noqa: PLC0415
        from ..models.create_responsible_person_request_phone_number import CreateResponsiblePersonRequestPhoneNumber # noqa: PLC0415
        name = self.name

        email = self.email

        phone_number = self.phone_number.to_dict()

        address = self.address.to_dict()

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
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address # noqa: PLC0415
        from ..models.create_responsible_person_request_phone_number import CreateResponsiblePersonRequestPhoneNumber # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        email = d.pop("email")

        phone_number = CreateResponsiblePersonRequestPhoneNumber.from_dict(d.pop("phone_number"))




        address = Address.from_dict(d.pop("address"))




        _locale = d.pop("locale", UNSET)
        locale: CreateResponsiblePersonRequestLocale | Unset
        if isinstance(_locale,  Unset):
            locale = UNSET
        else:
            locale = CreateResponsiblePersonRequestLocale(_locale)




        create_responsible_person_request = cls(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            locale=locale,
        )


        create_responsible_person_request.additional_properties = d
        return create_responsible_person_request

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
