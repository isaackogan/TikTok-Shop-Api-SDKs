from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShoppableVideoStatusResponseDataVideo")


@_attrs_define
class GetShoppableVideoStatusResponseDataVideo:
    """
    Attributes:
        id (str | Unset): Video id
        post_status (str | Unset): Video posting status. Possible values:
            - SUCCESS: The video was posted successfully.
            - FAIL: The video failed to post.
            - PROCESSING: The video is still being processed. Call this API again later to get the latest status.
        post_time (int | Unset): Returned if the video has been successfully posted, i.e. `posting_status = SUCCESS`.
            Represented in seconds.
    """

    id: str | Unset = UNSET
    post_status: str | Unset = UNSET
    post_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        post_status = self.post_status

        post_time = self.post_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if post_status is not UNSET:
            field_dict["post_status"] = post_status
        if post_time is not UNSET:
            field_dict["post_time"] = post_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        post_status = d.pop("post_status", UNSET)

        post_time = d.pop("post_time", UNSET)

        get_shoppable_video_status_response_data_video = cls(
            id=id,
            post_status=post_status,
            post_time=post_time,
        )

        get_shoppable_video_status_response_data_video.additional_properties = d
        return get_shoppable_video_status_response_data_video

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
