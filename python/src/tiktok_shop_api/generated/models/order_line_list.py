from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OrderLineList")



@_attrs_define
class OrderLineList:
    """ 
        Attributes:
            order_line_item_id (str | Unset): The corresponding order line ID
            sub_order_line_item_id (str | Unset): The sub-order-line ID inside a bundle product
                - Required for bundle products
                - Not required for non-bundle products
     """

    order_line_item_id: str | Unset = UNSET
    sub_order_line_item_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_line_item_id = self.order_line_item_id

        sub_order_line_item_id = self.sub_order_line_item_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_line_item_id is not UNSET:
            field_dict["order_line_item_id"] = order_line_item_id
        if sub_order_line_item_id is not UNSET:
            field_dict["sub_order_line_item_id"] = sub_order_line_item_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_line_item_id = d.pop("order_line_item_id", UNSET)

        sub_order_line_item_id = d.pop("sub_order_line_item_id", UNSET)

        order_line_list = cls(
            order_line_item_id=order_line_item_id,
            sub_order_line_item_id=sub_order_line_item_id,
        )


        order_line_list.additional_properties = d
        return order_line_list

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
