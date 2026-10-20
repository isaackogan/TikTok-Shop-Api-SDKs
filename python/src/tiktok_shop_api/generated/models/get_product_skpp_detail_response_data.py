from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_product_skpp_detail_response_data_reward import GetProductSKPPDetailResponseDataReward
  from ..models.get_product_skpp_detail_response_data_task_detail import GetProductSKPPDetailResponseDataTaskDetail





T = TypeVar("T", bound="GetProductSKPPDetailResponseData")



@_attrs_define
class GetProductSKPPDetailResponseData:
    """ 
        Attributes:
            product_id (str | Unset): Platform product ID.
            affiliate_program_status (str | Unset): Affiliate Program enrolment. Possible values: ACTIVE / INACTIVE.
            total_score (int | Unset): Current SKPP total score, as of update_time.
            target_score (int | Unset): Score threshold to qualify for SKPP.
            rewards (list[GetProductSKPPDetailResponseDataReward] | Unset): Reward list.
            task_details (list[GetProductSKPPDetailResponseDataTaskDetail] | Unset): Per-category score breakdown with
                suggested actions.
            update_time (int | Unset): Date of the offline data snapshot that total_score, rewards and the score breakdown
                are derived from, returned as a Unix timestamp in seconds, pinned to the last second of that date in UTC
                (23:59:59Z). The value is date-level only — the time component is always 23:59:59 UTC — because the SKPP scoring
                runs in an offline pipeline with no intraday granularity. Latency is typically T+1 (the evening of day N
                publishes the day N−1 snapshot) and at most T+2.
            skpp_status (str | Unset): Possible values: QUALIFIED / NOT_QUALIFIED / NOT_ELIGIBLE.
     """

    product_id: str | Unset = UNSET
    affiliate_program_status: str | Unset = UNSET
    total_score: int | Unset = UNSET
    target_score: int | Unset = UNSET
    rewards: list[GetProductSKPPDetailResponseDataReward] | Unset = UNSET
    task_details: list[GetProductSKPPDetailResponseDataTaskDetail] | Unset = UNSET
    update_time: int | Unset = UNSET
    skpp_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_skpp_detail_response_data_reward import GetProductSKPPDetailResponseDataReward # noqa: PLC0415
        from ..models.get_product_skpp_detail_response_data_task_detail import GetProductSKPPDetailResponseDataTaskDetail # noqa: PLC0415
        product_id = self.product_id

        affiliate_program_status = self.affiliate_program_status

        total_score = self.total_score

        target_score = self.target_score

        rewards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rewards, Unset):
            rewards = []
            for rewards_item_data in self.rewards:
                rewards_item = rewards_item_data.to_dict()
                rewards.append(rewards_item)



        task_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.task_details, Unset):
            task_details = []
            for task_details_item_data in self.task_details:
                task_details_item = task_details_item_data.to_dict()
                task_details.append(task_details_item)



        update_time = self.update_time

        skpp_status = self.skpp_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if affiliate_program_status is not UNSET:
            field_dict["affiliate_program_status"] = affiliate_program_status
        if total_score is not UNSET:
            field_dict["total_score"] = total_score
        if target_score is not UNSET:
            field_dict["target_score"] = target_score
        if rewards is not UNSET:
            field_dict["rewards"] = rewards
        if task_details is not UNSET:
            field_dict["task_details"] = task_details
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if skpp_status is not UNSET:
            field_dict["skpp_status"] = skpp_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_skpp_detail_response_data_reward import GetProductSKPPDetailResponseDataReward # noqa: PLC0415
        from ..models.get_product_skpp_detail_response_data_task_detail import GetProductSKPPDetailResponseDataTaskDetail # noqa: PLC0415
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        affiliate_program_status = d.pop("affiliate_program_status", UNSET)

        total_score = d.pop("total_score", UNSET)

        target_score = d.pop("target_score", UNSET)

        _rewards = d.pop("rewards", UNSET)
        rewards: list[GetProductSKPPDetailResponseDataReward] | Unset = UNSET
        if _rewards is not UNSET:
            rewards = []
            for rewards_item_data in _rewards:
                rewards_item = GetProductSKPPDetailResponseDataReward.from_dict(rewards_item_data)



                rewards.append(rewards_item)


        _task_details = d.pop("task_details", UNSET)
        task_details: list[GetProductSKPPDetailResponseDataTaskDetail] | Unset = UNSET
        if _task_details is not UNSET:
            task_details = []
            for task_details_item_data in _task_details:
                task_details_item = GetProductSKPPDetailResponseDataTaskDetail.from_dict(task_details_item_data)



                task_details.append(task_details_item)


        update_time = d.pop("update_time", UNSET)

        skpp_status = d.pop("skpp_status", UNSET)

        get_product_skpp_detail_response_data = cls(
            product_id=product_id,
            affiliate_program_status=affiliate_program_status,
            total_score=total_score,
            target_score=target_score,
            rewards=rewards,
            task_details=task_details,
            update_time=update_time,
            skpp_status=skpp_status,
        )


        get_product_skpp_detail_response_data.additional_properties = d
        return get_product_skpp_detail_response_data

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
