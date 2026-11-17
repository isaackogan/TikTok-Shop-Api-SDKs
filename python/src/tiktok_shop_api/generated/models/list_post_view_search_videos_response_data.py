from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.list_post_view_search_videos_response_data_video import ListPostViewSearchVideosResponseDataVideo





T = TypeVar("T", bound="ListPostViewSearchVideosResponseData")



@_attrs_define
class ListPostViewSearchVideosResponseData:
    """ 
        Attributes:
            next_page_token (str): Pass unchanged to retrieve the next page. Empty means the end of the available result
                window.
            end_date (datetime.date | Unset): Effective inclusive end date.
            start_date (datetime.date | Unset): Effective inclusive start date.
            videos (list[ListPostViewSearchVideosResponseDataVideo] | Unset): Videos in this page. A page can be empty while
                next_page_token is nonempty when no eligible videos remain in that source page.
     """

    next_page_token: str
    end_date: datetime.date | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    videos: list[ListPostViewSearchVideosResponseDataVideo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_post_view_search_videos_response_data_video import ListPostViewSearchVideosResponseDataVideo # noqa: PLC0415
        next_page_token = self.next_page_token

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        videos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "next_page_token": next_page_token,
        })
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if videos is not UNSET:
            field_dict["videos"] = videos

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_post_view_search_videos_response_data_video import ListPostViewSearchVideosResponseDataVideo # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token")

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        _videos = d.pop("videos", UNSET)
        videos: list[ListPostViewSearchVideosResponseDataVideo] | Unset = UNSET
        if _videos is not UNSET:
            videos = []
            for videos_item_data in _videos:
                videos_item = ListPostViewSearchVideosResponseDataVideo.from_dict(videos_item_data)



                videos.append(videos_item)


        list_post_view_search_videos_response_data = cls(
            next_page_token=next_page_token,
            end_date=end_date,
            start_date=start_date,
            videos=videos,
        )


        list_post_view_search_videos_response_data.additional_properties = d
        return list_post_view_search_videos_response_data

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
