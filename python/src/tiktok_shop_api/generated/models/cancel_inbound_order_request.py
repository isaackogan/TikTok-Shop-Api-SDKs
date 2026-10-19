from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CancelInboundOrderRequest")


@_attrs_define
class CancelInboundOrderRequest:
    """
    Attributes:
        order_id (str): The positive numeric identifier of the inbound order to cancel.

            **Note:** Provide the numeric sequence only; do not include the "IBR" prefix (for example, use `123456` instead
            of `IBR123456`).
        cancel_reason (str): Reason for cancelling the inbound order. The value must not be empty or contain only
            whitespace.
    """

    order_id: str
    cancel_reason: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        cancel_reason = self.cancel_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "cancel_reason": cancel_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("order_id")

        cancel_reason = d.pop("cancel_reason")

        cancel_inbound_order_request = cls(
            order_id=order_id,
            cancel_reason=cancel_reason,
        )

        cancel_inbound_order_request.additional_properties = d
        return cancel_inbound_order_request

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
