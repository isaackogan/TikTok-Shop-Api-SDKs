from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItemPostImage")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseDataChannelSummaryPhotoTopItemPostImage:
    """ 
        Attributes:
            color (str | Unset): Color of the image metadata for the images in the photo post.
            height (int | Unset): Height of the image metadata for the images in the photo post.
            mimetype (str | Unset): MIME type of the image.
            size (str | Unset): Size of the image metadata for the images in the photo post.
            thumb_uri (str | Unset): Resource URI identifying the image thumbnail.
            thumb_url_list (list[str] | Unset): URLs for the image thumbnail.
            tint_color (str | Unset): Tint color of the image metadata for the images in the photo post.
            uri (str | Unset): Resource URI identifying the image.
            url_list (list[str] | Unset): URLs for the image.
            width (int | Unset): Width of the image metadata for the images in the photo post.
     """

    color: str | Unset = UNSET
    height: int | Unset = UNSET
    mimetype: str | Unset = UNSET
    size: str | Unset = UNSET
    thumb_uri: str | Unset = UNSET
    thumb_url_list: list[str] | Unset = UNSET
    tint_color: str | Unset = UNSET
    uri: str | Unset = UNSET
    url_list: list[str] | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        color = self.color

        height = self.height

        mimetype = self.mimetype

        size = self.size

        thumb_uri = self.thumb_uri

        thumb_url_list: list[str] | Unset = UNSET
        if not isinstance(self.thumb_url_list, Unset):
            thumb_url_list = self.thumb_url_list



        tint_color = self.tint_color

        uri = self.uri

        url_list: list[str] | Unset = UNSET
        if not isinstance(self.url_list, Unset):
            url_list = self.url_list



        width = self.width


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if height is not UNSET:
            field_dict["height"] = height
        if mimetype is not UNSET:
            field_dict["mimetype"] = mimetype
        if size is not UNSET:
            field_dict["size"] = size
        if thumb_uri is not UNSET:
            field_dict["thumb_uri"] = thumb_uri
        if thumb_url_list is not UNSET:
            field_dict["thumb_url_list"] = thumb_url_list
        if tint_color is not UNSET:
            field_dict["tint_color"] = tint_color
        if uri is not UNSET:
            field_dict["uri"] = uri
        if url_list is not UNSET:
            field_dict["url_list"] = url_list
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color", UNSET)

        height = d.pop("height", UNSET)

        mimetype = d.pop("mimetype", UNSET)

        size = d.pop("size", UNSET)

        thumb_uri = d.pop("thumb_uri", UNSET)

        thumb_url_list = cast(list[str], d.pop("thumb_url_list", UNSET))


        tint_color = d.pop("tint_color", UNSET)

        uri = d.pop("uri", UNSET)

        url_list = cast(list[str], d.pop("url_list", UNSET))


        width = d.pop("width", UNSET)

        get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item_post_image = cls(
            color=color,
            height=height,
            mimetype=mimetype,
            size=size,
            thumb_uri=thumb_uri,
            thumb_url_list=thumb_url_list,
            tint_color=tint_color,
            uri=uri,
            url_list=url_list,
            width=width,
        )


        get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item_post_image.additional_properties = d
        return get_acc_audience_preference_summary_response_data_channel_summary_photo_top_item_post_image

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
