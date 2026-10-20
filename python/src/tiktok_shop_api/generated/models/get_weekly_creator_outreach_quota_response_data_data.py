from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule import (
        GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRule,
    )
    from ..models.get_weekly_creator_outreach_quota_response_data_data_quota_detail import (
        GetWeeklyCreatorOutreachQuotaResponseDataDataQuotaDetail,
    )


T = TypeVar("T", bound="GetWeeklyCreatorOutreachQuotaResponseDataData")


@_attrs_define
class GetWeeklyCreatorOutreachQuotaResponseDataData:
    """
    Attributes:
        shop_id (str | Unset): Shop id
        quota_type (str | Unset): Quota type, e.g.
            bouns quota;
            period quota
        gmv_tier (str | Unset): Shop gmv tier
        quota_sum (str | Unset): Shop quota sum
        quota_use (str | Unset): Shop quota used
        unlimited (bool | Unset): Whether the shop has unlimited creator outreach quota.
        reached_max_follower_cnt (str | Unset): Max creator follower count this shop can reach
        new_connect_count (str | Unset): New connect creator count during this quota period
        pair_connect_count (str | Unset): Connect paired creator count during this quota period
        start_time (str | Unset): Quota period start time
        end_time (str | Unset): Quota period end time
        gmv_level_rule (list[GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRule] | Unset): Quota GMV level rules
        quota_details (list[GetWeeklyCreatorOutreachQuotaResponseDataDataQuotaDetail] | Unset): Creator-level quota
            detail information
        bonus_exposure_post_percentile_threshold (str | Unset): Threshold for exposure posts percentile  for shops to
            obtain additional reward of creator-level quota, 0.8 means the 80th percentile.
    """

    shop_id: str | Unset = UNSET
    quota_type: str | Unset = UNSET
    gmv_tier: str | Unset = UNSET
    quota_sum: str | Unset = UNSET
    quota_use: str | Unset = UNSET
    unlimited: bool | Unset = UNSET
    reached_max_follower_cnt: str | Unset = UNSET
    new_connect_count: str | Unset = UNSET
    pair_connect_count: str | Unset = UNSET
    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET
    gmv_level_rule: list[GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRule] | Unset = UNSET
    quota_details: list[GetWeeklyCreatorOutreachQuotaResponseDataDataQuotaDetail] | Unset = UNSET
    bonus_exposure_post_percentile_threshold: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shop_id = self.shop_id

        quota_type = self.quota_type

        gmv_tier = self.gmv_tier

        quota_sum = self.quota_sum

        quota_use = self.quota_use

        unlimited = self.unlimited

        reached_max_follower_cnt = self.reached_max_follower_cnt

        new_connect_count = self.new_connect_count

        pair_connect_count = self.pair_connect_count

        start_time = self.start_time

        end_time = self.end_time

        gmv_level_rule: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gmv_level_rule, Unset):
            gmv_level_rule = []
            for gmv_level_rule_item_data in self.gmv_level_rule:
                gmv_level_rule_item = gmv_level_rule_item_data.to_dict()
                gmv_level_rule.append(gmv_level_rule_item)

        quota_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quota_details, Unset):
            quota_details = []
            for quota_details_item_data in self.quota_details:
                quota_details_item = quota_details_item_data.to_dict()
                quota_details.append(quota_details_item)

        bonus_exposure_post_percentile_threshold = self.bonus_exposure_post_percentile_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if quota_type is not UNSET:
            field_dict["quota_type"] = quota_type
        if gmv_tier is not UNSET:
            field_dict["gmv_tier"] = gmv_tier
        if quota_sum is not UNSET:
            field_dict["quota_sum"] = quota_sum
        if quota_use is not UNSET:
            field_dict["quota_use"] = quota_use
        if unlimited is not UNSET:
            field_dict["unlimited"] = unlimited
        if reached_max_follower_cnt is not UNSET:
            field_dict["reached_max_follower_cnt"] = reached_max_follower_cnt
        if new_connect_count is not UNSET:
            field_dict["new_connect_count"] = new_connect_count
        if pair_connect_count is not UNSET:
            field_dict["pair_connect_count"] = pair_connect_count
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if gmv_level_rule is not UNSET:
            field_dict["gmv_level_rule"] = gmv_level_rule
        if quota_details is not UNSET:
            field_dict["quota_details"] = quota_details
        if bonus_exposure_post_percentile_threshold is not UNSET:
            field_dict["bonus_exposure_post_percentile_threshold"] = bonus_exposure_post_percentile_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule import (
            GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRule,  # noqa: PLC0415
        )
        from ..models.get_weekly_creator_outreach_quota_response_data_data_quota_detail import (
            GetWeeklyCreatorOutreachQuotaResponseDataDataQuotaDetail,  # noqa: PLC0415
        )

        d = dict(src_dict)
        shop_id = d.pop("shop_id", UNSET)

        quota_type = d.pop("quota_type", UNSET)

        gmv_tier = d.pop("gmv_tier", UNSET)

        quota_sum = d.pop("quota_sum", UNSET)

        quota_use = d.pop("quota_use", UNSET)

        unlimited = d.pop("unlimited", UNSET)

        reached_max_follower_cnt = d.pop("reached_max_follower_cnt", UNSET)

        new_connect_count = d.pop("new_connect_count", UNSET)

        pair_connect_count = d.pop("pair_connect_count", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        _gmv_level_rule = d.pop("gmv_level_rule", UNSET)
        gmv_level_rule: list[GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRule] | Unset = UNSET
        if _gmv_level_rule is not UNSET:
            gmv_level_rule = []
            for gmv_level_rule_item_data in _gmv_level_rule:
                gmv_level_rule_item = GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRule.from_dict(
                    gmv_level_rule_item_data
                )

                gmv_level_rule.append(gmv_level_rule_item)

        _quota_details = d.pop("quota_details", UNSET)
        quota_details: list[GetWeeklyCreatorOutreachQuotaResponseDataDataQuotaDetail] | Unset = UNSET
        if _quota_details is not UNSET:
            quota_details = []
            for quota_details_item_data in _quota_details:
                quota_details_item = GetWeeklyCreatorOutreachQuotaResponseDataDataQuotaDetail.from_dict(
                    quota_details_item_data
                )

                quota_details.append(quota_details_item)

        bonus_exposure_post_percentile_threshold = d.pop("bonus_exposure_post_percentile_threshold", UNSET)

        get_weekly_creator_outreach_quota_response_data_data = cls(
            shop_id=shop_id,
            quota_type=quota_type,
            gmv_tier=gmv_tier,
            quota_sum=quota_sum,
            quota_use=quota_use,
            unlimited=unlimited,
            reached_max_follower_cnt=reached_max_follower_cnt,
            new_connect_count=new_connect_count,
            pair_connect_count=pair_connect_count,
            start_time=start_time,
            end_time=end_time,
            gmv_level_rule=gmv_level_rule,
            quota_details=quota_details,
            bonus_exposure_post_percentile_threshold=bonus_exposure_post_percentile_threshold,
        )

        get_weekly_creator_outreach_quota_response_data_data.additional_properties = d
        return get_weekly_creator_outreach_quota_response_data_data

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
