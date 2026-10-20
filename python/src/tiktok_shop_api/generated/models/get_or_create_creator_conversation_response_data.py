from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetOrCreateCreatorConversationResponseData")



@_attrs_define
class GetOrCreateCreatorConversationResponseData:
    """ 
        Attributes:
            conversation_id (str | Unset): The unique ID of the conversation.
            is_new (bool | Unset): Whether this is a new conversation.
            username (str | Unset): The TikTok creator's username.
            avatar (str | Unset): The URL for the TikTok creator's avatar image file.
            unread_count (int | Unset): Number of messages unread by the shop.
            creator_im_id (str | Unset): Creators' IM User ID.
     """

    conversation_id: str | Unset = UNSET
    is_new: bool | Unset = UNSET
    username: str | Unset = UNSET
    avatar: str | Unset = UNSET
    unread_count: int | Unset = UNSET
    creator_im_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        is_new = self.is_new

        username = self.username

        avatar = self.avatar

        unread_count = self.unread_count

        creator_im_id = self.creator_im_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if is_new is not UNSET:
            field_dict["is_new"] = is_new
        if username is not UNSET:
            field_dict["username"] = username
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count
        if creator_im_id is not UNSET:
            field_dict["creator_im_id"] = creator_im_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversation_id", UNSET)

        is_new = d.pop("is_new", UNSET)

        username = d.pop("username", UNSET)

        avatar = d.pop("avatar", UNSET)

        unread_count = d.pop("unread_count", UNSET)

        creator_im_id = d.pop("creator_im_id", UNSET)

        get_or_create_creator_conversation_response_data = cls(
            conversation_id=conversation_id,
            is_new=is_new,
            username=username,
            avatar=avatar,
            unread_count=unread_count,
            creator_im_id=creator_im_id,
        )


        get_or_create_creator_conversation_response_data.additional_properties = d
        return get_or_create_creator_conversation_response_data

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
