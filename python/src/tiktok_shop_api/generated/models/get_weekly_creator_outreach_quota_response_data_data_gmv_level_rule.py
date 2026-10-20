from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_left_gmv import GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleLeftGmv
  from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_quota_detail import GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleQuotaDetail
  from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_right_gmv import GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleRightGmv





T = TypeVar("T", bound="GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRule")



@_attrs_define
class GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRule:
    """ 
        Attributes:
            reached_max_follower_cnt (str | Unset): Maximum follower count for creators the shop can reach under this GMV
                tier.
            gmv_tier (str | Unset): GMV tier id
            left_gmv (GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleLeftGmv | Unset):
            right_gmv (GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleRightGmv | Unset):
            quota_details (list[GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleQuotaDetail] | Unset): Creator-
                level quota detail rules
     """

    reached_max_follower_cnt: str | Unset = UNSET
    gmv_tier: str | Unset = UNSET
    left_gmv: GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleLeftGmv | Unset = UNSET
    right_gmv: GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleRightGmv | Unset = UNSET
    quota_details: list[GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleQuotaDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_left_gmv import GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleLeftGmv # noqa: PLC0415
        from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_quota_detail import GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleQuotaDetail # noqa: PLC0415
        from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_right_gmv import GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleRightGmv # noqa: PLC0415
        reached_max_follower_cnt = self.reached_max_follower_cnt

        gmv_tier = self.gmv_tier

        left_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.left_gmv, Unset):
            left_gmv = self.left_gmv.to_dict()

        right_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.right_gmv, Unset):
            right_gmv = self.right_gmv.to_dict()

        quota_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quota_details, Unset):
            quota_details = []
            for quota_details_item_data in self.quota_details:
                quota_details_item = quota_details_item_data.to_dict()
                quota_details.append(quota_details_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reached_max_follower_cnt is not UNSET:
            field_dict["reached_max_follower_cnt"] = reached_max_follower_cnt
        if gmv_tier is not UNSET:
            field_dict["gmv_tier"] = gmv_tier
        if left_gmv is not UNSET:
            field_dict["left_gmv"] = left_gmv
        if right_gmv is not UNSET:
            field_dict["right_gmv"] = right_gmv
        if quota_details is not UNSET:
            field_dict["quota_details"] = quota_details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_left_gmv import GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleLeftGmv # noqa: PLC0415
        from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_quota_detail import GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleQuotaDetail # noqa: PLC0415
        from ..models.get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule_right_gmv import GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleRightGmv # noqa: PLC0415
        d = dict(src_dict)
        reached_max_follower_cnt = d.pop("reached_max_follower_cnt", UNSET)

        gmv_tier = d.pop("gmv_tier", UNSET)

        _left_gmv = d.pop("left_gmv", UNSET)
        left_gmv: GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleLeftGmv | Unset
        if isinstance(_left_gmv,  Unset):
            left_gmv = UNSET
        else:
            left_gmv = GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleLeftGmv.from_dict(_left_gmv)




        _right_gmv = d.pop("right_gmv", UNSET)
        right_gmv: GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleRightGmv | Unset
        if isinstance(_right_gmv,  Unset):
            right_gmv = UNSET
        else:
            right_gmv = GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleRightGmv.from_dict(_right_gmv)




        _quota_details = d.pop("quota_details", UNSET)
        quota_details: list[GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleQuotaDetail] | Unset = UNSET
        if _quota_details is not UNSET:
            quota_details = []
            for quota_details_item_data in _quota_details:
                quota_details_item = GetWeeklyCreatorOutreachQuotaResponseDataDataGmvLevelRuleQuotaDetail.from_dict(quota_details_item_data)



                quota_details.append(quota_details_item)


        get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule = cls(
            reached_max_follower_cnt=reached_max_follower_cnt,
            gmv_tier=gmv_tier,
            left_gmv=left_gmv,
            right_gmv=right_gmv,
            quota_details=quota_details,
        )


        get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule.additional_properties = d
        return get_weekly_creator_outreach_quota_response_data_data_gmv_level_rule

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
