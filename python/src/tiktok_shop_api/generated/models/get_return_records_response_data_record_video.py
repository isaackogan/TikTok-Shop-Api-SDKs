from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetReturnRecordsResponseDataRecordVideo")



@_attrs_define
class GetReturnRecordsResponseDataRecordVideo:
    """ 
        Attributes:
            url (str | Unset): Video URL.
            cover (str | Unset): Video thumbnail image.
            width (int | Unset): Video image width.
                Unit: px
            height (int | Unset): Video image height.
                Unit: px
            duration_millis (int | Unset): Video duration.
                Unit: milliseconds
     """

    url: str | Unset = UNSET
    cover: str | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    duration_millis: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        cover = self.cover

        width = self.width

        height = self.height

        duration_millis = self.duration_millis


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url
        if cover is not UNSET:
            field_dict["cover"] = cover
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if duration_millis is not UNSET:
            field_dict["duration_millis"] = duration_millis

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        cover = d.pop("cover", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        duration_millis = d.pop("duration_millis", UNSET)

        get_return_records_response_data_record_video = cls(
            url=url,
            cover=cover,
            width=width,
            height=height,
            duration_millis=duration_millis,
        )


        get_return_records_response_data_record_video.additional_properties = d
        return get_return_records_response_data_record_video

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
