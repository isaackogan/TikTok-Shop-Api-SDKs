from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile_creator_connect_info import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorConnectInfo
  from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfile





T = TypeVar("T", bound="GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfile")



@_attrs_define
class GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfile:
    """ 
        Attributes:
            is_official_recommend (bool | Unset): Creaor has official recommend tag or not
            contact_info_available (bool | Unset): Is creator contact infomation available
            creator_bind_mcn_name (str | Unset): Creator bind MCN name
            live_engagement_rate_30d (int | Unset): Creator engagement rate last 30 days
            video_play_cnt_30d_med (int | Unset): Creator average VIDEO play count last 30 days
            live_view_cnt_30d_med (int | Unset): Creator average LIVE view count last 30 days
            live_like_cnt_30d (int | Unset): Creator LIVE like count last 30 days
            live_comment_cnt_30d_med (int | Unset): Creator average LIVE comment count last 30 days
            live_share_cnt_30d_med (int | Unset): Creator average LIVE share count last 30 days
            video_publish_cnt_30d_med (int | Unset): Creator average VIDEO publish count last 30 days
            has_invited_90d (bool | Unset): Has invited before 90 days
            is_creator_blocked (bool | Unset): Is creator blocked by shop
            creator_level (int | Unset): Creator level
            creator_fulfillment_reviews (int | Unset): The number of fulfillment reviews submitted by sellers for the
                creator in the last 90 days.
            is_eligible_flat_fee (bool | Unset): Creator is eligible for flat fee invitation
            is_rising_star (bool | Unset): Creator has rising star tag or not
            creator_fulfillment_score_90d (str | Unset): Creator fulfillment score during last 90 days
            sample_score (int | Unset): Creator credit total score. e.g. 75 means creator' sample scole is 75/100.
            creator_connect_info (GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorConnectInfo |
                Unset):
            creator_trend_profile
                (list[GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfile] | Unset): Creator
                trend infomation
     """

    is_official_recommend: bool | Unset = UNSET
    contact_info_available: bool | Unset = UNSET
    creator_bind_mcn_name: str | Unset = UNSET
    live_engagement_rate_30d: int | Unset = UNSET
    video_play_cnt_30d_med: int | Unset = UNSET
    live_view_cnt_30d_med: int | Unset = UNSET
    live_like_cnt_30d: int | Unset = UNSET
    live_comment_cnt_30d_med: int | Unset = UNSET
    live_share_cnt_30d_med: int | Unset = UNSET
    video_publish_cnt_30d_med: int | Unset = UNSET
    has_invited_90d: bool | Unset = UNSET
    is_creator_blocked: bool | Unset = UNSET
    creator_level: int | Unset = UNSET
    creator_fulfillment_reviews: int | Unset = UNSET
    is_eligible_flat_fee: bool | Unset = UNSET
    is_rising_star: bool | Unset = UNSET
    creator_fulfillment_score_90d: str | Unset = UNSET
    sample_score: int | Unset = UNSET
    creator_connect_info: GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorConnectInfo | Unset = UNSET
    creator_trend_profile: list[GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile_creator_connect_info import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorConnectInfo # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfile # noqa: PLC0415
        is_official_recommend = self.is_official_recommend

        contact_info_available = self.contact_info_available

        creator_bind_mcn_name = self.creator_bind_mcn_name

        live_engagement_rate_30d = self.live_engagement_rate_30d

        video_play_cnt_30d_med = self.video_play_cnt_30d_med

        live_view_cnt_30d_med = self.live_view_cnt_30d_med

        live_like_cnt_30d = self.live_like_cnt_30d

        live_comment_cnt_30d_med = self.live_comment_cnt_30d_med

        live_share_cnt_30d_med = self.live_share_cnt_30d_med

        video_publish_cnt_30d_med = self.video_publish_cnt_30d_med

        has_invited_90d = self.has_invited_90d

        is_creator_blocked = self.is_creator_blocked

        creator_level = self.creator_level

        creator_fulfillment_reviews = self.creator_fulfillment_reviews

        is_eligible_flat_fee = self.is_eligible_flat_fee

        is_rising_star = self.is_rising_star

        creator_fulfillment_score_90d = self.creator_fulfillment_score_90d

        sample_score = self.sample_score

        creator_connect_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_connect_info, Unset):
            creator_connect_info = self.creator_connect_info.to_dict()

        creator_trend_profile: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creator_trend_profile, Unset):
            creator_trend_profile = []
            for creator_trend_profile_item_data in self.creator_trend_profile:
                creator_trend_profile_item = creator_trend_profile_item_data.to_dict()
                creator_trend_profile.append(creator_trend_profile_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_official_recommend is not UNSET:
            field_dict["is_official_recommend"] = is_official_recommend
        if contact_info_available is not UNSET:
            field_dict["contact_info_available"] = contact_info_available
        if creator_bind_mcn_name is not UNSET:
            field_dict["creator_bind_mcn_name"] = creator_bind_mcn_name
        if live_engagement_rate_30d is not UNSET:
            field_dict["live_engagement_rate_30d"] = live_engagement_rate_30d
        if video_play_cnt_30d_med is not UNSET:
            field_dict["video_play_cnt_30d_med"] = video_play_cnt_30d_med
        if live_view_cnt_30d_med is not UNSET:
            field_dict["live_view_cnt_30d_med"] = live_view_cnt_30d_med
        if live_like_cnt_30d is not UNSET:
            field_dict["live_like_cnt_30d"] = live_like_cnt_30d
        if live_comment_cnt_30d_med is not UNSET:
            field_dict["live_comment_cnt_30d_med"] = live_comment_cnt_30d_med
        if live_share_cnt_30d_med is not UNSET:
            field_dict["live_share_cnt_30d_med"] = live_share_cnt_30d_med
        if video_publish_cnt_30d_med is not UNSET:
            field_dict["video_publish_cnt_30d_med"] = video_publish_cnt_30d_med
        if has_invited_90d is not UNSET:
            field_dict["has_invited_90d"] = has_invited_90d
        if is_creator_blocked is not UNSET:
            field_dict["is_creator_blocked"] = is_creator_blocked
        if creator_level is not UNSET:
            field_dict["creator_level"] = creator_level
        if creator_fulfillment_reviews is not UNSET:
            field_dict["creator_fulfillment_reviews"] = creator_fulfillment_reviews
        if is_eligible_flat_fee is not UNSET:
            field_dict["is_eligible_flat_fee"] = is_eligible_flat_fee
        if is_rising_star is not UNSET:
            field_dict["is_rising_star"] = is_rising_star
        if creator_fulfillment_score_90d is not UNSET:
            field_dict["creator_fulfillment_score_90d"] = creator_fulfillment_score_90d
        if sample_score is not UNSET:
            field_dict["sample_score"] = sample_score
        if creator_connect_info is not UNSET:
            field_dict["creator_connect_info"] = creator_connect_info
        if creator_trend_profile is not UNSET:
            field_dict["creator_trend_profile"] = creator_trend_profile

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile_creator_connect_info import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorConnectInfo # noqa: PLC0415
        from ..models.get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile import GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfile # noqa: PLC0415
        d = dict(src_dict)
        is_official_recommend = d.pop("is_official_recommend", UNSET)

        contact_info_available = d.pop("contact_info_available", UNSET)

        creator_bind_mcn_name = d.pop("creator_bind_mcn_name", UNSET)

        live_engagement_rate_30d = d.pop("live_engagement_rate_30d", UNSET)

        video_play_cnt_30d_med = d.pop("video_play_cnt_30d_med", UNSET)

        live_view_cnt_30d_med = d.pop("live_view_cnt_30d_med", UNSET)

        live_like_cnt_30d = d.pop("live_like_cnt_30d", UNSET)

        live_comment_cnt_30d_med = d.pop("live_comment_cnt_30d_med", UNSET)

        live_share_cnt_30d_med = d.pop("live_share_cnt_30d_med", UNSET)

        video_publish_cnt_30d_med = d.pop("video_publish_cnt_30d_med", UNSET)

        has_invited_90d = d.pop("has_invited_90d", UNSET)

        is_creator_blocked = d.pop("is_creator_blocked", UNSET)

        creator_level = d.pop("creator_level", UNSET)

        creator_fulfillment_reviews = d.pop("creator_fulfillment_reviews", UNSET)

        is_eligible_flat_fee = d.pop("is_eligible_flat_fee", UNSET)

        is_rising_star = d.pop("is_rising_star", UNSET)

        creator_fulfillment_score_90d = d.pop("creator_fulfillment_score_90d", UNSET)

        sample_score = d.pop("sample_score", UNSET)

        _creator_connect_info = d.pop("creator_connect_info", UNSET)
        creator_connect_info: GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorConnectInfo | Unset
        if isinstance(_creator_connect_info,  Unset):
            creator_connect_info = UNSET
        else:
            creator_connect_info = GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorConnectInfo.from_dict(_creator_connect_info)




        _creator_trend_profile = d.pop("creator_trend_profile", UNSET)
        creator_trend_profile: list[GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfile] | Unset = UNSET
        if _creator_trend_profile is not UNSET:
            creator_trend_profile = []
            for creator_trend_profile_item_data in _creator_trend_profile:
                creator_trend_profile_item = GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfile.from_dict(creator_trend_profile_item_data)



                creator_trend_profile.append(creator_trend_profile_item)


        get_marketplace_creator_performance_response_data_creator_creator_profile = cls(
            is_official_recommend=is_official_recommend,
            contact_info_available=contact_info_available,
            creator_bind_mcn_name=creator_bind_mcn_name,
            live_engagement_rate_30d=live_engagement_rate_30d,
            video_play_cnt_30d_med=video_play_cnt_30d_med,
            live_view_cnt_30d_med=live_view_cnt_30d_med,
            live_like_cnt_30d=live_like_cnt_30d,
            live_comment_cnt_30d_med=live_comment_cnt_30d_med,
            live_share_cnt_30d_med=live_share_cnt_30d_med,
            video_publish_cnt_30d_med=video_publish_cnt_30d_med,
            has_invited_90d=has_invited_90d,
            is_creator_blocked=is_creator_blocked,
            creator_level=creator_level,
            creator_fulfillment_reviews=creator_fulfillment_reviews,
            is_eligible_flat_fee=is_eligible_flat_fee,
            is_rising_star=is_rising_star,
            creator_fulfillment_score_90d=creator_fulfillment_score_90d,
            sample_score=sample_score,
            creator_connect_info=creator_connect_info,
            creator_trend_profile=creator_trend_profile,
        )


        get_marketplace_creator_performance_response_data_creator_creator_profile.additional_properties = d
        return get_marketplace_creator_performance_response_data_creator_creator_profile

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
