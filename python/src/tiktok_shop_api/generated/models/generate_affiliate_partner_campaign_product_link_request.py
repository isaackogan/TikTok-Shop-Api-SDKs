from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GenerateAffiliatePartnerCampaignProductLinkRequest")


@_attrs_define
class GenerateAffiliatePartnerCampaignProductLinkRequest:
    """
    Attributes:
        creator_commission_rate (int): The commission rate paid to a creator, in hundredths of a percent (0.01%). The
            value must be at least 100 (1%) and no greater than the total commission rate set by the seller.
    """

    creator_commission_rate: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator_commission_rate = self.creator_commission_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creator_commission_rate": creator_commission_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_commission_rate = d.pop("creator_commission_rate")

        generate_affiliate_partner_campaign_product_link_request = cls(
            creator_commission_rate=creator_commission_rate,
        )

        generate_affiliate_partner_campaign_product_link_request.additional_properties = d
        return generate_affiliate_partner_campaign_product_link_request

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
