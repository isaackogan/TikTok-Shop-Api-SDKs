from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.size_chart_change_webhook_data_event_type import SizeChartChangeWebhookDataEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SizeChartChangeWebhookData")


@_attrs_define
class SizeChartChangeWebhookData:
    """
    Attributes:
        size_chart_template_id (str | Unset): The ID of the size chart template that's being changed.
        size_chart_template_name (str | Unset): The name of the size chart template that's being changed.
        event_type (SizeChartChangeWebhookDataEventType | Unset): The change that occurred for the size chart. Possible
            values:
             - `CREATE`: A new size chart is created
             - `EDIT`: The size chart is edited
             - `DELETE`: The size chart is deleted
        update_time (int | Unset): The time when the change occurred. Unix timestamp.
    """

    size_chart_template_id: str | Unset = UNSET
    size_chart_template_name: str | Unset = UNSET
    event_type: SizeChartChangeWebhookDataEventType | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size_chart_template_id = self.size_chart_template_id

        size_chart_template_name = self.size_chart_template_name

        event_type: str | Unset = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size_chart_template_id is not UNSET:
            field_dict["size_chart_template_id"] = size_chart_template_id
        if size_chart_template_name is not UNSET:
            field_dict["size_chart_template_name"] = size_chart_template_name
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        size_chart_template_id = d.pop("size_chart_template_id", UNSET)

        size_chart_template_name = d.pop("size_chart_template_name", UNSET)

        _event_type = d.pop("event_type", UNSET)
        event_type: SizeChartChangeWebhookDataEventType | Unset
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = SizeChartChangeWebhookDataEventType(_event_type)

        update_time = d.pop("update_time", UNSET)

        size_chart_change_webhook_data = cls(
            size_chart_template_id=size_chart_template_id,
            size_chart_template_name=size_chart_template_name,
            event_type=event_type,
            update_time=update_time,
        )

        size_chart_change_webhook_data.additional_properties = d
        return size_chart_change_webhook_data

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
