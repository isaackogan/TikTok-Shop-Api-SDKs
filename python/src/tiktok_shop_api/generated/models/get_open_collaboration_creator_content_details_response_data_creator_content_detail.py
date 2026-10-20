from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_open_collaboration_creator_content_details_response_data_creator_content_detail_creator_profile import GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetailCreatorProfile





T = TypeVar("T", bound="GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetail")



@_attrs_define
class GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetail:
    """ 
        Attributes:
            creator_profile (GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetailCreatorProfile |
                Unset):
            video_count (int | Unset): This field indicates the number of videos posted by the creator.
            live_count (int | Unset): This field indicates the number of lives posted by the creator.
            promotion_status (str | Unset): Promotion status of the creator.
                Field values:
                - NORMAL: When the creator is promoting normally, it returns to NORMAL status
                - TERMINATING:When the creator is asked by the merchant to terminate the promotion, the status will return to
                TERMINATING, indicating that the creator's promotion rights will expire soon.
            promotion_end_time (int | Unset): End time of creator promotion.
     """

    creator_profile: GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetailCreatorProfile | Unset = UNSET
    video_count: int | Unset = UNSET
    live_count: int | Unset = UNSET
    promotion_status: str | Unset = UNSET
    promotion_end_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_open_collaboration_creator_content_details_response_data_creator_content_detail_creator_profile import GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetailCreatorProfile # noqa: PLC0415
        creator_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_profile, Unset):
            creator_profile = self.creator_profile.to_dict()

        video_count = self.video_count

        live_count = self.live_count

        promotion_status = self.promotion_status

        promotion_end_time = self.promotion_end_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creator_profile is not UNSET:
            field_dict["creator_profile"] = creator_profile
        if video_count is not UNSET:
            field_dict["video_count"] = video_count
        if live_count is not UNSET:
            field_dict["live_count"] = live_count
        if promotion_status is not UNSET:
            field_dict["promotion_status"] = promotion_status
        if promotion_end_time is not UNSET:
            field_dict["promotion_end_time"] = promotion_end_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_open_collaboration_creator_content_details_response_data_creator_content_detail_creator_profile import GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetailCreatorProfile # noqa: PLC0415
        d = dict(src_dict)
        _creator_profile = d.pop("creator_profile", UNSET)
        creator_profile: GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetailCreatorProfile | Unset
        if isinstance(_creator_profile,  Unset):
            creator_profile = UNSET
        else:
            creator_profile = GetOpenCollaborationCreatorContentDetailsResponseDataCreatorContentDetailCreatorProfile.from_dict(_creator_profile)




        video_count = d.pop("video_count", UNSET)

        live_count = d.pop("live_count", UNSET)

        promotion_status = d.pop("promotion_status", UNSET)

        promotion_end_time = d.pop("promotion_end_time", UNSET)

        get_open_collaboration_creator_content_details_response_data_creator_content_detail = cls(
            creator_profile=creator_profile,
            video_count=video_count,
            live_count=live_count,
            promotion_status=promotion_status,
            promotion_end_time=promotion_end_time,
        )


        get_open_collaboration_creator_content_details_response_data_creator_content_detail.additional_properties = d
        return get_open_collaboration_creator_content_details_response_data_creator_content_detail

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
