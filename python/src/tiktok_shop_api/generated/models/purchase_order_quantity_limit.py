from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PurchaseOrderQuantityLimit")



@_attrs_define
class PurchaseOrderQuantityLimit:
    """ 
        Attributes:
            maximum_order_quantity (int | Unset): The maximum purchase quantity per order for each
                product variation (SKU).
                For example: If you set a maximum limit of 2 for a product with 5 variations (SKUs), the customer can purchase
                up to 2 of each SKU, for a total of 10 items per order.
            cumulative_order_quantity (int | Unset): · The total quantity a customer can buy of a product's
                variations (SKUs) across all orders, while the limit is active. Clearing the limit will reset their past
                purchases, allowing them to buy again up to the new limit, or without restriction if no limit is set.
                • For example, if you set a total limit of 2 for a product with 5 variations (SKUs), the customer can buy up to
                2 of each SKU, for a total of 10 items across multiple purchases. After that, they can't buy more unless you
                clear the limits.The total limit must be more than or equal to the maximum
                limit.
     """

    maximum_order_quantity: int | Unset = UNSET
    cumulative_order_quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        maximum_order_quantity = self.maximum_order_quantity

        cumulative_order_quantity = self.cumulative_order_quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if maximum_order_quantity is not UNSET:
            field_dict["maximum_order_quantity"] = maximum_order_quantity
        if cumulative_order_quantity is not UNSET:
            field_dict["cumulative_order_quantity"] = cumulative_order_quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        maximum_order_quantity = d.pop("maximum_order_quantity", UNSET)

        cumulative_order_quantity = d.pop("cumulative_order_quantity", UNSET)

        purchase_order_quantity_limit = cls(
            maximum_order_quantity=maximum_order_quantity,
            cumulative_order_quantity=cumulative_order_quantity,
        )


        purchase_order_quantity_limit.additional_properties = d
        return purchase_order_quantity_limit

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
