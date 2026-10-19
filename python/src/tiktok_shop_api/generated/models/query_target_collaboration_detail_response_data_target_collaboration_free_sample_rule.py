from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule")


@_attrs_define
class QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule:
    """
    Attributes:
        has_free_sample (bool | Unset): If true, free samples are provided to creators invited to the target
            collaboration group.
        is_sample_approval_exempt (bool | Unset): If true, creators invited to the target collaboration are exempt from
            seller review and will automatically be approved for a free sample.
            Note that if has_free_sample=false, this field will not take effect.
    """

    has_free_sample: bool | Unset = UNSET
    is_sample_approval_exempt: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_free_sample = self.has_free_sample

        is_sample_approval_exempt = self.is_sample_approval_exempt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_free_sample is not UNSET:
            field_dict["has_free_sample"] = has_free_sample
        if is_sample_approval_exempt is not UNSET:
            field_dict["is_sample_approval_exempt"] = is_sample_approval_exempt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_free_sample = d.pop("has_free_sample", UNSET)

        is_sample_approval_exempt = d.pop("is_sample_approval_exempt", UNSET)

        query_target_collaboration_detail_response_data_target_collaboration_free_sample_rule = cls(
            has_free_sample=has_free_sample,
            is_sample_approval_exempt=is_sample_approval_exempt,
        )

        query_target_collaboration_detail_response_data_target_collaboration_free_sample_rule.additional_properties = d
        return query_target_collaboration_detail_response_data_target_collaboration_free_sample_rule

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
