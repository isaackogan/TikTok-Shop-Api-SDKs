from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GenerateAffiliatePartnerCampaignProductLinkResponseData")



@_attrs_define
class GenerateAffiliatePartnerCampaignProductLinkResponseData:
    """ 
        Attributes:
            product_promotion_link (str | Unset): A URL for product promotion content. This URL is provided to agencies for
                sharing with colloborating creators. Creators share this link with followers via the TikTok App. Note that
                creators control whether or not to add products to their showcase in the pop-up window.
     """

    product_promotion_link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_promotion_link = self.product_promotion_link


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_promotion_link is not UNSET:
            field_dict["product_promotion_link"] = product_promotion_link

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_promotion_link = d.pop("product_promotion_link", UNSET)

        generate_affiliate_partner_campaign_product_link_response_data = cls(
            product_promotion_link=product_promotion_link,
        )


        generate_affiliate_partner_campaign_product_link_response_data.additional_properties = d
        return generate_affiliate_partner_campaign_product_link_response_data

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
