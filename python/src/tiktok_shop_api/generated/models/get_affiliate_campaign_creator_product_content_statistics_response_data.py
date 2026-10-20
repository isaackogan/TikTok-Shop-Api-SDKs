from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_affiliate_campaign_creator_product_content_statistics_response_data_creator_content_statistic import GetAffiliateCampaignCreatorProductContentStatisticsResponseDataCreatorContentStatistic





T = TypeVar("T", bound="GetAffiliateCampaignCreatorProductContentStatisticsResponseData")



@_attrs_define
class GetAffiliateCampaignCreatorProductContentStatisticsResponseData:
    """ 
        Attributes:
            creator_content_statistics
                (list[GetAffiliateCampaignCreatorProductContentStatisticsResponseDataCreatorContentStatistic] | Unset): A list
                of objects that represent content statistics for the associated creator.
     """

    creator_content_statistics: list[GetAffiliateCampaignCreatorProductContentStatisticsResponseDataCreatorContentStatistic] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_affiliate_campaign_creator_product_content_statistics_response_data_creator_content_statistic import GetAffiliateCampaignCreatorProductContentStatisticsResponseDataCreatorContentStatistic # noqa: PLC0415
        creator_content_statistics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creator_content_statistics, Unset):
            creator_content_statistics = []
            for creator_content_statistics_item_data in self.creator_content_statistics:
                creator_content_statistics_item = creator_content_statistics_item_data.to_dict()
                creator_content_statistics.append(creator_content_statistics_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creator_content_statistics is not UNSET:
            field_dict["creator_content_statistics"] = creator_content_statistics

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_affiliate_campaign_creator_product_content_statistics_response_data_creator_content_statistic import GetAffiliateCampaignCreatorProductContentStatisticsResponseDataCreatorContentStatistic # noqa: PLC0415
        d = dict(src_dict)
        _creator_content_statistics = d.pop("creator_content_statistics", UNSET)
        creator_content_statistics: list[GetAffiliateCampaignCreatorProductContentStatisticsResponseDataCreatorContentStatistic] | Unset = UNSET
        if _creator_content_statistics is not UNSET:
            creator_content_statistics = []
            for creator_content_statistics_item_data in _creator_content_statistics:
                creator_content_statistics_item = GetAffiliateCampaignCreatorProductContentStatisticsResponseDataCreatorContentStatistic.from_dict(creator_content_statistics_item_data)



                creator_content_statistics.append(creator_content_statistics_item)


        get_affiliate_campaign_creator_product_content_statistics_response_data = cls(
            creator_content_statistics=creator_content_statistics,
        )


        get_affiliate_campaign_creator_product_content_statistics_response_data.additional_properties = d
        return get_affiliate_campaign_creator_product_content_statistics_response_data

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
