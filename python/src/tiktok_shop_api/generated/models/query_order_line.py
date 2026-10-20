from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="QueryOrderLine")



@_attrs_define
class QueryOrderLine:
    """ 
        Attributes:
            order_line_id (str): The unique identifier of the order line item.
            product_id (str): The unique identifier of the product.
            sku_id (str): The unique identifier of the sku.
            pod_order_data_id (str): The unique identifier of the pod data.
     """

    order_line_id: str
    product_id: str
    sku_id: str
    pod_order_data_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_line_id = self.order_line_id

        product_id = self.product_id

        sku_id = self.sku_id

        pod_order_data_id = self.pod_order_data_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "order_line_id": order_line_id,
            "product_id": product_id,
            "sku_id": sku_id,
            "pod_order_data_id": pod_order_data_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_line_id = d.pop("order_line_id")

        product_id = d.pop("product_id")

        sku_id = d.pop("sku_id")

        pod_order_data_id = d.pop("pod_order_data_id")

        query_order_line = cls(
            order_line_id=order_line_id,
            product_id=product_id,
            sku_id=sku_id,
            pod_order_data_id=pod_order_data_id,
        )


        query_order_line.additional_properties = d
        return query_order_line

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
