from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SearchSellerPartnerCampaignsResponseDataCampaignJoinStatusCount")



@_attrs_define
class SearchSellerPartnerCampaignsResponseDataCampaignJoinStatusCount:
    """ 
        Attributes:
            category (str): UNSPECIFIED is an unspecified category; JOINED is Manage; NOT_JOINED is Discover; CLOSED is
                Closed.
            count (int): Number of campaigns in this join-status category.
     """

    category: str
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        category = self.category

        count = self.count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "category": category,
            "count": count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        count = d.pop("count")

        search_seller_partner_campaigns_response_data_campaign_join_status_count = cls(
            category=category,
            count=count,
        )


        search_seller_partner_campaigns_response_data_campaign_join_status_count.additional_properties = d
        return search_seller_partner_campaigns_response_data_campaign_join_status_count

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
