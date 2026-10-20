from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shop_videos_performance_details_response_data_video_performance_interval import GetShopVideosPerformanceDetailsResponseDataVideoPerformanceInterval
  from ..models.get_shop_videos_performance_details_response_data_video_performance_viewer_profile import GetShopVideosPerformanceDetailsResponseDataVideoPerformanceViewerProfile





T = TypeVar("T", bound="GetShopVideosPerformanceDetailsResponseDataVideoPerformance")



@_attrs_define
class GetShopVideosPerformanceDetailsResponseDataVideoPerformance:
    """ 
        Attributes:
            intervals (list[GetShopVideosPerformanceDetailsResponseDataVideoPerformanceInterval] | Unset): Interval data for
                the requested time range.
            viewer_profile (list[GetShopVideosPerformanceDetailsResponseDataVideoPerformanceViewerProfile] | Unset): Viewer
                profile of the video.
     """

    intervals: list[GetShopVideosPerformanceDetailsResponseDataVideoPerformanceInterval] | Unset = UNSET
    viewer_profile: list[GetShopVideosPerformanceDetailsResponseDataVideoPerformanceViewerProfile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_videos_performance_details_response_data_video_performance_interval import GetShopVideosPerformanceDetailsResponseDataVideoPerformanceInterval # noqa: PLC0415
        from ..models.get_shop_videos_performance_details_response_data_video_performance_viewer_profile import GetShopVideosPerformanceDetailsResponseDataVideoPerformanceViewerProfile # noqa: PLC0415
        intervals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intervals, Unset):
            intervals = []
            for intervals_item_data in self.intervals:
                intervals_item = intervals_item_data.to_dict()
                intervals.append(intervals_item)



        viewer_profile: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.viewer_profile, Unset):
            viewer_profile = []
            for viewer_profile_item_data in self.viewer_profile:
                viewer_profile_item = viewer_profile_item_data.to_dict()
                viewer_profile.append(viewer_profile_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if intervals is not UNSET:
            field_dict["intervals"] = intervals
        if viewer_profile is not UNSET:
            field_dict["viewer_profile"] = viewer_profile

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_videos_performance_details_response_data_video_performance_interval import GetShopVideosPerformanceDetailsResponseDataVideoPerformanceInterval # noqa: PLC0415
        from ..models.get_shop_videos_performance_details_response_data_video_performance_viewer_profile import GetShopVideosPerformanceDetailsResponseDataVideoPerformanceViewerProfile # noqa: PLC0415
        d = dict(src_dict)
        _intervals = d.pop("intervals", UNSET)
        intervals: list[GetShopVideosPerformanceDetailsResponseDataVideoPerformanceInterval] | Unset = UNSET
        if _intervals is not UNSET:
            intervals = []
            for intervals_item_data in _intervals:
                intervals_item = GetShopVideosPerformanceDetailsResponseDataVideoPerformanceInterval.from_dict(intervals_item_data)



                intervals.append(intervals_item)


        _viewer_profile = d.pop("viewer_profile", UNSET)
        viewer_profile: list[GetShopVideosPerformanceDetailsResponseDataVideoPerformanceViewerProfile] | Unset = UNSET
        if _viewer_profile is not UNSET:
            viewer_profile = []
            for viewer_profile_item_data in _viewer_profile:
                viewer_profile_item = GetShopVideosPerformanceDetailsResponseDataVideoPerformanceViewerProfile.from_dict(viewer_profile_item_data)



                viewer_profile.append(viewer_profile_item)


        get_shop_videos_performance_details_response_data_video_performance = cls(
            intervals=intervals,
            viewer_profile=viewer_profile,
        )


        get_shop_videos_performance_details_response_data_video_performance.additional_properties = d
        return get_shop_videos_performance_details_response_data_video_performance

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
