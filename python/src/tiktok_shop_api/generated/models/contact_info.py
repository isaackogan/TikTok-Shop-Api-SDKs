from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactInfo")


@_attrs_define
class ContactInfo:
    """
    Attributes:
        whatsapp (str | Unset): The partner's phone number registered in WhatsApp, in E.164 international format.
            Applicable if the target market is MY, SG, GB, ID, or US.
        email (str | Unset): The partner's email address.
        phone (str | Unset): The partner's phone number in E.164 international format.
        zalo (str | Unset): The partner's phone number registered in Zalo, in E.164 international format. Applicable if
            the target market is VN.
        viber (str | Unset): The partner's phone number registered in Viber, in E.164 international format. Applicable
            if the target market is PH.
        line (str | Unset): The partner's phone number registered in LINE, in E.164 international format. Applicable if
            the target market is TH.
    """

    whatsapp: str | Unset = UNSET
    email: str | Unset = UNSET
    phone: str | Unset = UNSET
    zalo: str | Unset = UNSET
    viber: str | Unset = UNSET
    line: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        whatsapp = self.whatsapp

        email = self.email

        phone = self.phone

        zalo = self.zalo

        viber = self.viber

        line = self.line

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if whatsapp is not UNSET:
            field_dict["whatsapp"] = whatsapp
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if zalo is not UNSET:
            field_dict["zalo"] = zalo
        if viber is not UNSET:
            field_dict["viber"] = viber
        if line is not UNSET:
            field_dict["line"] = line

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        whatsapp = d.pop("whatsapp", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        zalo = d.pop("zalo", UNSET)

        viber = d.pop("viber", UNSET)

        line = d.pop("line", UNSET)

        contact_info = cls(
            whatsapp=whatsapp,
            email=email,
            phone=phone,
            zalo=zalo,
            viber=viber,
            line=line,
        )

        contact_info.additional_properties = d
        return contact_info

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
