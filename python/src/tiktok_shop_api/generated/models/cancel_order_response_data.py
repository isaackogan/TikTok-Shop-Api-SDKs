from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelOrderResponseData")


@_attrs_define
class CancelOrderResponseData:
    """
    Attributes:
        cancel_id (str | Unset): The identifier of a specific order cancellation.
        cancel_status (str | Unset): The status of an order cancellation request.
            Available values:
            - `CANCELLATION_REQUEST_PENDING`
            - `CANCELLATION_REQUEST_SUCCESS`
            - `CANCELLATION_REQUEST_CANCEL`
            - `CANCELLATION_REQUEST_COMPLETE`
    """

    cancel_id: str | Unset = UNSET
    cancel_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancel_id = self.cancel_id

        cancel_status = self.cancel_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancel_id is not UNSET:
            field_dict["cancel_id"] = cancel_id
        if cancel_status is not UNSET:
            field_dict["cancel_status"] = cancel_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cancel_id = d.pop("cancel_id", UNSET)

        cancel_status = d.pop("cancel_status", UNSET)

        cancel_order_response_data = cls(
            cancel_id=cancel_id,
            cancel_status=cancel_status,
        )

        cancel_order_response_data.additional_properties = d
        return cancel_order_response_data

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
