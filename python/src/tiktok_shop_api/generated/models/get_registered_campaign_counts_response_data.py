from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetRegisteredCampaignCountsResponseData")



@_attrs_define
class GetRegisteredCampaignCountsResponseData:
    """ 
        Attributes:
            active_count (int | Unset): Number of campaigns in the current statistics scope with CampaignStatus.ACTIVE,
                covering registration, the wait for execution, and execution itself. Not limited to campaigns currently
                executing and does not establish that benefits are effective for the shop.
            all_count (int | Unset): Total campaigns in the current statistics scope. Not a count of campaign groups,
                products, registration records, or livestream sessions.
            ended_count (int | Unset): Number of ended or no longer effective campaigns in the current statistics scope,
                including deactivated campaigns counted as ended.
            upcoming_count (int | Unset): Number of campaigns in the current statistics scope whose registration has not
                started, corresponding to CampaignStatus.UPCOMING.
     """

    active_count: int | Unset = UNSET
    all_count: int | Unset = UNSET
    ended_count: int | Unset = UNSET
    upcoming_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        active_count = self.active_count

        all_count = self.all_count

        ended_count = self.ended_count

        upcoming_count = self.upcoming_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if active_count is not UNSET:
            field_dict["active_count"] = active_count
        if all_count is not UNSET:
            field_dict["all_count"] = all_count
        if ended_count is not UNSET:
            field_dict["ended_count"] = ended_count
        if upcoming_count is not UNSET:
            field_dict["upcoming_count"] = upcoming_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_count = d.pop("active_count", UNSET)

        all_count = d.pop("all_count", UNSET)

        ended_count = d.pop("ended_count", UNSET)

        upcoming_count = d.pop("upcoming_count", UNSET)

        get_registered_campaign_counts_response_data = cls(
            active_count=active_count,
            all_count=all_count,
            ended_count=ended_count,
            upcoming_count=upcoming_count,
        )


        get_registered_campaign_counts_response_data.additional_properties = d
        return get_registered_campaign_counts_response_data

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
