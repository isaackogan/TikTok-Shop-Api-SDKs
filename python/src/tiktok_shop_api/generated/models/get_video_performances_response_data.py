from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_video_performances_response_data_video import GetVideoPerformancesResponseDataVideo





T = TypeVar("T", bound="GetVideoPerformancesResponseData")



@_attrs_define
class GetVideoPerformancesResponseData:
    """ 
        Attributes:
            videos (list[GetVideoPerformancesResponseDataVideo] | Unset): Contains a list of video objects. The inner list
                of objects will be organized in ascending order based on the video_id field.
     """

    videos: list[GetVideoPerformancesResponseDataVideo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_video_performances_response_data_video import GetVideoPerformancesResponseDataVideo # noqa: PLC0415
        videos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if videos is not UNSET:
            field_dict["videos"] = videos

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_video_performances_response_data_video import GetVideoPerformancesResponseDataVideo # noqa: PLC0415
        d = dict(src_dict)
        _videos = d.pop("videos", UNSET)
        videos: list[GetVideoPerformancesResponseDataVideo] | Unset = UNSET
        if _videos is not UNSET:
            videos = []
            for videos_item_data in _videos:
                videos_item = GetVideoPerformancesResponseDataVideo.from_dict(videos_item_data)



                videos.append(videos_item)


        get_video_performances_response_data = cls(
            videos=videos,
        )


        get_video_performances_response_data.additional_properties = d
        return get_video_performances_response_data

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
