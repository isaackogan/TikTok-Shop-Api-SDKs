from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail import GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetail





T = TypeVar("T", bound="GetCampaignProductPerformanceListResponseDataCampaignProductStatistic")



@_attrs_define
class GetCampaignProductPerformanceListResponseDataCampaignProductStatistic:
    """ 
        Attributes:
            data_update_time (str | Unset): The time at which the product data was last updated, in Unix epoch format.
            creator_sales_num (int | Unset): The number of creators credited with at least one product sale.
            collaborated_creators_num (int | Unset): The total number of creators associated with the campaign.
            promoted_creator_num (int | Unset): The number of the creators involved in the campaign.
            sample_requested_creator_num (int | Unset): The total number of samples requested by all creators associated
                with the campaign.
            campaign_product_detail
                (GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetail | Unset):
     """

    data_update_time: str | Unset = UNSET
    creator_sales_num: int | Unset = UNSET
    collaborated_creators_num: int | Unset = UNSET
    promoted_creator_num: int | Unset = UNSET
    sample_requested_creator_num: int | Unset = UNSET
    campaign_product_detail: GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetail | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail import GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetail # noqa: PLC0415
        data_update_time = self.data_update_time

        creator_sales_num = self.creator_sales_num

        collaborated_creators_num = self.collaborated_creators_num

        promoted_creator_num = self.promoted_creator_num

        sample_requested_creator_num = self.sample_requested_creator_num

        campaign_product_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign_product_detail, Unset):
            campaign_product_detail = self.campaign_product_detail.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_update_time is not UNSET:
            field_dict["data_update_time"] = data_update_time
        if creator_sales_num is not UNSET:
            field_dict["creator_sales_num"] = creator_sales_num
        if collaborated_creators_num is not UNSET:
            field_dict["collaborated_creators_num"] = collaborated_creators_num
        if promoted_creator_num is not UNSET:
            field_dict["promoted_creator_num"] = promoted_creator_num
        if sample_requested_creator_num is not UNSET:
            field_dict["sample_requested_creator_num"] = sample_requested_creator_num
        if campaign_product_detail is not UNSET:
            field_dict["campaign_product_detail"] = campaign_product_detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail import GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetail # noqa: PLC0415
        d = dict(src_dict)
        data_update_time = d.pop("data_update_time", UNSET)

        creator_sales_num = d.pop("creator_sales_num", UNSET)

        collaborated_creators_num = d.pop("collaborated_creators_num", UNSET)

        promoted_creator_num = d.pop("promoted_creator_num", UNSET)

        sample_requested_creator_num = d.pop("sample_requested_creator_num", UNSET)

        _campaign_product_detail = d.pop("campaign_product_detail", UNSET)
        campaign_product_detail: GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetail | Unset
        if isinstance(_campaign_product_detail,  Unset):
            campaign_product_detail = UNSET
        else:
            campaign_product_detail = GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetail.from_dict(_campaign_product_detail)




        get_campaign_product_performance_list_response_data_campaign_product_statistic = cls(
            data_update_time=data_update_time,
            creator_sales_num=creator_sales_num,
            collaborated_creators_num=collaborated_creators_num,
            promoted_creator_num=promoted_creator_num,
            sample_requested_creator_num=sample_requested_creator_num,
            campaign_product_detail=campaign_product_detail,
        )


        get_campaign_product_performance_list_response_data_campaign_product_statistic.additional_properties = d
        return get_campaign_product_performance_list_response_data_campaign_product_statistic

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
