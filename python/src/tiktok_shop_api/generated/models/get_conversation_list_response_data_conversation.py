from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetConversationListResponseDataConversation")


@_attrs_define
class GetConversationListResponseDataConversation:
    """
    Attributes:
        id (str | Unset): Conversation unique ID.
        unread_count (int | Unset): Number of unread messages.
        username (str | Unset): The TikTok user name.
        avatar (str | Unset): The URL for the TikTok creator's avatar image file.
        creator_im_id (str | Unset): Creators' IM User ID.
    """

    id: str | Unset = UNSET
    unread_count: int | Unset = UNSET
    username: str | Unset = UNSET
    avatar: str | Unset = UNSET
    creator_im_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        unread_count = self.unread_count

        username = self.username

        avatar = self.avatar

        creator_im_id = self.creator_im_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count
        if username is not UNSET:
            field_dict["username"] = username
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if creator_im_id is not UNSET:
            field_dict["creator_im_id"] = creator_im_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        unread_count = d.pop("unread_count", UNSET)

        username = d.pop("username", UNSET)

        avatar = d.pop("avatar", UNSET)

        creator_im_id = d.pop("creator_im_id", UNSET)

        get_conversation_list_response_data_conversation = cls(
            id=id,
            unread_count=unread_count,
            username=username,
            avatar=avatar,
            creator_im_id=creator_im_id,
        )

        get_conversation_list_response_data_conversation.additional_properties = d
        return get_conversation_list_response_data_conversation

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
