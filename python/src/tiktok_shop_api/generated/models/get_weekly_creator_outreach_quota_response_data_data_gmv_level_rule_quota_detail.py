from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleQuotaDetail")



@_attrs_define
class GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleQuotaDetail:
    """ 
        Attributes:
            creator_levels (list[int] | Unset): Creator tiers covered in the current quota tiering
            quota_period_sum (int | Unset): Period quota num in the current quota tiering
            quota_bonus_sum (int | Unset): Bonus quota num in the current quota tiering, if the seller meet the exposure
                posts percentile threshold, will gain quota bonus
     """

    creator_levels: list[int] | Unset = UNSET
    quota_period_sum: int | Unset = UNSET
    quota_bonus_sum: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        creator_levels: list[int] | Unset = UNSET
        if not isinstance(self.creator_levels, Unset):
            creator_levels = self.creator_levels



        quota_period_sum = self.quota_period_sum

        quota_bonus_sum = self.quota_bonus_sum


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creator_levels is not UNSET:
            field_dict["creator_levels"] = creator_levels
        if quota_period_sum is not UNSET:
            field_dict["quota_period_sum"] = quota_period_sum
        if quota_bonus_sum is not UNSET:
            field_dict["quota_bonus_sum"] = quota_bonus_sum

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_levels = cast(list[int], d.pop("creator_levels", UNSET))


        quota_period_sum = d.pop("quota_period_sum", UNSET)

        quota_bonus_sum = d.pop("quota_bonus_sum", UNSET)

        get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_quota_detail = cls(
            creator_levels=creator_levels,
            quota_period_sum=quota_period_sum,
            quota_bonus_sum=quota_bonus_sum,
        )


        get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_quota_detail.additional_properties = d
        return get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_quota_detail

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
