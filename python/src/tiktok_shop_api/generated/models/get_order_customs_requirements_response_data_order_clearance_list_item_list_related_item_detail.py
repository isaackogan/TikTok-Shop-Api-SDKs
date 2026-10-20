from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetOrderCustomsRequirementsResponseDataOrderClearanceListItemListRelatedItemDetail")



@_attrs_define
class GetOrderCustomsRequirementsResponseDataOrderClearanceListItemListRelatedItemDetail:
    """ 
        Attributes:
            product_id (str | Unset): Product ID.
            sku_id (str | Unset): SKU ID.
            qty (int | Unset): The amount of this sku
            price_percent (int | Unset): unit: %, price_percent=10 means 10%
     """

    product_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    qty: int | Unset = UNSET
    price_percent: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        sku_id = self.sku_id

        qty = self.qty

        price_percent = self.price_percent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if qty is not UNSET:
            field_dict["qty"] = qty
        if price_percent is not UNSET:
            field_dict["price_percent"] = price_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        qty = d.pop("qty", UNSET)

        price_percent = d.pop("price_percent", UNSET)

        get_order_customs_requirements_response_data_order_clearance_list_item_list_related_item_detail = cls(
            product_id=product_id,
            sku_id=sku_id,
            qty=qty,
            price_percent=price_percent,
        )


        get_order_customs_requirements_response_data_order_clearance_list_item_list_related_item_detail.additional_properties = d
        return get_order_customs_requirements_response_data_order_clearance_list_item_list_related_item_detail

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
