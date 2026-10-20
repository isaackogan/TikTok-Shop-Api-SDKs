from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile_gmv import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfileGmv





T = TypeVar("T", bound="GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfile")



@_attrs_define
class GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfile:
    """ 
        Attributes:
            start_timestamp (int | Unset): Trend start timestamp
            end_timestamp (int | Unset): Trend end timestamp
            gmv (GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfileGmv | Unset):
            units_sold (int | Unset): Trend units sold
            follower (int | Unset): Trend follower
            engagement_rate (int | Unset): Trend engagement rate e.g. 558 means creator's engagement rate is 5.58%
     """

    start_timestamp: int | Unset = UNSET
    end_timestamp: int | Unset = UNSET
    gmv: GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfileGmv | Unset = UNSET
    units_sold: int | Unset = UNSET
    follower: int | Unset = UNSET
    engagement_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile_gmv import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfileGmv # noqa: PLC0415
        start_timestamp = self.start_timestamp

        end_timestamp = self.end_timestamp

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        units_sold = self.units_sold

        follower = self.follower

        engagement_rate = self.engagement_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start_timestamp is not UNSET:
            field_dict["start_timestamp"] = start_timestamp
        if end_timestamp is not UNSET:
            field_dict["end_timestamp"] = end_timestamp
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if units_sold is not UNSET:
            field_dict["units_sold"] = units_sold
        if follower is not UNSET:
            field_dict["follower"] = follower
        if engagement_rate is not UNSET:
            field_dict["engagement_rate"] = engagement_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile_gmv import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfileGmv # noqa: PLC0415
        d = dict(src_dict)
        start_timestamp = d.pop("start_timestamp", UNSET)

        end_timestamp = d.pop("end_timestamp", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfileGmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfileGmv.from_dict(_gmv)




        units_sold = d.pop("units_sold", UNSET)

        follower = d.pop("follower", UNSET)

        engagement_rate = d.pop("engagement_rate", UNSET)

        get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile = cls(
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            gmv=gmv,
            units_sold=units_sold,
            follower=follower,
            engagement_rate=engagement_rate,
        )


        get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile.additional_properties = d
        return get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile

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
