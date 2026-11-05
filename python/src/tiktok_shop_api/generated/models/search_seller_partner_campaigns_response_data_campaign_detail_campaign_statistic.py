from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchSellerPartnerCampaignsResponseDataCampaignDetailCampaignStatistic")



@_attrs_define
class SearchSellerPartnerCampaignsResponseDataCampaignDetailCampaignStatistic:
    """ 
        Attributes:
            applied_products_num (int | Unset): Number of products submitted to the campaign.
            closed_products_num (int | Unset): Number of product registrations in the closed state.
            declined_agency_num (int | Unset): Number of agencies that have declined participation in the campaign.
            joined_agency_num (int | Unset): Number of agencies that have joined the campaign.
            ongoing_products_num (int | Unset): Number of products currently participating in the campaign.
            pending_products_num (int | Unset): Number of submitted products awaiting review.
            rejected_products_num (int | Unset): Number of products rejected from the campaign.
     """

    applied_products_num: int | Unset = UNSET
    closed_products_num: int | Unset = UNSET
    declined_agency_num: int | Unset = UNSET
    joined_agency_num: int | Unset = UNSET
    ongoing_products_num: int | Unset = UNSET
    pending_products_num: int | Unset = UNSET
    rejected_products_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        applied_products_num = self.applied_products_num

        closed_products_num = self.closed_products_num

        declined_agency_num = self.declined_agency_num

        joined_agency_num = self.joined_agency_num

        ongoing_products_num = self.ongoing_products_num

        pending_products_num = self.pending_products_num

        rejected_products_num = self.rejected_products_num


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if applied_products_num is not UNSET:
            field_dict["applied_products_num"] = applied_products_num
        if closed_products_num is not UNSET:
            field_dict["closed_products_num"] = closed_products_num
        if declined_agency_num is not UNSET:
            field_dict["declined_agency_num"] = declined_agency_num
        if joined_agency_num is not UNSET:
            field_dict["joined_agency_num"] = joined_agency_num
        if ongoing_products_num is not UNSET:
            field_dict["ongoing_products_num"] = ongoing_products_num
        if pending_products_num is not UNSET:
            field_dict["pending_products_num"] = pending_products_num
        if rejected_products_num is not UNSET:
            field_dict["rejected_products_num"] = rejected_products_num

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        applied_products_num = d.pop("applied_products_num", UNSET)

        closed_products_num = d.pop("closed_products_num", UNSET)

        declined_agency_num = d.pop("declined_agency_num", UNSET)

        joined_agency_num = d.pop("joined_agency_num", UNSET)

        ongoing_products_num = d.pop("ongoing_products_num", UNSET)

        pending_products_num = d.pop("pending_products_num", UNSET)

        rejected_products_num = d.pop("rejected_products_num", UNSET)

        search_seller_partner_campaigns_response_data_campaign_detail_campaign_statistic = cls(
            applied_products_num=applied_products_num,
            closed_products_num=closed_products_num,
            declined_agency_num=declined_agency_num,
            joined_agency_num=joined_agency_num,
            ongoing_products_num=ongoing_products_num,
            pending_products_num=pending_products_num,
            rejected_products_num=rejected_products_num,
        )


        search_seller_partner_campaigns_response_data_campaign_detail_campaign_statistic.additional_properties = d
        return search_seller_partner_campaigns_response_data_campaign_detail_campaign_statistic

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
