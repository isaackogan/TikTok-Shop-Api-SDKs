from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_creator_profile_response_data_avatar import GetCreatorProfileResponseDataAvatar


T = TypeVar("T", bound="GetCreatorProfileResponseData")


@_attrs_define
class GetCreatorProfileResponseData:
    """
    Attributes:
        avatar (GetCreatorProfileResponseDataAvatar | Unset):
        username (str | Unset): The TikTok user name.
        selection_region (str | Unset): The region in which the creator is eligible to promote products in showcases,
            videos, and live streams.
        register_region (str | Unset): The region in which the creator's TikTok account is registered.
        seller_type (str | Unset): If the creator is also also has a TikTok Shop seller account, the seller type of the
            creator. This is an enumerated type with values:
            - CROSS_BORDER
            - LOCAL
        permissions (list[str] | Unset): A list of product promotion permissions for the creator. The list can include
            zero or more of the following permissions:
            - LIVE_STREAM_PERMISSION
            - SELF_SALE_PERMISSION
            - ADD_AFFILIATE_PERMISSION
            - PHOTO_SHOPPABLE_PERMISSION_PRODUCT
            - PHOTO_SHOPPABLE_PERMISSION_SHOP
        user_type (str | Unset): The creator's user type. This is an enumerated type with values:
            - TIKTOK_SHOP_OFFICIAL_ACCOUNT
            - TIKTOK_MARKETING_ACCOUNT
            - TIKTOK_SHOP_CREATOR
        creator_user_open_id (str | Unset): Creator Open ID. [More
            details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
    """

    avatar: GetCreatorProfileResponseDataAvatar | Unset = UNSET
    username: str | Unset = UNSET
    selection_region: str | Unset = UNSET
    register_region: str | Unset = UNSET
    seller_type: str | Unset = UNSET
    permissions: list[str] | Unset = UNSET
    user_type: str | Unset = UNSET
    creator_user_open_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avatar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        username = self.username

        selection_region = self.selection_region

        register_region = self.register_region

        seller_type = self.seller_type

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        user_type = self.user_type

        creator_user_open_id = self.creator_user_open_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if username is not UNSET:
            field_dict["username"] = username
        if selection_region is not UNSET:
            field_dict["selection_region"] = selection_region
        if register_region is not UNSET:
            field_dict["register_region"] = register_region
        if seller_type is not UNSET:
            field_dict["seller_type"] = seller_type
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if user_type is not UNSET:
            field_dict["user_type"] = user_type
        if creator_user_open_id is not UNSET:
            field_dict["creator_user_open_id"] = creator_user_open_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_profile_response_data_avatar import (
            GetCreatorProfileResponseDataAvatar,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _avatar = d.pop("avatar", UNSET)
        avatar: GetCreatorProfileResponseDataAvatar | Unset
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = GetCreatorProfileResponseDataAvatar.from_dict(_avatar)

        username = d.pop("username", UNSET)

        selection_region = d.pop("selection_region", UNSET)

        register_region = d.pop("register_region", UNSET)

        seller_type = d.pop("seller_type", UNSET)

        permissions = cast(list[str], d.pop("permissions", UNSET))

        user_type = d.pop("user_type", UNSET)

        creator_user_open_id = d.pop("creator_user_open_id", UNSET)

        get_creator_profile_response_data = cls(
            avatar=avatar,
            username=username,
            selection_region=selection_region,
            register_region=register_region,
            seller_type=seller_type,
            permissions=permissions,
            user_type=user_type,
            creator_user_open_id=creator_user_open_id,
        )

        get_creator_profile_response_data.additional_properties = d
        return get_creator_profile_response_data

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
