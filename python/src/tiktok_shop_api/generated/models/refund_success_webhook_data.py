from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.refund_success_webhook_data_line_item import RefundSuccessWebhookDataLineItem


T = TypeVar("T", bound="RefundSuccessWebhookData")


@_attrs_define
class RefundSuccessWebhookData:
    """
    Attributes:
        aftersales_request_id (str | Unset): Parent aftersales request identifier.
        line_items (list[RefundSuccessWebhookDataLineItem] | Unset): Line-item level identifiers included in the
            successful refund.
        refund_currency (str | Unset): Currency of the refunded amount.
        refund_status (str | Unset): Refund result. Current example shows `REFUND_SUCCESS`.
        refund_timestamp (int | Unset): Refund completion time in Unix seconds.
        refund_total (str | Unset): Total refunded amount.
        rma_id (str | Unset): Associated RMA identifier.
    """

    aftersales_request_id: str | Unset = UNSET
    line_items: list[RefundSuccessWebhookDataLineItem] | Unset = UNSET
    refund_currency: str | Unset = UNSET
    refund_status: str | Unset = UNSET
    refund_timestamp: int | Unset = UNSET
    refund_total: str | Unset = UNSET
    rma_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aftersales_request_id = self.aftersales_request_id

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        refund_currency = self.refund_currency

        refund_status = self.refund_status

        refund_timestamp = self.refund_timestamp

        refund_total = self.refund_total

        rma_id = self.rma_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aftersales_request_id is not UNSET:
            field_dict["aftersales_request_id"] = aftersales_request_id
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if refund_currency is not UNSET:
            field_dict["refund_currency"] = refund_currency
        if refund_status is not UNSET:
            field_dict["refund_status"] = refund_status
        if refund_timestamp is not UNSET:
            field_dict["refund_timestamp"] = refund_timestamp
        if refund_total is not UNSET:
            field_dict["refund_total"] = refund_total
        if rma_id is not UNSET:
            field_dict["rma_id"] = rma_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refund_success_webhook_data_line_item import RefundSuccessWebhookDataLineItem  # noqa: PLC0415

        d = dict(src_dict)
        aftersales_request_id = d.pop("aftersales_request_id", UNSET)

        _line_items = d.pop("line_items", UNSET)
        line_items: list[RefundSuccessWebhookDataLineItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = RefundSuccessWebhookDataLineItem.from_dict(line_items_item_data)

                line_items.append(line_items_item)

        refund_currency = d.pop("refund_currency", UNSET)

        refund_status = d.pop("refund_status", UNSET)

        refund_timestamp = d.pop("refund_timestamp", UNSET)

        refund_total = d.pop("refund_total", UNSET)

        rma_id = d.pop("rma_id", UNSET)

        refund_success_webhook_data = cls(
            aftersales_request_id=aftersales_request_id,
            line_items=line_items,
            refund_currency=refund_currency,
            refund_status=refund_status,
            refund_timestamp=refund_timestamp,
            refund_total=refund_total,
            rma_id=rma_id,
        )

        refund_success_webhook_data.additional_properties = d
        return refund_success_webhook_data

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
