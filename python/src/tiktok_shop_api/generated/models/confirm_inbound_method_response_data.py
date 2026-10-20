from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfirmInboundMethodResponseData")


@_attrs_define
class ConfirmInboundMethodResponseData:
    """
    Attributes:
        inbound_order_ids (list[str] | Unset): List of child inbound order IDs generated for the confirmed FBT inbound
            plan.
    """

    inbound_order_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound_order_ids: list[str] | Unset = UNSET
        if not isinstance(self.inbound_order_ids, Unset):
            inbound_order_ids = self.inbound_order_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound_order_ids is not UNSET:
            field_dict["inbound_order_ids"] = inbound_order_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inbound_order_ids = cast(list[str], d.pop("inbound_order_ids", UNSET))

        confirm_inbound_method_response_data = cls(
            inbound_order_ids=inbound_order_ids,
        )

        confirm_inbound_method_response_data.additional_properties = d
        return confirm_inbound_method_response_data

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
