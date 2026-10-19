from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avatar import Avatar


T = TypeVar("T", bound="QueryTargetCollaborationDetailResponseDataTargetCollaborationCreator")


@_attrs_define
class QueryTargetCollaborationDetailResponseDataTargetCollaborationCreator:
    """
    Attributes:
        username (str | Unset): The TikTok user name.
        nickname (str | Unset): The TikTok nick name.
        avatar (Avatar | Unset):
        selection_region (str | Unset): The regions in which the creator is eligible to promote products in showcases,
            videos, and live streams.
        showcase_product_count (int | Unset): This field indicates the number of products creator has added  to the
            showcase from target collaboration.
            The count includes NORMAL and DELETING states.
        content_product_count (int | Unset): This field indicates the number of products creator has posted video or
            live from target collaboration.
            The count includes NORMAL and DELETING states.
        collaboration_status (str | Unset): The status of the creator in the current target cooperation.
            Field values:
            - NORMAL: The status of the creator in the current target collaboration is normal.
            - DELETING: The status of the creator in the current target collaboration is deleting.The creator's product
            promotion relationship in the DELETING status will end the delayed effectiveness status and flow to the DELETED
            status at 00:00 the next day.
            - DELETED: The status of the creator in the current target collaboration is deleted.
        product_effective_status (str | Unset): The effectiveness of the target collaboration's product commissions for
            this creator.
            Field values:
            - EFFECTIVE_ALL: The commission is effective for this creator on all products in the target collaboration.
            - EFFECTIVE_PARTIALLY: The commission is effective for this creator on some products in the target
            collaboration.
            - EFFECTIVE_NONE: The commission is not effective for this creator on any products in the target collaboration.
            Normally, the commission rate for all products under Target Collaboration is effective.
            If the merchant participates in TOP_CREATOR_PROGRAM, and TOP_CREATOR_PROGRAM includes the current creator and
            some products, the commission rate will be based on TOP_CREATOR_PROGRAM. The products' commission under the
            current Target Collaboration will only be partially effective for the creator, corresponding to
            EFFECTIVE_PARTIALLY status.
        creator_open_id (str | Unset): Creator Open ID. [More
            details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
    """

    username: str | Unset = UNSET
    nickname: str | Unset = UNSET
    avatar: Avatar | Unset = UNSET
    selection_region: str | Unset = UNSET
    showcase_product_count: int | Unset = UNSET
    content_product_count: int | Unset = UNSET
    collaboration_status: str | Unset = UNSET
    product_effective_status: str | Unset = UNSET
    creator_open_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        nickname = self.nickname

        avatar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        selection_region = self.selection_region

        showcase_product_count = self.showcase_product_count

        content_product_count = self.content_product_count

        collaboration_status = self.collaboration_status

        product_effective_status = self.product_effective_status

        creator_open_id = self.creator_open_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if selection_region is not UNSET:
            field_dict["selection_region"] = selection_region
        if showcase_product_count is not UNSET:
            field_dict["showcase_product_count"] = showcase_product_count
        if content_product_count is not UNSET:
            field_dict["content_product_count"] = content_product_count
        if collaboration_status is not UNSET:
            field_dict["collaboration_status"] = collaboration_status
        if product_effective_status is not UNSET:
            field_dict["product_effective_status"] = product_effective_status
        if creator_open_id is not UNSET:
            field_dict["creator_open_id"] = creator_open_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avatar import Avatar  # noqa: PLC0415

        d = dict(src_dict)
        username = d.pop("username", UNSET)

        nickname = d.pop("nickname", UNSET)

        _avatar = d.pop("avatar", UNSET)
        avatar: Avatar | Unset
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = Avatar.from_dict(_avatar)

        selection_region = d.pop("selection_region", UNSET)

        showcase_product_count = d.pop("showcase_product_count", UNSET)

        content_product_count = d.pop("content_product_count", UNSET)

        collaboration_status = d.pop("collaboration_status", UNSET)

        product_effective_status = d.pop("product_effective_status", UNSET)

        creator_open_id = d.pop("creator_open_id", UNSET)

        query_target_collaboration_detail_response_data_target_collaboration_creator = cls(
            username=username,
            nickname=nickname,
            avatar=avatar,
            selection_region=selection_region,
            showcase_product_count=showcase_product_count,
            content_product_count=content_product_count,
            collaboration_status=collaboration_status,
            product_effective_status=product_effective_status,
            creator_open_id=creator_open_id,
        )

        query_target_collaboration_detail_response_data_target_collaboration_creator.additional_properties = d
        return query_target_collaboration_detail_response_data_target_collaboration_creator

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
