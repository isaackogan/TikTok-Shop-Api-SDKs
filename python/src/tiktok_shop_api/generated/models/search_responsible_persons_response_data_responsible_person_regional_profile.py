from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_responsible_persons_response_data_responsible_person_regional_profile_locale import (
    SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileLocale,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_responsible_persons_response_data_responsible_person_regional_profile_address import (
        SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileAddress,
    )
    from ..models.search_responsible_persons_response_data_responsible_person_regional_profile_phone_number import (
        SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfilePhoneNumber,
    )


T = TypeVar("T", bound="SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfile")


@_attrs_define
class SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfile:
    """
    Attributes:
        locale (SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileLocale | Unset): The BCP-47 locale
            code representing the language used for specifying the responsible person information.
            Possible values:
            - de-DE
            - en-IE
            - es-ES
            - fr-FR
            - it-IT
        name (str | Unset): The responsible person name.
            Max length: 200 characters
        email (str | Unset): The email address of the responsible person.
        phone_number (SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfilePhoneNumber | Unset):
        address (SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileAddress | Unset):
    """

    locale: SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileLocale | Unset = UNSET
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    phone_number: SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfilePhoneNumber | Unset = UNSET
    address: SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileAddress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale: str | Unset = UNSET
        if not isinstance(self.locale, Unset):
            locale = self.locale.value

        name = self.name

        email = self.email

        phone_number: dict[str, Any] | Unset = UNSET
        if not isinstance(self.phone_number, Unset):
            phone_number = self.phone_number.to_dict()

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locale is not UNSET:
            field_dict["locale"] = locale
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_responsible_persons_response_data_responsible_person_regional_profile_address import (
            SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileAddress,  # noqa: PLC0415
        )
        from ..models.search_responsible_persons_response_data_responsible_person_regional_profile_phone_number import (
            SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfilePhoneNumber,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _locale = d.pop("locale", UNSET)
        locale: SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileLocale | Unset
        if isinstance(_locale, Unset):
            locale = UNSET
        else:
            locale = SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileLocale(_locale)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        _phone_number = d.pop("phone_number", UNSET)
        phone_number: SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfilePhoneNumber | Unset
        if isinstance(_phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfilePhoneNumber.from_dict(
                _phone_number
            )

        _address = d.pop("address", UNSET)
        address: SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileAddress | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfileAddress.from_dict(_address)

        search_responsible_persons_response_data_responsible_person_regional_profile = cls(
            locale=locale,
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
        )

        search_responsible_persons_response_data_responsible_person_regional_profile.additional_properties = d
        return search_responsible_persons_response_data_responsible_person_regional_profile

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
