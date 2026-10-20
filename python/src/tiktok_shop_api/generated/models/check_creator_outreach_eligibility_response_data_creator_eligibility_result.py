from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CheckCreatorOutreachEligibilityResponseDataCreatorEligibilityResult")



@_attrs_define
class CheckCreatorOutreachEligibilityResponseDataCreatorEligibilityResult:
    """ 
        Attributes:
            creator_level (int | Unset): Creator level evaluated by the quota rules.
            creator_open_id (str | Unset): Creator Open ID from the request.
            is_blocked (bool | Unset): Whether a blocking relationship prevents the shop and creator from connecting.
            is_connected (bool | Unset): Whether the shop is already connected with the creator.
            is_creator_follower_count_threshold_met (bool | Unset): Whether the creator meets the follower count threshold
                required for the shop to initiate creator outreach.
            is_creator_level_quota_available (bool | Unset): Whether outreach quota is available for the creator's level.
            is_paired (bool | Unset): Whether the shop is paired with the creator.
     """

    creator_level: int | Unset = UNSET
    creator_open_id: str | Unset = UNSET
    is_blocked: bool | Unset = UNSET
    is_connected: bool | Unset = UNSET
    is_creator_follower_count_threshold_met: bool | Unset = UNSET
    is_creator_level_quota_available: bool | Unset = UNSET
    is_paired: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        creator_level = self.creator_level

        creator_open_id = self.creator_open_id

        is_blocked = self.is_blocked

        is_connected = self.is_connected

        is_creator_follower_count_threshold_met = self.is_creator_follower_count_threshold_met

        is_creator_level_quota_available = self.is_creator_level_quota_available

        is_paired = self.is_paired


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creator_level is not UNSET:
            field_dict["creator_level"] = creator_level
        if creator_open_id is not UNSET:
            field_dict["creator_open_id"] = creator_open_id
        if is_blocked is not UNSET:
            field_dict["is_blocked"] = is_blocked
        if is_connected is not UNSET:
            field_dict["is_connected"] = is_connected
        if is_creator_follower_count_threshold_met is not UNSET:
            field_dict["is_creator_follower_count_threshold_met"] = is_creator_follower_count_threshold_met
        if is_creator_level_quota_available is not UNSET:
            field_dict["is_creator_level_quota_available"] = is_creator_level_quota_available
        if is_paired is not UNSET:
            field_dict["is_paired"] = is_paired

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_level = d.pop("creator_level", UNSET)

        creator_open_id = d.pop("creator_open_id", UNSET)

        is_blocked = d.pop("is_blocked", UNSET)

        is_connected = d.pop("is_connected", UNSET)

        is_creator_follower_count_threshold_met = d.pop("is_creator_follower_count_threshold_met", UNSET)

        is_creator_level_quota_available = d.pop("is_creator_level_quota_available", UNSET)

        is_paired = d.pop("is_paired", UNSET)

        check_creator_outreach_eligibility_response_data_creator_eligibility_result = cls(
            creator_level=creator_level,
            creator_open_id=creator_open_id,
            is_blocked=is_blocked,
            is_connected=is_connected,
            is_creator_follower_count_threshold_met=is_creator_follower_count_threshold_met,
            is_creator_level_quota_available=is_creator_level_quota_available,
            is_paired=is_paired,
        )


        check_creator_outreach_eligibility_response_data_creator_eligibility_result.additional_properties = d
        return check_creator_outreach_eligibility_response_data_creator_eligibility_result

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
