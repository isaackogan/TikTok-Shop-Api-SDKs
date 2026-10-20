from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GetAffiliateCampaignCreatorProductContentStatisticsResponseDataCreatorContentStatistic")



@_attrs_define
class GetAffiliateCampaignCreatorProductContentStatisticsResponseDataCreatorContentStatistic:
    """ 
        Attributes:
            content_type (str | Unset): Content type: `VIDEO` for video content or `LIVE_ROOM` for live-room content.
            cover_img_url (str | Unset): A URL for the live room cover image in the TikTok CDN.The video content doesn't
                have this value.
            source_url (str | Unset): The URL on the public TikTok website at which the live room video can be played back.
                When content_type == VIDEO, the value is the url of the source video; when content_type == LIVE_ROOM, the value
                is the url where you can play back the recording of the live.
            view_count (str | Unset): The number of public views of the live room or video.
            like_count (str | Unset): The number of TikTok user likes associated with the live room or video.
            comment_num (str | Unset): The number of TikTok user comments associated with the live room or video.
            paid_order_num (str | Unset): The total number of paid orders associated with the live room or video.
            paid_amount (str | Unset): The aggregate value of product orders associated with the live room or video.
            linked_tiktok_video (str | Unset): The friendly URL for the video on the TikTok website.
            published_date (datetime.date | Unset): When content_type == VIDEO, this is the date when the video was
                published; when content_type == LIVE_ROOM, this is the date when the live started. The value is in YYYY_MM_DD
                format.
            content_end_date (datetime.date | None | Unset): When content_type == VIDEO, this field is None; when
                content_type == LIVE_ROOM, this is the date when the live ended. The value is in YYYY_MM_DD format.
     """

    content_type: str | Unset = UNSET
    cover_img_url: str | Unset = UNSET
    source_url: str | Unset = UNSET
    view_count: str | Unset = UNSET
    like_count: str | Unset = UNSET
    comment_num: str | Unset = UNSET
    paid_order_num: str | Unset = UNSET
    paid_amount: str | Unset = UNSET
    linked_tiktok_video: str | Unset = UNSET
    published_date: datetime.date | Unset = UNSET
    content_end_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        cover_img_url = self.cover_img_url

        source_url = self.source_url

        view_count = self.view_count

        like_count = self.like_count

        comment_num = self.comment_num

        paid_order_num = self.paid_order_num

        paid_amount = self.paid_amount

        linked_tiktok_video = self.linked_tiktok_video

        published_date: str | Unset = UNSET
        if not isinstance(self.published_date, Unset):
            published_date = self.published_date.isoformat()

        content_end_date: None | str | Unset
        if isinstance(self.content_end_date, Unset):
            content_end_date = UNSET
        elif isinstance(self.content_end_date, datetime.date):
            content_end_date = self.content_end_date.isoformat()
        else:
            content_end_date = self.content_end_date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if cover_img_url is not UNSET:
            field_dict["cover_img_url"] = cover_img_url
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if view_count is not UNSET:
            field_dict["view_count"] = view_count
        if like_count is not UNSET:
            field_dict["like_count"] = like_count
        if comment_num is not UNSET:
            field_dict["comment_num"] = comment_num
        if paid_order_num is not UNSET:
            field_dict["paid_order_num"] = paid_order_num
        if paid_amount is not UNSET:
            field_dict["paid_amount"] = paid_amount
        if linked_tiktok_video is not UNSET:
            field_dict["linked_tiktok_video"] = linked_tiktok_video
        if published_date is not UNSET:
            field_dict["published_date"] = published_date
        if content_end_date is not UNSET:
            field_dict["content_end_date"] = content_end_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content_type", UNSET)

        cover_img_url = d.pop("cover_img_url", UNSET)

        source_url = d.pop("source_url", UNSET)

        view_count = d.pop("view_count", UNSET)

        like_count = d.pop("like_count", UNSET)

        comment_num = d.pop("comment_num", UNSET)

        paid_order_num = d.pop("paid_order_num", UNSET)

        paid_amount = d.pop("paid_amount", UNSET)

        linked_tiktok_video = d.pop("linked_tiktok_video", UNSET)

        _published_date = d.pop("published_date", UNSET)
        published_date: datetime.date | Unset
        if isinstance(_published_date,  Unset):
            published_date = UNSET
        else:
            published_date = datetime.date.fromisoformat(_published_date)




        def _parse_content_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                content_end_date_type_0 = datetime.date.fromisoformat(data)



                return content_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        content_end_date = _parse_content_end_date(d.pop("content_end_date", UNSET))


        get_affiliate_campaign_creator_product_content_statistics_response_data_creator_content_statistic = cls(
            content_type=content_type,
            cover_img_url=cover_img_url,
            source_url=source_url,
            view_count=view_count,
            like_count=like_count,
            comment_num=comment_num,
            paid_order_num=paid_order_num,
            paid_amount=paid_amount,
            linked_tiktok_video=linked_tiktok_video,
            published_date=published_date,
            content_end_date=content_end_date,
        )


        get_affiliate_campaign_creator_product_content_statistics_response_data_creator_content_statistic.additional_properties = d
        return get_affiliate_campaign_creator_product_content_statistics_response_data_creator_content_statistic

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
