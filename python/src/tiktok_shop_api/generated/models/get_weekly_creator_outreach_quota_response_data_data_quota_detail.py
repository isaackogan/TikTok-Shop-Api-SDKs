from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWeeklyCreatorOutreachQuotaResponseDataDataQuotaDetail")


@_attrs_define
class GetWeeklyCreatorOutreachQuotaResponseDataDataQuotaDetail:
    """
    Attributes:
        creator_levels (list[int] | Unset): Creator tiers covered in the current quota tiering
        quota_period_sum (int | Unset): Period quota num in the current quota tiering
        quota_period_use (int | Unset): Period quota use in the current quota tiering
        quota_bonus_sum (int | Unset): Bonus quota num in the current quota tiering, if the seller meet the exposure
            posts percentile threshold, will gain quota bonus
        quota_bonus_use (int | Unset): Bonus quota use in the current quota tiering, bonus will be consume first.
    """

    creator_levels: list[int] | Unset = UNSET
    quota_period_sum: int | Unset = UNSET
    quota_period_use: int | Unset = UNSET
    quota_bonus_sum: int | Unset = UNSET
    quota_bonus_use: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator_levels: list[int] | Unset = UNSET
        if not isinstance(self.creator_levels, Unset):
            creator_levels = self.creator_levels

        quota_period_sum = self.quota_period_sum

        quota_period_use = self.quota_period_use

        quota_bonus_sum = self.quota_bonus_sum

        quota_bonus_use = self.quota_bonus_use

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator_levels is not UNSET:
            field_dict["creator_levels"] = creator_levels
        if quota_period_sum is not UNSET:
            field_dict["quota_period_sum"] = quota_period_sum
        if quota_period_use is not UNSET:
            field_dict["quota_period_use"] = quota_period_use
        if quota_bonus_sum is not UNSET:
            field_dict["quota_bonus_sum"] = quota_bonus_sum
        if quota_bonus_use is not UNSET:
            field_dict["quota_bonus_use"] = quota_bonus_use

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_levels = cast(list[int], d.pop("creator_levels", UNSET))

        quota_period_sum = d.pop("quota_period_sum", UNSET)

        quota_period_use = d.pop("quota_period_use", UNSET)

        quota_bonus_sum = d.pop("quota_bonus_sum", UNSET)

        quota_bonus_use = d.pop("quota_bonus_use", UNSET)

        get_weekly_creator_outreach_quota_response_data_data_quota_detail = cls(
            creator_levels=creator_levels,
            quota_period_sum=quota_period_sum,
            quota_period_use=quota_period_use,
            quota_bonus_sum=quota_bonus_sum,
            quota_bonus_use=quota_bonus_use,
        )

        get_weekly_creator_outreach_quota_response_data_data_quota_detail.additional_properties = d
        return get_weekly_creator_outreach_quota_response_data_data_quota_detail

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
