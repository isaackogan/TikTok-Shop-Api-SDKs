from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_open_collaboration_sample_rule_request_sample_rule import (
        EditOpenCollaborationSampleRuleRequestSampleRule,
    )


T = TypeVar("T", bound="EditOpenCollaborationSampleRuleRequest")


@_attrs_define
class EditOpenCollaborationSampleRuleRequest:
    """
    Attributes:
        product_id (str): The product ID to which the sample rule applies. You can only assign one sample rule for one
            `product_id`. Only the most recent API call will take effect.
        sample_rule (EditOpenCollaborationSampleRuleRequestSampleRule | Unset):
    """

    product_id: str
    sample_rule: EditOpenCollaborationSampleRuleRequestSampleRule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        sample_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sample_rule, Unset):
            sample_rule = self.sample_rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
            }
        )
        if sample_rule is not UNSET:
            field_dict["sample_rule"] = sample_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_open_collaboration_sample_rule_request_sample_rule import (
            EditOpenCollaborationSampleRuleRequestSampleRule,  # noqa: PLC0415
        )

        d = dict(src_dict)
        product_id = d.pop("product_id")

        _sample_rule = d.pop("sample_rule", UNSET)
        sample_rule: EditOpenCollaborationSampleRuleRequestSampleRule | Unset
        if isinstance(_sample_rule, Unset):
            sample_rule = UNSET
        else:
            sample_rule = EditOpenCollaborationSampleRuleRequestSampleRule.from_dict(_sample_rule)

        edit_open_collaboration_sample_rule_request = cls(
            product_id=product_id,
            sample_rule=sample_rule,
        )

        edit_open_collaboration_sample_rule_request.additional_properties = d
        return edit_open_collaboration_sample_rule_request

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
