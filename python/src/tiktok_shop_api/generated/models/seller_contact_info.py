from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SellerContactInfo")



@_attrs_define
class SellerContactInfo:
    """ 
        Attributes:
            email (str | Unset): The seller's email address.
            phone_number (str | Unset): The phone number of the seller.
            whatsapp (str | Unset): The phone number used by the seller to register for WhatsApp.
            telegram (str | Unset): The  seller's Telegram username or phone number.
            line (str | Unset): The phone number used by the seller to register for the Line app.
     """

    email: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    whatsapp: str | Unset = UNSET
    telegram: str | Unset = UNSET
    line: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        phone_number = self.phone_number

        whatsapp = self.whatsapp

        telegram = self.telegram

        line = self.line


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if email is not UNSET:
            field_dict["email"] = email
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if whatsapp is not UNSET:
            field_dict["whatsapp"] = whatsapp
        if telegram is not UNSET:
            field_dict["telegram"] = telegram
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        whatsapp = d.pop("whatsapp", UNSET)

        telegram = d.pop("telegram", UNSET)

        line = d.pop("line", UNSET)

        seller_contact_info = cls(
            email=email,
            phone_number=phone_number,
            whatsapp=whatsapp,
            telegram=telegram,
            line=line,
        )


        seller_contact_info.additional_properties = d
        return seller_contact_info

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
