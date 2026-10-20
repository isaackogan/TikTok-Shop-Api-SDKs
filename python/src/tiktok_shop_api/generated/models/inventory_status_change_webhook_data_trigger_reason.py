from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="InventoryStatusChangeWebhookDataTriggerReason")



@_attrs_define
class InventoryStatusChangeWebhookDataTriggerReason:
    """ 
        Attributes:
            alert_type (str | Unset): PREDICTION: TikTok Shop predicts the inventory will go out of stock in X days
                 REALTIME: The inventory has reached LOW_STOCK or OUT_OF_STOCK
            lead_days (int | Unset): When `alert_type == PREDICTION`, the value is the time slot between `update_time` and
                the predicted out-of-stock date.
                 When `alert_type == REALTIME`, the parameter is not returned.
            low_stock_threshold (int | Unset): When `alert_type == REALTIME`, the value is the low stock threshold met.
                 When `alert_type == PREDICTION`, the parameter is not returned.
     """

    alert_type: str | Unset = UNSET
    lead_days: int | Unset = UNSET
    low_stock_threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        alert_type = self.alert_type

        lead_days = self.lead_days

        low_stock_threshold = self.low_stock_threshold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if alert_type is not UNSET:
            field_dict["alert_type"] = alert_type
        if lead_days is not UNSET:
            field_dict["lead_days"] = lead_days
        if low_stock_threshold is not UNSET:
            field_dict["low_stock_threshold"] = low_stock_threshold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alert_type = d.pop("alert_type", UNSET)

        lead_days = d.pop("lead_days", UNSET)

        low_stock_threshold = d.pop("low_stock_threshold", UNSET)

        inventory_status_change_webhook_data_trigger_reason = cls(
            alert_type=alert_type,
            lead_days=lead_days,
            low_stock_threshold=low_stock_threshold,
        )


        inventory_status_change_webhook_data_trigger_reason.additional_properties = d
        return inventory_status_change_webhook_data_trigger_reason

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
