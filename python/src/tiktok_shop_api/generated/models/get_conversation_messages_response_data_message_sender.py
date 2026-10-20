from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetConversationMessagesResponseDataMessageSender")



@_attrs_define
class GetConversationMessagesResponseDataMessageSender:
    """ 
        Attributes:
            im_user_id (str | Unset): Sender's ID.
                These are IM IDs, and can not be used to query orders.
            role (str | Unset): Sender's role. Possible enumerations:
                - `BUYER`
                - `SHOP`
                - `CUSTOMER_SERVICE`
                - `SYSTEM`
                - `ROBOT`
                For `SYSTEM` and `ROBOT` role, the value of `im_user_id`, `nickname`, and `avatar` are the same as those of the
                `SHOP` role.
            nickname (str | Unset): Sender's nickname.
                - For shops, the nickname is the shop's name.
                - For customer service, the nickname is the customer service's name.
                - For buyers, the nickname is the buyer's nickname on TikTok.
                You can set the nicknames for shops and customer service agents on Seller Center.
            avatar (str | Unset): Sender's avatar URL.
     """

    im_user_id: str | Unset = UNSET
    role: str | Unset = UNSET
    nickname: str | Unset = UNSET
    avatar: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        im_user_id = self.im_user_id

        role = self.role

        nickname = self.nickname

        avatar = self.avatar


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if im_user_id is not UNSET:
            field_dict["im_user_id"] = im_user_id
        if role is not UNSET:
            field_dict["role"] = role
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        im_user_id = d.pop("im_user_id", UNSET)

        role = d.pop("role", UNSET)

        nickname = d.pop("nickname", UNSET)

        avatar = d.pop("avatar", UNSET)

        get_conversation_messages_response_data_message_sender = cls(
            im_user_id=im_user_id,
            role=role,
            nickname=nickname,
            avatar=avatar,
        )


        get_conversation_messages_response_data_message_sender.additional_properties = d
        return get_conversation_messages_response_data_message_sender

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
