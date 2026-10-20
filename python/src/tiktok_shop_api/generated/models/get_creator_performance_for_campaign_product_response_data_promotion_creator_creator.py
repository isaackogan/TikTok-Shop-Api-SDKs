from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorCreator")



@_attrs_define
class GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorCreator:
    """ 
        Attributes:
            nick_name (str | Unset): The TikTok nickname of the creator.
            avatar_url (str | Unset): A URL for the creator's avatar image in the TikTok CDN.
            follower_num (int | Unset): The total count of TikTok followers for the creator.
            user_name (str | Unset): The TikTok username of the creator.
            creator_open_id (str | Unset): Creator Open ID. More details:https://partner.tiktokshop.com/docv2/page/3obfokj6
     """

    nick_name: str | Unset = UNSET
    avatar_url: str | Unset = UNSET
    follower_num: int | Unset = UNSET
    user_name: str | Unset = UNSET
    creator_open_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        nick_name = self.nick_name

        avatar_url = self.avatar_url

        follower_num = self.follower_num

        user_name = self.user_name

        creator_open_id = self.creator_open_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if nick_name is not UNSET:
            field_dict["nick_name"] = nick_name
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if follower_num is not UNSET:
            field_dict["follower_num"] = follower_num
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if creator_open_id is not UNSET:
            field_dict["creator_open_id"] = creator_open_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nick_name = d.pop("nick_name", UNSET)

        avatar_url = d.pop("avatar_url", UNSET)

        follower_num = d.pop("follower_num", UNSET)

        user_name = d.pop("user_name", UNSET)

        creator_open_id = d.pop("creator_open_id", UNSET)

        get_creator_performance_for_campaign_product_response_data_promotion_creator_creator = cls(
            nick_name=nick_name,
            avatar_url=avatar_url,
            follower_num=follower_num,
            user_name=user_name,
            creator_open_id=creator_open_id,
        )


        get_creator_performance_for_campaign_product_response_data_promotion_creator_creator.additional_properties = d
        return get_creator_performance_for_campaign_product_response_data_promotion_creator_creator

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
