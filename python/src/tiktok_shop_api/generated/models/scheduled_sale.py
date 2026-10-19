from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ScheduledSale")


@_attrs_define
class ScheduledSale:
    """
    Attributes:
        is_enabled_scheduled_sale (bool): Whether scheduled listing is enabled for this product. If `true`,
            `schedule_sale_time` must be provided.
        schedule_sale_time (int): Scheduled listing time, expressed as a Unix timestamp in milliseconds; must be later
            than the current time and within 90 days, and is required when is_enabled_scheduled_sale is true.
    """

    is_enabled_scheduled_sale: bool
    schedule_sale_time: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_enabled_scheduled_sale = self.is_enabled_scheduled_sale

        schedule_sale_time = self.schedule_sale_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_enabled_scheduled_sale": is_enabled_scheduled_sale,
                "schedule_sale_time": schedule_sale_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_enabled_scheduled_sale = d.pop("is_enabled_scheduled_sale")

        schedule_sale_time = d.pop("schedule_sale_time")

        scheduled_sale = cls(
            is_enabled_scheduled_sale=is_enabled_scheduled_sale,
            schedule_sale_time=schedule_sale_time,
        )

        scheduled_sale.additional_properties = d
        return scheduled_sale

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
