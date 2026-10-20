from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_tracking_response_data_tracking import GetOrderTrackingResponseDataTracking


T = TypeVar("T", bound="GetOrderTrackingResponseData")


@_attrs_define
class GetOrderTrackingResponseData:
    """
    Attributes:
        tracking (list[GetOrderTrackingResponseDataTracking] | Unset): The return list of tracking information.
    """

    tracking: list[GetOrderTrackingResponseDataTracking] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracking: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tracking, Unset):
            tracking = []
            for tracking_item_data in self.tracking:
                tracking_item = tracking_item_data.to_dict()
                tracking.append(tracking_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_tracking_response_data_tracking import (
            GetOrderTrackingResponseDataTracking,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _tracking = d.pop("tracking", UNSET)
        tracking: list[GetOrderTrackingResponseDataTracking] | Unset = UNSET
        if _tracking is not UNSET:
            tracking = []
            for tracking_item_data in _tracking:
                tracking_item = GetOrderTrackingResponseDataTracking.from_dict(tracking_item_data)

                tracking.append(tracking_item)

        get_order_tracking_response_data = cls(
            tracking=tracking,
        )

        get_order_tracking_response_data.additional_properties = d
        return get_order_tracking_response_data

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
