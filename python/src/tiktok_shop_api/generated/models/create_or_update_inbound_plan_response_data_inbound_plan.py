from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOrUpdateInboundPlanResponseDataInboundPlan")


@_attrs_define
class CreateOrUpdateInboundPlanResponseDataInboundPlan:
    """
    Attributes:
        plan_id (str | Unset): Plan identifier.
    """

    plan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_id = self.plan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plan_id is not UNSET:
            field_dict["plan_id"] = plan_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plan_id = d.pop("plan_id", UNSET)

        create_or_update_inbound_plan_response_data_inbound_plan = cls(
            plan_id=plan_id,
        )

        create_or_update_inbound_plan_response_data_inbound_plan.additional_properties = d
        return create_or_update_inbound_plan_response_data_inbound_plan

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
