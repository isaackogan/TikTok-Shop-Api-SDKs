from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_bestselling_videos_response_data_video_product_info import GetBestsellingVideosResponseDataVideoProductInfo





T = TypeVar("T", bound="GetBestsellingVideosResponseDataVideo")



@_attrs_define
class GetBestsellingVideosResponseDataVideo:
    """ 
        Attributes:
            rank (int | Unset): Gmv rank of the video
            id (str | Unset): Video id
            nick_name (str | Unset): Creator handle
            gmv_range (str | Unset): Gmv range of the video
            views (int | Unset): Accumulative number of video views since the video was published.
            likes (int | Unset): Accumulative number of video likes since the video was published.
            comments (int | Unset): Accumulative number of video comments since the video was published.
            shares (int | Unset): Accumulative number of video shares since the video was published.
            product_infos (list[GetBestsellingVideosResponseDataVideoProductInfo] | Unset): List of product anchors
                associated with the video, including product IDs and product names. Excludes deactivated and sold-out products.
            publish_time (int | Unset): The time when the video was published, as a Unix timestamp in seconds (UTC).
            duration (int | Unset): Duration of the video, in seconds.
     """

    rank: int | Unset = UNSET
    id: str | Unset = UNSET
    nick_name: str | Unset = UNSET
    gmv_range: str | Unset = UNSET
    views: int | Unset = UNSET
    likes: int | Unset = UNSET
    comments: int | Unset = UNSET
    shares: int | Unset = UNSET
    product_infos: list[GetBestsellingVideosResponseDataVideoProductInfo] | Unset = UNSET
    publish_time: int | Unset = UNSET
    duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_bestselling_videos_response_data_video_product_info import GetBestsellingVideosResponseDataVideoProductInfo # noqa: PLC0415
        rank = self.rank

        id = self.id

        nick_name = self.nick_name

        gmv_range = self.gmv_range

        views = self.views

        likes = self.likes

        comments = self.comments

        shares = self.shares

        product_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_infos, Unset):
            product_infos = []
            for product_infos_item_data in self.product_infos:
                product_infos_item = product_infos_item_data.to_dict()
                product_infos.append(product_infos_item)



        publish_time = self.publish_time

        duration = self.duration


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rank is not UNSET:
            field_dict["rank"] = rank
        if id is not UNSET:
            field_dict["id"] = id
        if nick_name is not UNSET:
            field_dict["nick_name"] = nick_name
        if gmv_range is not UNSET:
            field_dict["gmv_range"] = gmv_range
        if views is not UNSET:
            field_dict["views"] = views
        if likes is not UNSET:
            field_dict["likes"] = likes
        if comments is not UNSET:
            field_dict["comments"] = comments
        if shares is not UNSET:
            field_dict["shares"] = shares
        if product_infos is not UNSET:
            field_dict["product_infos"] = product_infos
        if publish_time is not UNSET:
            field_dict["publish_time"] = publish_time
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_bestselling_videos_response_data_video_product_info import GetBestsellingVideosResponseDataVideoProductInfo # noqa: PLC0415
        d = dict(src_dict)
        rank = d.pop("rank", UNSET)

        id = d.pop("id", UNSET)

        nick_name = d.pop("nick_name", UNSET)

        gmv_range = d.pop("gmv_range", UNSET)

        views = d.pop("views", UNSET)

        likes = d.pop("likes", UNSET)

        comments = d.pop("comments", UNSET)

        shares = d.pop("shares", UNSET)

        _product_infos = d.pop("product_infos", UNSET)
        product_infos: list[GetBestsellingVideosResponseDataVideoProductInfo] | Unset = UNSET
        if _product_infos is not UNSET:
            product_infos = []
            for product_infos_item_data in _product_infos:
                product_infos_item = GetBestsellingVideosResponseDataVideoProductInfo.from_dict(product_infos_item_data)



                product_infos.append(product_infos_item)


        publish_time = d.pop("publish_time", UNSET)

        duration = d.pop("duration", UNSET)

        get_bestselling_videos_response_data_video = cls(
            rank=rank,
            id=id,
            nick_name=nick_name,
            gmv_range=gmv_range,
            views=views,
            likes=likes,
            comments=comments,
            shares=shares,
            product_infos=product_infos,
            publish_time=publish_time,
            duration=duration,
        )


        get_bestselling_videos_response_data_video.additional_properties = d
        return get_bestselling_videos_response_data_video

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
