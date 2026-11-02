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
  from ..models.get_off_site_performance_details_response_data_content_creator import GetOffSitePerformanceDetailsResponseDataContentCreator
  from ..models.get_off_site_performance_details_response_data_content_metric import GetOffSitePerformanceDetailsResponseDataContentMetric





T = TypeVar("T", bound="GetOffSitePerformanceDetailsResponseDataContent")



@_attrs_define
class GetOffSitePerformanceDetailsResponseDataContent:
    """ 
        Attributes:
            content_id (str | Unset): Video ID for VIDEO items, LIVE room ID for LIVE items, or product ID for PRODUCT
                items.
            content_type (str | Unset): Type of item: VIDEO (video), LIVE (LIVE session), or PRODUCT (product).
            cover_image_url (str | Unset): Cover image URL for the video, LIVE session, or product, when available.
            creator (GetOffSitePerformanceDetailsResponseDataContentCreator | Unset):
            duration_seconds (int | None | Unset): Duration of the VIDEO or LIVE session in seconds, when available. Not
                applicable to PRODUCT items; missing or inapplicable metadata may be null.
            metrics (GetOffSitePerformanceDetailsResponseDataContentMetric | Unset):
            post_time (datetime.datetime | None | Unset): Publication time for VIDEO items or start time for LIVE sessions,
                expressed as an ISO 8601 timestamp with timezone. Not applicable to PRODUCT items; unavailable metadata may be
                null.
            rank (int | Unset): One-based display position in the current sorted result set, continuing across pages. This
                is not a stable business rank; records with equal sort values may change order between requests.
            title (str | Unset): Video title, LIVE session title, or product name, depending on content_type, when
                available.
     """

    content_id: str | Unset = UNSET
    content_type: str | Unset = UNSET
    cover_image_url: str | Unset = UNSET
    creator: GetOffSitePerformanceDetailsResponseDataContentCreator | Unset = UNSET
    duration_seconds: int | None | Unset = UNSET
    metrics: GetOffSitePerformanceDetailsResponseDataContentMetric | Unset = UNSET
    post_time: datetime.datetime | None | Unset = UNSET
    rank: int | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_off_site_performance_details_response_data_content_creator import GetOffSitePerformanceDetailsResponseDataContentCreator # noqa: PLC0415
        from ..models.get_off_site_performance_details_response_data_content_metric import GetOffSitePerformanceDetailsResponseDataContentMetric # noqa: PLC0415
        content_id = self.content_id

        content_type = self.content_type

        cover_image_url = self.cover_image_url

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        duration_seconds: int | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        post_time: None | str | Unset
        if isinstance(self.post_time, Unset):
            post_time = UNSET
        elif isinstance(self.post_time, datetime.datetime):
            post_time = self.post_time.isoformat()
        else:
            post_time = self.post_time

        rank = self.rank

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if cover_image_url is not UNSET:
            field_dict["cover_image_url"] = cover_image_url
        if creator is not UNSET:
            field_dict["creator"] = creator
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if post_time is not UNSET:
            field_dict["post_time"] = post_time
        if rank is not UNSET:
            field_dict["rank"] = rank
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_off_site_performance_details_response_data_content_creator import GetOffSitePerformanceDetailsResponseDataContentCreator # noqa: PLC0415
        from ..models.get_off_site_performance_details_response_data_content_metric import GetOffSitePerformanceDetailsResponseDataContentMetric # noqa: PLC0415
        d = dict(src_dict)
        content_id = d.pop("content_id", UNSET)

        content_type = d.pop("content_type", UNSET)

        cover_image_url = d.pop("cover_image_url", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: GetOffSitePerformanceDetailsResponseDataContentCreator | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = GetOffSitePerformanceDetailsResponseDataContentCreator.from_dict(_creator)




        def _parse_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))


        _metrics = d.pop("metrics", UNSET)
        metrics: GetOffSitePerformanceDetailsResponseDataContentMetric | Unset
        if isinstance(_metrics,  Unset):
            metrics = UNSET
        else:
            metrics = GetOffSitePerformanceDetailsResponseDataContentMetric.from_dict(_metrics)




        def _parse_post_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                post_time_type_0 = datetime.datetime.fromisoformat(data)



                return post_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        post_time = _parse_post_time(d.pop("post_time", UNSET))


        rank = d.pop("rank", UNSET)

        title = d.pop("title", UNSET)

        get_off_site_performance_details_response_data_content = cls(
            content_id=content_id,
            content_type=content_type,
            cover_image_url=cover_image_url,
            creator=creator,
            duration_seconds=duration_seconds,
            metrics=metrics,
            post_time=post_time,
            rank=rank,
            title=title,
        )


        get_off_site_performance_details_response_data_content.additional_properties = d
        return get_off_site_performance_details_response_data_content

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
