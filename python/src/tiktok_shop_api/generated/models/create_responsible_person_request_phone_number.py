from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CreateResponsiblePersonRequestPhoneNumber")



@_attrs_define
class CreateResponsiblePersonRequestPhoneNumber:
    """ 
        Attributes:
            country_code (str): The country code of the phone number, prefixed by a plus `+` symbol. E.g. +353 for Ireland.
                Only EU country codes are allowed.
                Max digits: 4
            local_number (str): The local number.
                Length: 7 - 11 digits
     """

    country_code: str
    local_number: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        local_number = self.local_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "country_code": country_code,
            "local_number": local_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("country_code")

        local_number = d.pop("local_number")

        create_responsible_person_request_phone_number = cls(
            country_code=country_code,
            local_number=local_number,
        )


        create_responsible_person_request_phone_number.additional_properties = d
        return create_responsible_person_request_phone_number

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
