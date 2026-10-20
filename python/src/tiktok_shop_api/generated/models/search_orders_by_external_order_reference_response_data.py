from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_orders_by_external_order_reference_response_data_order import SearchOrdersByExternalOrderReferenceResponseDataOrder





T = TypeVar("T", bound="SearchOrdersByExternalOrderReferenceResponseData")



@_attrs_define
class SearchOrdersByExternalOrderReferenceResponseData:
    """ 
        Attributes:
            orders (list[SearchOrdersByExternalOrderReferenceResponseDataOrder] | Unset): A list of TikTok Shop orders that
                match the specified external order ID and OMS platform. This field may be omitted when no orders match.
     """

    orders: list[SearchOrdersByExternalOrderReferenceResponseDataOrder] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_orders_by_external_order_reference_response_data_order import SearchOrdersByExternalOrderReferenceResponseDataOrder # noqa: PLC0415
        orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_orders_by_external_order_reference_response_data_order import SearchOrdersByExternalOrderReferenceResponseDataOrder # noqa: PLC0415
        d = dict(src_dict)
        _orders = d.pop("orders", UNSET)
        orders: list[SearchOrdersByExternalOrderReferenceResponseDataOrder] | Unset = UNSET
        if _orders is not UNSET:
            orders = []
            for orders_item_data in _orders:
                orders_item = SearchOrdersByExternalOrderReferenceResponseDataOrder.from_dict(orders_item_data)



                orders.append(orders_item)


        search_orders_by_external_order_reference_response_data = cls(
            orders=orders,
        )


        search_orders_by_external_order_reference_response_data.additional_properties = d
        return search_orders_by_external_order_reference_response_data

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
