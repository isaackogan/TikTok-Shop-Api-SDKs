from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetConversationsResponseDataConversationParticipant")


@_attrs_define
class GetConversationsResponseDataConversationParticipant:
    """
    Attributes:
        im_user_id (str | Unset): Participant's ID, in IM system. This ID is used in IM system and can not be used to
            query orders. To query orders, use `user_id` instead.
        avatar (str | Unset): Participant's avatar URL.
        user_id (str | Unset): Participant's ID.
        role (str | Unset): Participant's role.
            Possible enumerations:
            - `BUYER`
            - `SHOP`
            - `CUSTOMER_SERVICE`
        nickname (str | Unset): Participant's nickname.
        buyer_platform (str | Unset): Which platform is the buyer from.
            This field will only be returned when the participant's `role` is `BUYER` and the shop's region is Indonesia.
            Possible enumerations:
            - TIKTOK_SHOP
            - TOKOPEDIA
            You cannot send platform-specific content to the buyer from a different platform. For example, when you send a
            product card to the Tokopedia buyer, you must ensure the product is listed on Tokopedia.
    """

    im_user_id: str | Unset = UNSET
    avatar: str | Unset = UNSET
    user_id: str | Unset = UNSET
    role: str | Unset = UNSET
    nickname: str | Unset = UNSET
    buyer_platform: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        im_user_id = self.im_user_id

        avatar = self.avatar

        user_id = self.user_id

        role = self.role

        nickname = self.nickname

        buyer_platform = self.buyer_platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if im_user_id is not UNSET:
            field_dict["im_user_id"] = im_user_id
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if role is not UNSET:
            field_dict["role"] = role
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if buyer_platform is not UNSET:
            field_dict["buyer_platform"] = buyer_platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        im_user_id = d.pop("im_user_id", UNSET)

        avatar = d.pop("avatar", UNSET)

        user_id = d.pop("user_id", UNSET)

        role = d.pop("role", UNSET)

        nickname = d.pop("nickname", UNSET)

        buyer_platform = d.pop("buyer_platform", UNSET)

        get_conversations_response_data_conversation_participant = cls(
            im_user_id=im_user_id,
            avatar=avatar,
            user_id=user_id,
            role=role,
            nickname=nickname,
            buyer_platform=buyer_platform,
        )

        get_conversations_response_data_conversation_participant.additional_properties = d
        return get_conversations_response_data_conversation_participant

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
