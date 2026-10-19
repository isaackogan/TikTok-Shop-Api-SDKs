from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avatar import Avatar
    from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv import (
        GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv,
    )
    from ..models.get_marketplace_creator_performance_response_data_creator_live_gmv import (
        GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv,
    )
    from ..models.gmv_range import GmvRange
    from ..models.search_creators_in_creator_marketplace_response_data_creator_creator_profile import (
        SearchCreatorsInCreatorMarketplaceResponseDataCreatorCreatorProfile,
    )
    from ..models.search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic import (
        SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographic,
    )
    from ..models.units_sold_range import UnitsSoldRange
    from ..models.video_gmv import VideoGmv


T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceResponseDataCreator")


@_attrs_define
class SearchCreatorsInCreatorMarketplaceResponseDataCreator:
    """
    Attributes:
        username (str | Unset): Creator's TikTok Username
        nickname (str | Unset): Creator's TikTok Nickname
        avatar (Avatar | Unset):
        selection_region (str | Unset): Regions where the creator operates and promotes products
        category_ids (list[str] | Unset): It indicates the main product categories when the creator posts products.
        avg_ec_live_uv (int | Unset): Average UV for creator's e-commerce live streams
        avg_ec_video_view_count (int | Unset): Average views for creator's e-commerce videos
        follower_count (int | Unset): Follower count
        gmv (GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv | Unset):
        live_gmv (GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv | Unset):
        video_gmv (VideoGmv | Unset):
        gmv_range (GmvRange | Unset):
        units_sold_range (UnitsSoldRange | Unset):
        top_follower_demographics (SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographic | Unset):
        creator_open_id (str | Unset): Creator Open ID. [More
            details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
        creator_profile (SearchCreatorsInCreatorMarketplaceResponseDataCreatorCreatorProfile | Unset):
    """

    username: str | Unset = UNSET
    nickname: str | Unset = UNSET
    avatar: Avatar | Unset = UNSET
    selection_region: str | Unset = UNSET
    category_ids: list[str] | Unset = UNSET
    avg_ec_live_uv: int | Unset = UNSET
    avg_ec_video_view_count: int | Unset = UNSET
    follower_count: int | Unset = UNSET
    gmv: GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv | Unset = UNSET
    live_gmv: GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv | Unset = UNSET
    video_gmv: VideoGmv | Unset = UNSET
    gmv_range: GmvRange | Unset = UNSET
    units_sold_range: UnitsSoldRange | Unset = UNSET
    top_follower_demographics: SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographic | Unset = (
        UNSET
    )
    creator_open_id: str | Unset = UNSET
    creator_profile: SearchCreatorsInCreatorMarketplaceResponseDataCreatorCreatorProfile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        nickname = self.nickname

        avatar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        selection_region = self.selection_region

        category_ids: list[str] | Unset = UNSET
        if not isinstance(self.category_ids, Unset):
            category_ids = self.category_ids

        avg_ec_live_uv = self.avg_ec_live_uv

        avg_ec_video_view_count = self.avg_ec_video_view_count

        follower_count = self.follower_count

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        live_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_gmv, Unset):
            live_gmv = self.live_gmv.to_dict()

        video_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_gmv, Unset):
            video_gmv = self.video_gmv.to_dict()

        gmv_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv_range, Unset):
            gmv_range = self.gmv_range.to_dict()

        units_sold_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.units_sold_range, Unset):
            units_sold_range = self.units_sold_range.to_dict()

        top_follower_demographics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_follower_demographics, Unset):
            top_follower_demographics = self.top_follower_demographics.to_dict()

        creator_open_id = self.creator_open_id

        creator_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_profile, Unset):
            creator_profile = self.creator_profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if selection_region is not UNSET:
            field_dict["selection_region"] = selection_region
        if category_ids is not UNSET:
            field_dict["category_ids"] = category_ids
        if avg_ec_live_uv is not UNSET:
            field_dict["avg_ec_live_uv"] = avg_ec_live_uv
        if avg_ec_video_view_count is not UNSET:
            field_dict["avg_ec_video_view_count"] = avg_ec_video_view_count
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if live_gmv is not UNSET:
            field_dict["live_gmv"] = live_gmv
        if video_gmv is not UNSET:
            field_dict["video_gmv"] = video_gmv
        if gmv_range is not UNSET:
            field_dict["gmv_range"] = gmv_range
        if units_sold_range is not UNSET:
            field_dict["units_sold_range"] = units_sold_range
        if top_follower_demographics is not UNSET:
            field_dict["top_follower_demographics"] = top_follower_demographics
        if creator_open_id is not UNSET:
            field_dict["creator_open_id"] = creator_open_id
        if creator_profile is not UNSET:
            field_dict["creator_profile"] = creator_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar import Avatar  # noqa: PLC0415
        from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv import (
            GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv,  # noqa: PLC0415
        )
        from ..models.get_marketplace_creator_performance_response_data_creator_live_gmv import (
            GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv,  # noqa: PLC0415
        )
        from ..models.gmv_range import GmvRange  # noqa: PLC0415
        from ..models.search_creators_in_creator_marketplace_response_data_creator_creator_profile import (
            SearchCreatorsInCreatorMarketplaceResponseDataCreatorCreatorProfile,  # noqa: PLC0415
        )
        from ..models.search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic import (
            SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographic,  # noqa: PLC0415
        )
        from ..models.units_sold_range import UnitsSoldRange  # noqa: PLC0415
        from ..models.video_gmv import VideoGmv  # noqa: PLC0415

        d = dict(src_dict)
        username = d.pop("username", UNSET)

        nickname = d.pop("nickname", UNSET)

        _avatar = d.pop("avatar", UNSET)
        avatar: Avatar | Unset
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Avatar.from_dict(_avatar)

        selection_region = d.pop("selection_region", UNSET)

        category_ids = cast(list[str], d.pop("category_ids", UNSET))

        avg_ec_live_uv = d.pop("avg_ec_live_uv", UNSET)

        avg_ec_video_view_count = d.pop("avg_ec_video_view_count", UNSET)

        follower_count = d.pop("follower_count", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv | Unset
        if isinstance(_gmv, Unset):
            gmv = UNSET
        else:
            gmv = GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv.from_dict(_gmv)

        _live_gmv = d.pop("live_gmv", UNSET)
        live_gmv: GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv | Unset
        if isinstance(_live_gmv, Unset):
            live_gmv = UNSET
        else:
            live_gmv = GetMarketplaceCreatorPerformanceResponseDataCreatorLiveGmv.from_dict(_live_gmv)

        _video_gmv = d.pop("video_gmv", UNSET)
        video_gmv: VideoGmv | Unset
        if isinstance(_video_gmv, Unset):
            video_gmv = UNSET
        else:
            video_gmv = VideoGmv.from_dict(_video_gmv)

        _gmv_range = d.pop("gmv_range", UNSET)
        gmv_range: GmvRange | Unset
        if isinstance(_gmv_range, Unset):
            gmv_range = UNSET
        else:
            gmv_range = GmvRange.from_dict(_gmv_range)

        _units_sold_range = d.pop("units_sold_range", UNSET)
        units_sold_range: UnitsSoldRange | Unset
        if isinstance(_units_sold_range, Unset):
            units_sold_range = UNSET
        else:
            units_sold_range = UnitsSoldRange.from_dict(_units_sold_range)

        _top_follower_demographics = d.pop("top_follower_demographics", UNSET)
        top_follower_demographics: SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographic | Unset
        if isinstance(_top_follower_demographics, Unset):
            top_follower_demographics = UNSET
        else:
            top_follower_demographics = (
                SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographic.from_dict(
                    _top_follower_demographics
                )
            )

        creator_open_id = d.pop("creator_open_id", UNSET)

        _creator_profile = d.pop("creator_profile", UNSET)
        creator_profile: SearchCreatorsInCreatorMarketplaceResponseDataCreatorCreatorProfile | Unset
        if isinstance(_creator_profile, Unset):
            creator_profile = UNSET
        else:
            creator_profile = SearchCreatorsInCreatorMarketplaceResponseDataCreatorCreatorProfile.from_dict(
                _creator_profile
            )

        search_creators_in_creator_marketplace_response_data_creator = cls(
            username=username,
            nickname=nickname,
            avatar=avatar,
            selection_region=selection_region,
            category_ids=category_ids,
            avg_ec_live_uv=avg_ec_live_uv,
            avg_ec_video_view_count=avg_ec_video_view_count,
            follower_count=follower_count,
            gmv=gmv,
            live_gmv=live_gmv,
            video_gmv=video_gmv,
            gmv_range=gmv_range,
            units_sold_range=units_sold_range,
            top_follower_demographics=top_follower_demographics,
            creator_open_id=creator_open_id,
            creator_profile=creator_profile,
        )

        search_creators_in_creator_marketplace_response_data_creator.additional_properties = d
        return search_creators_in_creator_marketplace_response_data_creator

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
