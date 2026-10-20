from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.threshold import Threshold


T = TypeVar("T", bound="GetOpenCollaborationSampleRulesResponseDataSampleRule")


@_attrs_define
class GetOpenCollaborationSampleRulesResponseDataSampleRule:
    """
    Attributes:
        product_id (str | Unset): The unique id of product.
        sample_quota (int | Unset): The sample total quantity provided by seller which creators can apply for.
        is_sample_time_unlimited (bool | Unset): Whether samples are timely unlimited for request:
            - If true, it means available all the time
            - If false, it means sample only available from `begin_time` to `end_time`.
        status (str | Unset): Free sample rule status:
            - NOT_STARTED. Not yet reached the specified `begin_time`.
            - ONGOING. The sample rule is effective and the collaboration is ongoing.
            - `NO_LEFT_COUNT`. `sample_quantity_available` is `0`.
            - PLAN_EXCEPTION. The product commission collaboration status is abnormal
            - EXPIRED. Exceeded the `end_time`.
        available_quantity (int | Unset): The quantity of remaining samples available for application.
        start_time (int | Unset): When present, the start of the sample application period, expressed as a Unix
            timestamp in seconds (UTC).
        end_time (int | Unset): When present, the end of the sample application period, expressed as a Unix timestamp in
            seconds (UTC).
        thresholds (Threshold | Unset):
    """

    product_id: str | Unset = UNSET
    sample_quota: int | Unset = UNSET
    is_sample_time_unlimited: bool | Unset = UNSET
    status: str | Unset = UNSET
    available_quantity: int | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    thresholds: Threshold | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        sample_quota = self.sample_quota

        is_sample_time_unlimited = self.is_sample_time_unlimited

        status = self.status

        available_quantity = self.available_quantity

        start_time = self.start_time

        end_time = self.end_time

        thresholds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thresholds, Unset):
            thresholds = self.thresholds.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if sample_quota is not UNSET:
            field_dict["sample_quota"] = sample_quota
        if is_sample_time_unlimited is not UNSET:
            field_dict["is_sample_time_unlimited"] = is_sample_time_unlimited
        if status is not UNSET:
            field_dict["status"] = status
        if available_quantity is not UNSET:
            field_dict["available_quantity"] = available_quantity
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if thresholds is not UNSET:
            field_dict["thresholds"] = thresholds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.threshold import Threshold  # noqa: PLC0415

        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        sample_quota = d.pop("sample_quota", UNSET)

        is_sample_time_unlimited = d.pop("is_sample_time_unlimited", UNSET)

        status = d.pop("status", UNSET)

        available_quantity = d.pop("available_quantity", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        _thresholds = d.pop("thresholds", UNSET)
        thresholds: Threshold | Unset
        if isinstance(_thresholds, Unset):
            thresholds = UNSET
        else:
            thresholds = Threshold.from_dict(_thresholds)

        get_open_collaboration_sample_rules_response_data_sample_rule = cls(
            product_id=product_id,
            sample_quota=sample_quota,
            is_sample_time_unlimited=is_sample_time_unlimited,
            status=status,
            available_quantity=available_quantity,
            start_time=start_time,
            end_time=end_time,
            thresholds=thresholds,
        )

        get_open_collaboration_sample_rules_response_data_sample_rule.additional_properties = d
        return get_open_collaboration_sample_rules_response_data_sample_rule

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
