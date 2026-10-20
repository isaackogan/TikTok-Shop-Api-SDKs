from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateAffiliatePartnerCampaignRequestContactInfo")



@_attrs_define
class CreateAffiliatePartnerCampaignRequestContactInfo:
    """ 
        Attributes:
            email (str): The partner's email address.
            whatsapp (str | Unset): The partner's phone number registered in WhatsApp, in E.164 international format.
                Required if the target market is MY, SG, GB, or ID; optional if the target market is US; otherwise, not
                applicable.
            phone (str | Unset): The partner's phone number in E.164 international format.
            zalo (str | Unset): The partner's phone number registered in Zalo, in E.164 international format. Required if
                the target market is VN; otherwise, not applicable.
            viber (str | Unset): The partner's phone number registered in Viber, in E.164 international format. Required if
                the target market is PH; otherwise, not applicable.
            line (str | Unset): The partner's phone number registered in LINE, in E.164 international format. Required if
                the target market is TH; otherwise, not applicable.
     """

    email: str
    whatsapp: str | Unset = UNSET
    phone: str | Unset = UNSET
    zalo: str | Unset = UNSET
    viber: str | Unset = UNSET
    line: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        whatsapp = self.whatsapp

        phone = self.phone

        zalo = self.zalo

        viber = self.viber

        line = self.line


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "email": email,
        })
        if whatsapp is not UNSET:
            field_dict["whatsapp"] = whatsapp
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
        email = d.pop("email")

        whatsapp = d.pop("whatsapp", UNSET)

        phone = d.pop("phone", UNSET)

        zalo = d.pop("zalo", UNSET)

        viber = d.pop("viber", UNSET)

        line = d.pop("line", UNSET)

        create_affiliate_partner_campaign_request_contact_info = cls(
            email=email,
            whatsapp=whatsapp,
            phone=phone,
            zalo=zalo,
            viber=viber,
            line=line,
        )


        create_affiliate_partner_campaign_request_contact_info.additional_properties = d
        return create_affiliate_partner_campaign_request_contact_info

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
