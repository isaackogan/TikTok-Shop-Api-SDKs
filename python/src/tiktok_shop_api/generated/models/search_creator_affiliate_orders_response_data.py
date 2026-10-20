from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_creator_affiliate_orders_response_data_order import SearchCreatorAffiliateOrdersResponseDataOrder





T = TypeVar("T", bound="SearchCreatorAffiliateOrdersResponseData")



@_attrs_define
class SearchCreatorAffiliateOrdersResponseData:
    """ 
        Attributes:
            orders (list[SearchCreatorAffiliateOrdersResponseDataOrder] | Unset): The order resource.
            next_page_token (str | Unset): An opaque token used to retrieve the next page of results. Specify
                `create_time_ge` and `create_time_lt` in the first request and reuse the same values for every page. Pass a non-
                empty returned token as `page_token` in the next request. An empty value indicates the last page; stop
                requesting additional pages.
            total_count (int | Unset): The total number of SKU orders that match the search criteria. `page_size` limits
                SKU-order rows before they are grouped into `orders`; because one order can contain multiple SKUs, the number of
                returned order objects can be less than `page_size`. Use `next_page_token` to continue pagination.
     """

    orders: list[SearchCreatorAffiliateOrdersResponseDataOrder] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_creator_affiliate_orders_response_data_order import SearchCreatorAffiliateOrdersResponseDataOrder # noqa: PLC0415
        orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)



        next_page_token = self.next_page_token

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if orders is not UNSET:
            field_dict["orders"] = orders
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_creator_affiliate_orders_response_data_order import SearchCreatorAffiliateOrdersResponseDataOrder # noqa: PLC0415
        d = dict(src_dict)
        _orders = d.pop("orders", UNSET)
        orders: list[SearchCreatorAffiliateOrdersResponseDataOrder] | Unset = UNSET
        if _orders is not UNSET:
            orders = []
            for orders_item_data in _orders:
                orders_item = SearchCreatorAffiliateOrdersResponseDataOrder.from_dict(orders_item_data)



                orders.append(orders_item)


        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        search_creator_affiliate_orders_response_data = cls(
            orders=orders,
            next_page_token=next_page_token,
            total_count=total_count,
        )


        search_creator_affiliate_orders_response_data.additional_properties = d
        return search_creator_affiliate_orders_response_data

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
