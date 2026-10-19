from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubmitCustomsClearanceInformationRequestOrderListItemListItemDetail")


@_attrs_define
class SubmitCustomsClearanceInformationRequestOrderListItemListItemDetail:
    """
    Attributes:
        sku_id (str): The SKU ID for this customs clearance detail.
        qty (int): Quantity of this SKU in the customs clearance detail. Must be greater than 0.
        price_percent (int): Percentage assigned to this SKU within the order line. Each value must be non-negative, and
            the price_percent values in item_detail must total 100. For example, 10 means 10%.
    """

    sku_id: str
    qty: int
    price_percent: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sku_id = self.sku_id

        qty = self.qty

        price_percent = self.price_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sku_id": sku_id,
                "qty": qty,
                "price_percent": price_percent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sku_id = d.pop("sku_id")

        qty = d.pop("qty")

        price_percent = d.pop("price_percent")

        submit_customs_clearance_information_request_order_list_item_list_item_detail = cls(
            sku_id=sku_id,
            qty=qty,
            price_percent=price_percent,
        )

        submit_customs_clearance_information_request_order_list_item_list_item_detail.additional_properties = d
        return submit_customs_clearance_information_request_order_list_item_list_item_detail

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
