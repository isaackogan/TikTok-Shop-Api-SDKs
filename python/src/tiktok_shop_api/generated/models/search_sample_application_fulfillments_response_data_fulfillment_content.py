from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchSampleApplicationFulfillmentsResponseDataFulfillmentContent")



@_attrs_define
class SearchSampleApplicationFulfillmentsResponseDataFulfillmentContent:
    """ 
        Attributes:
            id (str | Unset): The video or live room identifier.
            format_ (str | Unset): The format of the generated content:
                - LIVE
                - `VIDEO`
            url (str | Unset): The content source link.
            view_count (int | Unset): The cumulative number of views of the content.
            like_count (int | Unset): The cumulative number of likes on the content.
            comment_count (int | Unset): The cumulative number of comments on the content.
            paid_order_count (int | Unset): The cumulative total number of orders paid for content.
            page_link (str | Unset): Content page url of TikTok.
            description (str | Unset): The title of video or the description of the live room.
            create_time (int | Unset): - When `format` is `VIDEO`, this is the Unix timestamp, in seconds, when the video is
                first made public and linked to the product.
                - When `format` is `LIVE`, this is the Unix timestamp, in seconds, when the product link is first added to the
                live stream.
            live_end_time (int | Unset): Only when `format==LIVE`.
                It refers to the time when the product link is removed from the live room. If the product link remains active
                and is not removed, then it is the end of the live stream.
     """

    id: str | Unset = UNSET
    format_: str | Unset = UNSET
    url: str | Unset = UNSET
    view_count: int | Unset = UNSET
    like_count: int | Unset = UNSET
    comment_count: int | Unset = UNSET
    paid_order_count: int | Unset = UNSET
    page_link: str | Unset = UNSET
    description: str | Unset = UNSET
    create_time: int | Unset = UNSET
    live_end_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        format_ = self.format_

        url = self.url

        view_count = self.view_count

        like_count = self.like_count

        comment_count = self.comment_count

        paid_order_count = self.paid_order_count

        page_link = self.page_link

        description = self.description

        create_time = self.create_time

        live_end_time = self.live_end_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if format_ is not UNSET:
            field_dict["format"] = format_
        if url is not UNSET:
            field_dict["url"] = url
        if view_count is not UNSET:
            field_dict["view_count"] = view_count
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if comment_count is not UNSET:
            field_dict["comment_count"] = comment_count
        if paid_order_count is not UNSET:
            field_dict["paid_order_count"] = paid_order_count
        if page_link is not UNSET:
            field_dict["page_link"] = page_link
        if description is not UNSET:
            field_dict["description"] = description
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if live_end_time is not UNSET:
            field_dict["live_end_time"] = live_end_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        format_ = d.pop("format", UNSET)

        url = d.pop("url", UNSET)

        view_count = d.pop("view_count", UNSET)

        like_count = d.pop("like_count", UNSET)

        comment_count = d.pop("comment_count", UNSET)

        paid_order_count = d.pop("paid_order_count", UNSET)

        page_link = d.pop("page_link", UNSET)

        description = d.pop("description", UNSET)

        create_time = d.pop("create_time", UNSET)

        live_end_time = d.pop("live_end_time", UNSET)

        search_sample_application_fulfillments_response_data_fulfillment_content = cls(
            id=id,
            format_=format_,
            url=url,
            view_count=view_count,
            like_count=like_count,
            comment_count=comment_count,
            paid_order_count=paid_order_count,
            page_link=page_link,
            description=description,
            create_time=create_time,
            live_end_time=live_end_time,
        )


        search_sample_application_fulfillments_response_data_fulfillment_content.additional_properties = d
        return search_sample_application_fulfillments_response_data_fulfillment_content

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
