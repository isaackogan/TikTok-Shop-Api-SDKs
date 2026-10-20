from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetConversationResponseDataConversationParticipant")



@_attrs_define
class GetConversationResponseDataConversationParticipant:
    """ 
        Attributes:
            im_user_id (str | Unset): Participant's ID, in IM system. This ID is used in IM system and can not be used to
                query orders. To query orders, use `user_id` instead.
            role (str | Unset): Participant's role.
                Possible enumerations:
                - `BUYER`
                - `SHOP`
                - `CUSTOMER_SERVICE`
            nickname (str | Unset): Participant's nickname.
            avatar (str | Unset): Participant's avatar URL.
            user_id (str | Unset): Participant's ID.
            platform (str | Unset): Platform the buyer is from.
                This field is returned only when the participant role is `BUYER` and the shop region is Indonesia. Possible
                values:
                - `TIKTOK_SHOP`
                - `TOKOPEDIA`
                You cannot send platform-specific content to a buyer from another platform. For example, when sending a product
                card to a Tokopedia buyer, ensure that the product is listed on Tokopedia.
     """

    im_user_id: str | Unset = UNSET
    role: str | Unset = UNSET
    nickname: str | Unset = UNSET
    avatar: str | Unset = UNSET
    user_id: str | Unset = UNSET
    platform: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        im_user_id = self.im_user_id

        role = self.role

        nickname = self.nickname

        avatar = self.avatar

        user_id = self.user_id

        platform = self.platform


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
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        im_user_id = d.pop("im_user_id", UNSET)

        role = d.pop("role", UNSET)

        nickname = d.pop("nickname", UNSET)

        avatar = d.pop("avatar", UNSET)

        user_id = d.pop("user_id", UNSET)

        platform = d.pop("platform", UNSET)

        get_conversation_response_data_conversation_participant = cls(
            im_user_id=im_user_id,
            role=role,
            nickname=nickname,
            avatar=avatar,
            user_id=user_id,
            platform=platform,
        )


        get_conversation_response_data_conversation_participant.additional_properties = d
        return get_conversation_response_data_conversation_participant

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
