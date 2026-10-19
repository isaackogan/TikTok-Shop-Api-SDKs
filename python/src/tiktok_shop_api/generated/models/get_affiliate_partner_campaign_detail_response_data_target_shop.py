from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAffiliatePartnerCampaignDetailResponseDataTargetShop")


@_attrs_define
class GetAffiliatePartnerCampaignDetailResponseDataTargetShop:
    """
    Attributes:
        code (str | Unset): The seller shop code in available in TikTok Shop Seller Central by clicking on the Seller
            Profile icon in the top right of the user interface.
        name (str | Unset): The TikTok Shop name.
    """

    code: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        get_affiliate_partner_campaign_detail_response_data_target_shop = cls(
            code=code,
            name=name,
        )

        get_affiliate_partner_campaign_detail_response_data_target_shop.additional_properties = d
        return get_affiliate_partner_campaign_detail_response_data_target_shop

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
