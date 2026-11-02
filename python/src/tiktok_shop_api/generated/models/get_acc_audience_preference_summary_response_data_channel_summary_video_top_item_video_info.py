from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItemVideoInfo")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItemVideoInfo:
    """ 
        Attributes:
            backup_url (str | Unset): Backup playback URL for this video representation.
            bitrate (int | Unset): Bitrate of this video representation.
            file_hash (str | Unset): Hash identifying this video file.
            format_ (str | Unset): File format of this video representation.
            height (int | Unset): Height format of this video representation.
            main_url (str | Unset): Primary playback URL for this video representation.
            size (int | Unset): Size of this video representation.
            url_expire (int | Unset): Url expire timestamp format of this video representation.
            video_quality (str | Unset): Quality label of this video representation.
            width (int | Unset): Width of this video representation.
     """

    backup_url: str | Unset = UNSET
    bitrate: int | Unset = UNSET
    file_hash: str | Unset = UNSET
    format_: str | Unset = UNSET
    height: int | Unset = UNSET
    main_url: str | Unset = UNSET
    size: int | Unset = UNSET
    url_expire: int | Unset = UNSET
    video_quality: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        backup_url = self.backup_url

        bitrate = self.bitrate

        file_hash = self.file_hash

        format_ = self.format_

        height = self.height

        main_url = self.main_url

        size = self.size

        url_expire = self.url_expire

        video_quality = self.video_quality

        width = self.width


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if backup_url is not UNSET:
            field_dict["backup_url"] = backup_url
        if bitrate is not UNSET:
            field_dict["bitrate"] = bitrate
        if file_hash is not UNSET:
            field_dict["file_hash"] = file_hash
        if format_ is not UNSET:
            field_dict["format"] = format_
        if height is not UNSET:
            field_dict["height"] = height
        if main_url is not UNSET:
            field_dict["main_url"] = main_url
        if size is not UNSET:
            field_dict["size"] = size
        if url_expire is not UNSET:
            field_dict["url_expire"] = url_expire
        if video_quality is not UNSET:
            field_dict["video_quality"] = video_quality
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_url = d.pop("backup_url", UNSET)

        bitrate = d.pop("bitrate", UNSET)

        file_hash = d.pop("file_hash", UNSET)

        format_ = d.pop("format", UNSET)

        height = d.pop("height", UNSET)

        main_url = d.pop("main_url", UNSET)

        size = d.pop("size", UNSET)

        url_expire = d.pop("url_expire", UNSET)

        video_quality = d.pop("video_quality", UNSET)

        width = d.pop("width", UNSET)

        get_acc_audience_preference_summary_response_data_channel_summary_video_top_item_video_info = cls(
            backup_url=backup_url,
            bitrate=bitrate,
            file_hash=file_hash,
            format_=format_,
            height=height,
            main_url=main_url,
            size=size,
            url_expire=url_expire,
            video_quality=video_quality,
            width=width,
        )


        get_acc_audience_preference_summary_response_data_channel_summary_video_top_item_video_info.additional_properties = d
        return get_acc_audience_preference_summary_response_data_channel_summary_video_top_item_video_info

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
