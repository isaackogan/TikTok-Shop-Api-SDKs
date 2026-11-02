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
  from ..models.get_acc_audience_preference_summary_response_data_channel_summary_video_top_item_video_info import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItemVideoInfo
  from ..models.linked_product import LinkedProduct
  from ..models.stat import Stat





T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItem")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItem:
    """ 
        Attributes:
            linked_products (list[LinkedProduct] | Unset): Products linked to the video, when provided.
            publish_time (datetime.date | Unset): Publication date of the video, in YYYY-MM-DD format (UTC).
            seller_own_avatar_url (str | Unset): URL of the content author's avatar.
            seller_own_id (str | Unset): ID of the content author.
            seller_own_name (str | Unset): Display name of the content author.
            stats (Stat | Unset):
            video_cover_url (str | Unset): URL of the video cover image.
            video_id (str | Unset): ID of the video.
            video_infos (list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItemVideoInfo] | Unset):
                Available video file representations and their playback metadata.
            video_title (str | Unset): Title of the video.
     """

    linked_products: list[LinkedProduct] | Unset = UNSET
    publish_time: datetime.date | Unset = UNSET
    seller_own_avatar_url: str | Unset = UNSET
    seller_own_id: str | Unset = UNSET
    seller_own_name: str | Unset = UNSET
    stats: Stat | Unset = UNSET
    video_cover_url: str | Unset = UNSET
    video_id: str | Unset = UNSET
    video_infos: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItemVideoInfo] | Unset = UNSET
    video_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_video_top_item_video_info import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItemVideoInfo # noqa: PLC0415
        from ..models.linked_product import LinkedProduct # noqa: PLC0415
        from ..models.stat import Stat # noqa: PLC0415
        linked_products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_products, Unset):
            linked_products = []
            for linked_products_item_data in self.linked_products:
                linked_products_item = linked_products_item_data.to_dict()
                linked_products.append(linked_products_item)



        publish_time: str | Unset = UNSET
        if not isinstance(self.publish_time, Unset):
            publish_time = self.publish_time.isoformat()

        seller_own_avatar_url = self.seller_own_avatar_url

        seller_own_id = self.seller_own_id

        seller_own_name = self.seller_own_name

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        video_cover_url = self.video_cover_url

        video_id = self.video_id

        video_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.video_infos, Unset):
            video_infos = []
            for video_infos_item_data in self.video_infos:
                video_infos_item = video_infos_item_data.to_dict()
                video_infos.append(video_infos_item)



        video_title = self.video_title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if linked_products is not UNSET:
            field_dict["linked_products"] = linked_products
        if publish_time is not UNSET:
            field_dict["publish_time"] = publish_time
        if seller_own_avatar_url is not UNSET:
            field_dict["seller_own_avatar_url"] = seller_own_avatar_url
        if seller_own_id is not UNSET:
            field_dict["seller_own_id"] = seller_own_id
        if seller_own_name is not UNSET:
            field_dict["seller_own_name"] = seller_own_name
        if stats is not UNSET:
            field_dict["stats"] = stats
        if video_cover_url is not UNSET:
            field_dict["video_cover_url"] = video_cover_url
        if video_id is not UNSET:
            field_dict["video_id"] = video_id
        if video_infos is not UNSET:
            field_dict["video_infos"] = video_infos
        if video_title is not UNSET:
            field_dict["video_title"] = video_title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary_video_top_item_video_info import GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItemVideoInfo # noqa: PLC0415
        from ..models.linked_product import LinkedProduct # noqa: PLC0415
        from ..models.stat import Stat # noqa: PLC0415
        d = dict(src_dict)
        _linked_products = d.pop("linked_products", UNSET)
        linked_products: list[LinkedProduct] | Unset = UNSET
        if _linked_products is not UNSET:
            linked_products = []
            for linked_products_item_data in _linked_products:
                linked_products_item = LinkedProduct.from_dict(linked_products_item_data)



                linked_products.append(linked_products_item)


        _publish_time = d.pop("publish_time", UNSET)
        publish_time: datetime.date | Unset
        if isinstance(_publish_time,  Unset):
            publish_time = UNSET
        else:
            publish_time = datetime.date.fromisoformat(_publish_time)




        seller_own_avatar_url = d.pop("seller_own_avatar_url", UNSET)

        seller_own_id = d.pop("seller_own_id", UNSET)

        seller_own_name = d.pop("seller_own_name", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Stat | Unset
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = Stat.from_dict(_stats)




        video_cover_url = d.pop("video_cover_url", UNSET)

        video_id = d.pop("video_id", UNSET)

        _video_infos = d.pop("video_infos", UNSET)
        video_infos: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItemVideoInfo] | Unset = UNSET
        if _video_infos is not UNSET:
            video_infos = []
            for video_infos_item_data in _video_infos:
                video_infos_item = GetACCAudiencePreferenceSummaryResponseDataChannelSummaryVideoTopItemVideoInfo.from_dict(video_infos_item_data)



                video_infos.append(video_infos_item)


        video_title = d.pop("video_title", UNSET)

        get_acc_audience_preference_summary_response_data_channel_summary_video_top_item = cls(
            linked_products=linked_products,
            publish_time=publish_time,
            seller_own_avatar_url=seller_own_avatar_url,
            seller_own_id=seller_own_id,
            seller_own_name=seller_own_name,
            stats=stats,
            video_cover_url=video_cover_url,
            video_id=video_id,
            video_infos=video_infos,
            video_title=video_title,
        )


        get_acc_audience_preference_summary_response_data_channel_summary_video_top_item.additional_properties = d
        return get_acc_audience_preference_summary_response_data_channel_summary_video_top_item

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
