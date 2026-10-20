from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avatar import Avatar


T = TypeVar("T", bound="GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetailCreatorProfile")


@_attrs_define
class GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetailCreatorProfile:
    """
    Attributes:
        username (str | Unset): The creator's username.
        nickname (str | Unset): The creator's nickname.
        follower_count (int | Unset): Number of followers of the creator.
        avatar (Avatar | Unset):
        creator_open_id (str | Unset): Creator Open ID. [More
            details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
    """

    username: str | Unset = UNSET
    nickname: str | Unset = UNSET
    follower_count: int | Unset = UNSET
    avatar: Avatar | Unset = UNSET
    creator_open_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        nickname = self.nickname

        follower_count = self.follower_count

        avatar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        creator_open_id = self.creator_open_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if follower_count is not UNSET:
            field_dict["follower_count"] = follower_count
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if creator_open_id is not UNSET:
            field_dict["creator_open_id"] = creator_open_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar import Avatar  # noqa: PLC0415

        d = dict(src_dict)
        username = d.pop("username", UNSET)

        nickname = d.pop("nickname", UNSET)

        follower_count = d.pop("follower_count", UNSET)

        _avatar = d.pop("avatar", UNSET)
        avatar: Avatar | Unset
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Avatar.from_dict(_avatar)

        creator_open_id = d.pop("creator_open_id", UNSET)

        get_open_collaboration_creator_content_details_response_data_creator_content_detail_creator_profile = cls(
            username=username,
            nickname=nickname,
            follower_count=follower_count,
            avatar=avatar,
            creator_open_id=creator_open_id,
        )

        get_open_collaboration_creator_content_details_response_data_creator_content_detail_creator_profile.additional_properties = d
        return get_open_collaboration_creator_content_details_response_data_creator_content_detail_creator_profile

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
