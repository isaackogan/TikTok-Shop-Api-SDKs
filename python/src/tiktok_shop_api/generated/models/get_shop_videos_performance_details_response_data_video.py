from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_available_review_decisions_response_data_error import GetAvailableReviewDecisionsResponseDataError
  from ..models.get_shop_videos_performance_details_response_data_video_performance import GetShopVideosPerformanceDetailsResponseDataVideoPerformance
  from ..models.get_shop_videos_performance_details_response_data_video_video import GetShopVideosPerformanceDetailsResponseDataVideoVideo





T = TypeVar("T", bound="GetShopVideosPerformanceDetailsResponseDataVideo")



@_attrs_define
class GetShopVideosPerformanceDetailsResponseDataVideo:
    """ 
        Attributes:
            error (GetAvailableReviewDecisionsResponseDataError | Unset):
            performance (GetShopVideosPerformanceDetailsResponseDataVideoPerformance | Unset):
            video (GetShopVideosPerformanceDetailsResponseDataVideoVideo | Unset):
            video_id (str | Unset): The requested video ID.
     """

    error: GetAvailableReviewDecisionsResponseDataError | Unset = UNSET
    performance: GetShopVideosPerformanceDetailsResponseDataVideoPerformance | Unset = UNSET
    video: GetShopVideosPerformanceDetailsResponseDataVideoVideo | Unset = UNSET
    video_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_available_review_decisions_response_data_error import GetAvailableReviewDecisionsResponseDataError # noqa: PLC0415
        from ..models.get_shop_videos_performance_details_response_data_video_performance import GetShopVideosPerformanceDetailsResponseDataVideoPerformance # noqa: PLC0415
        from ..models.get_shop_videos_performance_details_response_data_video_video import GetShopVideosPerformanceDetailsResponseDataVideoVideo # noqa: PLC0415
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.performance, Unset):
            performance = self.performance.to_dict()

        video: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        video_id = self.video_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error is not UNSET:
            field_dict["error"] = error
        if performance is not UNSET:
            field_dict["performance"] = performance
        if video is not UNSET:
            field_dict["video"] = video
        if video_id is not UNSET:
            field_dict["video_id"] = video_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_available_review_decisions_response_data_error import GetAvailableReviewDecisionsResponseDataError # noqa: PLC0415
        from ..models.get_shop_videos_performance_details_response_data_video_performance import GetShopVideosPerformanceDetailsResponseDataVideoPerformance # noqa: PLC0415
        from ..models.get_shop_videos_performance_details_response_data_video_video import GetShopVideosPerformanceDetailsResponseDataVideoVideo # noqa: PLC0415
        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: GetAvailableReviewDecisionsResponseDataError | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = GetAvailableReviewDecisionsResponseDataError.from_dict(_error)




        _performance = d.pop("performance", UNSET)
        performance: GetShopVideosPerformanceDetailsResponseDataVideoPerformance | Unset
        if isinstance(_performance,  Unset):
            performance = UNSET
        else:
            performance = GetShopVideosPerformanceDetailsResponseDataVideoPerformance.from_dict(_performance)




        _video = d.pop("video", UNSET)
        video: GetShopVideosPerformanceDetailsResponseDataVideoVideo | Unset
        if isinstance(_video,  Unset):
            video = UNSET
        else:
            video = GetShopVideosPerformanceDetailsResponseDataVideoVideo.from_dict(_video)




        video_id = d.pop("video_id", UNSET)

        get_shop_videos_performance_details_response_data_video = cls(
            error=error,
            performance=performance,
            video=video,
            video_id=video_id,
        )


        get_shop_videos_performance_details_response_data_video.additional_properties = d
        return get_shop_videos_performance_details_response_data_video

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
