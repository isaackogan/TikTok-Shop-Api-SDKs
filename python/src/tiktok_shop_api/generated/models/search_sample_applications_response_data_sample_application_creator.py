from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gmv import Gmv


T = TypeVar("T", bound="SearchSampleApplicationsResponseDataSampleApplicationCreator")


@_attrs_define
class SearchSampleApplicationsResponseDataSampleApplicationCreator:
    """
    Attributes:
        creator_open_id (str | Unset): Creator Open ID. [More
            details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
        username (str | Unset): TikTok User Name of a creator
        nickname (str | Unset): TikTok Nick Name of a creator
        follower_count (int | Unset): The number of creator's followers
        avatar_url (str | Unset): The URL of the creator's avatar image
        gmv (Gmv | Unset):
        content_count (int | Unset): The number of contents a creator has posted in the last 30 days. It is formatted as
            an integer. If the creator has not authorized the sharing of this information, the field returns an empty
            string.
        fulfillment_percentage (str | Unset): The creator's sample fulfillment rate over the past 90 days, returned as a
            percentage string with no percent sign (for example, `60.85`). If the creator has not authorized disclosure of
            this information, the field returns an empty string.
        ec_video_view (int | Unset): The median number of creators' shoppable video views over the past 30 days. If the
            creator has not authorized the sharing of this information, the field returns an empty string.
    """

    creator_open_id: str | Unset = UNSET
    username: str | Unset = UNSET
    nickname: str | Unset = UNSET
    follower_count: int | Unset = UNSET
    avatar_url: str | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    content_count: int | Unset = UNSET
    fulfillment_percentage: str | Unset = UNSET
    ec_video_view: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator_open_id = self.creator_open_id

        username = self.username

        nickname = self.nickname

        follower_count = self.follower_count

        avatar_url = self.avatar_url

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        content_count = self.content_count

        fulfillment_percentage = self.fulfillment_percentage

        ec_video_view = self.ec_video_view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator_open_id is not UNSET:
            field_dict["creator_open_id"] = creator_open_id
        if username is not UNSET:
            field_dict["username"] = username
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if content_count is not UNSET:
            field_dict["content_count"] = content_count
        if fulfillment_percentage is not UNSET:
            field_dict["fulfillment_percentage"] = fulfillment_percentage
        if ec_video_view is not UNSET:
            field_dict["ec_video_view"] = ec_video_view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv  # noqa: PLC0415

        d = dict(src_dict)
        creator_open_id = d.pop("creator_open_id", UNSET)

        username = d.pop("username", UNSET)

        nickname = d.pop("nickname", UNSET)

        follower_count = d.pop("follower_count", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv, Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)

        content_count = d.pop("content_count", UNSET)

        fulfillment_percentage = d.pop("fulfillment_percentage", UNSET)

        ec_video_view = d.pop("ec_video_view", UNSET)

        search_sample_applications_response_data_sample_application_creator = cls(
            creator_open_id=creator_open_id,
            username=username,
            nickname=nickname,
            follower_count=follower_count,
            avatar_url=avatar_url,
            gmv=gmv,
            content_count=content_count,
            fulfillment_percentage=fulfillment_percentage,
            ec_video_view=ec_video_view,
        )

        search_sample_applications_response_data_sample_application_creator.additional_properties = d
        return search_sample_applications_response_data_sample_application_creator

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
