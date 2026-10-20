from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.threshold import Threshold


T = TypeVar("T", bound="EditOpenCollaborationSampleRuleRequestSampleRule")


@_attrs_define
class EditOpenCollaborationSampleRuleRequestSampleRule:
    """
    Attributes:
        activate_status (str): To activate the sample rule, use `ACTIVATE`; to deactivate the sample rule, use
            `DEACTIVATE`.
            When using `ACTIVATE`, you must specify the details of the rule; when using `DEACTIVATE`, you just need to
            specify `product_id`.
        sample_quota (int | Unset): The total quantity of the samples provided by the seller that the creators can apply
            for.
        is_sample_time_unlimited (bool | Unset): Whether the sample is always available for application:
            - If true, the sample can be requested at any time.
            - If false, the sample can only be requested during specified time periods. You must set start_time and
            end_time.
        start_time (int | Unset): The start of the period during which a creator can apply for samples, as a Unix
            timestamp in seconds. You must specify `start_time` and `end_time` together.
        end_time (int | Unset): The end of the period during which a creator can apply for samples, as a Unix timestamp
            in seconds. You must specify `start_time` and `end_time` together.
        thresholds (Threshold | Unset):
    """

    activate_status: str
    sample_quota: int | Unset = UNSET
    is_sample_time_unlimited: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    thresholds: Threshold | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activate_status = self.activate_status

        sample_quota = self.sample_quota

        is_sample_time_unlimited = self.is_sample_time_unlimited

        start_time = self.start_time

        end_time = self.end_time

        thresholds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thresholds, Unset):
            thresholds = self.thresholds.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activate_status": activate_status,
            }
        )
        if sample_quota is not UNSET:
            field_dict["sample_quota"] = sample_quota
        if is_sample_time_unlimited is not UNSET:
            field_dict["is_sample_time_unlimited"] = is_sample_time_unlimited
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
        activate_status = d.pop("activate_status")

        sample_quota = d.pop("sample_quota", UNSET)

        is_sample_time_unlimited = d.pop("is_sample_time_unlimited", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        _thresholds = d.pop("thresholds", UNSET)
        thresholds: Threshold | Unset
        if isinstance(_thresholds, Unset):
            thresholds = UNSET
        else:
            thresholds = Threshold.from_dict(_thresholds)

        edit_open_collaboration_sample_rule_request_sample_rule = cls(
            activate_status=activate_status,
            sample_quota=sample_quota,
            is_sample_time_unlimited=is_sample_time_unlimited,
            start_time=start_time,
            end_time=end_time,
            thresholds=thresholds,
        )

        edit_open_collaboration_sample_rule_request_sample_rule.additional_properties = d
        return edit_open_collaboration_sample_rule_request_sample_rule

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
