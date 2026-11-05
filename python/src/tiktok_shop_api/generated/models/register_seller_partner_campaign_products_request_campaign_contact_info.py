from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RegisterSellerPartnerCampaignProductsRequestCampaignContactInfo")



@_attrs_define
class RegisterSellerPartnerCampaignProductsRequestCampaignContactInfo:
    """ 
        Attributes:
            type_ (str): Contact method. At least one EMAIL entry is required; WHATSAPP is optional.
            value (str): Plain email address for type EMAIL, without display names or Markdown. For type WHATSAPP, use 1-30
                digits, optionally preceded by a plus sign. This sensitive value is not returned in error messages.
            region_code (str | Unset): Supported country and calling-code pair from the registration country selector, for
                example US#1 or TH#66. Required for WhatsApp; optional and ignored for email. The pair is validated; phone
                ownership and WhatsApp account availability are not verified.
     """

    type_: str
    value: str
    region_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value = self.value

        region_code = self.region_code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "value": value,
        })
        if region_code is not UNSET:
            field_dict["region_code"] = region_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        value = d.pop("value")

        region_code = d.pop("region_code", UNSET)

        register_seller_partner_campaign_products_request_campaign_contact_info = cls(
            type_=type_,
            value=value,
            region_code=region_code,
        )


        register_seller_partner_campaign_products_request_campaign_contact_info.additional_properties = d
        return register_seller_partner_campaign_products_request_campaign_contact_info

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
