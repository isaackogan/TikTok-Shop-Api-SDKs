from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePackagesRequestOrderLineItem")


@_attrs_define
class CreatePackagesRequestOrderLineItem:
    """
    Attributes:
        order_line_id (str | Unset): The TikTok Shop order line item ID.
        sub_item_id (str | Unset): Only for virtual bundle items,list of sub item ids.
            If ship_type=2,This is a required field;If ship_type=1&3,we will not use this field
    """

    order_line_id: str | Unset = UNSET
    sub_item_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_line_id = self.order_line_id

        sub_item_id = self.sub_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if sub_item_id is not UNSET:
            field_dict["sub_item_id"] = sub_item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_line_id = d.pop("order_line_id", UNSET)

        sub_item_id = d.pop("sub_item_id", UNSET)

        create_packages_request_order_line_item = cls(
            order_line_id=order_line_id,
            sub_item_id=sub_item_id,
        )

        create_packages_request_order_line_item.additional_properties = d
        return create_packages_request_order_line_item

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
