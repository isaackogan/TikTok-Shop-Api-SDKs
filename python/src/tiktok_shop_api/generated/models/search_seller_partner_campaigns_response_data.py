from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_seller_partner_campaigns_response_data_campaign_detail import SearchSellerPartnerCampaignsResponseDataCampaignDetail
  from ..models.search_seller_partner_campaigns_response_data_campaign_join_status_count import SearchSellerPartnerCampaignsResponseDataCampaignJoinStatusCount





T = TypeVar("T", bound="SearchSellerPartnerCampaignsResponseData")



@_attrs_define
class SearchSellerPartnerCampaignsResponseData:
    """ 
        Attributes:
            next_page_token (str): Pass this token unchanged to retrieve the next page. Empty when no further page is
                available within the supported query window.
            campaign_details (list[SearchSellerPartnerCampaignsResponseDataCampaignDetail] | Unset): Complete shared schema;
                actual fields depend on campaign type and list branch.
            campaign_join_status_counts (list[SearchSellerPartnerCampaignsResponseDataCampaignJoinStatusCount] | Unset):
                Counts for available join-status categories. Array order has no business meaning; identify each count by
                category.
            total_num (int | Unset): Total matching campaigns, not the number of records in this page.
     """

    next_page_token: str
    campaign_details: list[SearchSellerPartnerCampaignsResponseDataCampaignDetail] | Unset = UNSET
    campaign_join_status_counts: list[SearchSellerPartnerCampaignsResponseDataCampaignJoinStatusCount] | Unset = UNSET
    total_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_seller_partner_campaigns_response_data_campaign_detail import SearchSellerPartnerCampaignsResponseDataCampaignDetail # noqa: PLC0415
        from ..models.search_seller_partner_campaigns_response_data_campaign_join_status_count import SearchSellerPartnerCampaignsResponseDataCampaignJoinStatusCount # noqa: PLC0415
        next_page_token = self.next_page_token

        campaign_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campaign_details, Unset):
            campaign_details = []
            for campaign_details_item_data in self.campaign_details:
                campaign_details_item = campaign_details_item_data.to_dict()
                campaign_details.append(campaign_details_item)



        campaign_join_status_counts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campaign_join_status_counts, Unset):
            campaign_join_status_counts = []
            for campaign_join_status_counts_item_data in self.campaign_join_status_counts:
                campaign_join_status_counts_item = campaign_join_status_counts_item_data.to_dict()
                campaign_join_status_counts.append(campaign_join_status_counts_item)



        total_num = self.total_num


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "next_page_token": next_page_token,
        })
        if campaign_details is not UNSET:
            field_dict["campaign_details"] = campaign_details
        if campaign_join_status_counts is not UNSET:
            field_dict["campaign_join_status_counts"] = campaign_join_status_counts
        if total_num is not UNSET:
            field_dict["total_num"] = total_num

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_seller_partner_campaigns_response_data_campaign_detail import SearchSellerPartnerCampaignsResponseDataCampaignDetail # noqa: PLC0415
        from ..models.search_seller_partner_campaigns_response_data_campaign_join_status_count import SearchSellerPartnerCampaignsResponseDataCampaignJoinStatusCount # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token")

        _campaign_details = d.pop("campaign_details", UNSET)
        campaign_details: list[SearchSellerPartnerCampaignsResponseDataCampaignDetail] | Unset = UNSET
        if _campaign_details is not UNSET:
            campaign_details = []
            for campaign_details_item_data in _campaign_details:
                campaign_details_item = SearchSellerPartnerCampaignsResponseDataCampaignDetail.from_dict(campaign_details_item_data)



                campaign_details.append(campaign_details_item)


        _campaign_join_status_counts = d.pop("campaign_join_status_counts", UNSET)
        campaign_join_status_counts: list[SearchSellerPartnerCampaignsResponseDataCampaignJoinStatusCount] | Unset = UNSET
        if _campaign_join_status_counts is not UNSET:
            campaign_join_status_counts = []
            for campaign_join_status_counts_item_data in _campaign_join_status_counts:
                campaign_join_status_counts_item = SearchSellerPartnerCampaignsResponseDataCampaignJoinStatusCount.from_dict(campaign_join_status_counts_item_data)



                campaign_join_status_counts.append(campaign_join_status_counts_item)


        total_num = d.pop("total_num", UNSET)

        search_seller_partner_campaigns_response_data = cls(
            next_page_token=next_page_token,
            campaign_details=campaign_details,
            campaign_join_status_counts=campaign_join_status_counts,
            total_num=total_num,
        )


        search_seller_partner_campaigns_response_data.additional_properties = d
        return search_seller_partner_campaigns_response_data

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
