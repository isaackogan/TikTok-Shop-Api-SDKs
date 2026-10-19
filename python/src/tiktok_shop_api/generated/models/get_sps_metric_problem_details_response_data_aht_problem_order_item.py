from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSPSMetricProblemDetailsResponseDataAhtProblemOrderItem")


@_attrs_define
class GetSPSMetricProblemDetailsResponseDataAhtProblemOrderItem:
    """
    Attributes:
        aftersales_type_name (str | Unset): Aftersales type returned by TikTok Shop aftersales classification.
        approve_duration_hours (str | Unset): Approval duration in hours.
        inspect_duration_hours (str | Unset): Inspection duration in hours.
        order_id (str | Unset): Order ID.
        return_order_id (str | Unset): Return order ID.
        review_count (int | Unset): Number of review rounds.
        total_handle_duration_hours (str | Unset): Total aftersales handle duration in hours.
    """

    aftersales_type_name: str | Unset = UNSET
    approve_duration_hours: str | Unset = UNSET
    inspect_duration_hours: str | Unset = UNSET
    order_id: str | Unset = UNSET
    return_order_id: str | Unset = UNSET
    review_count: int | Unset = UNSET
    total_handle_duration_hours: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aftersales_type_name = self.aftersales_type_name

        approve_duration_hours = self.approve_duration_hours

        inspect_duration_hours = self.inspect_duration_hours

        order_id = self.order_id

        return_order_id = self.return_order_id

        review_count = self.review_count

        total_handle_duration_hours = self.total_handle_duration_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aftersales_type_name is not UNSET:
            field_dict["aftersales_type_name"] = aftersales_type_name
        if approve_duration_hours is not UNSET:
            field_dict["approve_duration_hours"] = approve_duration_hours
        if inspect_duration_hours is not UNSET:
            field_dict["inspect_duration_hours"] = inspect_duration_hours
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if return_order_id is not UNSET:
            field_dict["return_order_id"] = return_order_id
        if review_count is not UNSET:
            field_dict["review_count"] = review_count
        if total_handle_duration_hours is not UNSET:
            field_dict["total_handle_duration_hours"] = total_handle_duration_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aftersales_type_name = d.pop("aftersales_type_name", UNSET)

        approve_duration_hours = d.pop("approve_duration_hours", UNSET)

        inspect_duration_hours = d.pop("inspect_duration_hours", UNSET)

        order_id = d.pop("order_id", UNSET)

        return_order_id = d.pop("return_order_id", UNSET)

        review_count = d.pop("review_count", UNSET)

        total_handle_duration_hours = d.pop("total_handle_duration_hours", UNSET)

        get_sps_metric_problem_details_response_data_aht_problem_order_item = cls(
            aftersales_type_name=aftersales_type_name,
            approve_duration_hours=approve_duration_hours,
            inspect_duration_hours=inspect_duration_hours,
            order_id=order_id,
            return_order_id=return_order_id,
            review_count=review_count,
            total_handle_duration_hours=total_handle_duration_hours,
        )

        get_sps_metric_problem_details_response_data_aht_problem_order_item.additional_properties = d
        return get_sps_metric_problem_details_response_data_aht_problem_order_item

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
