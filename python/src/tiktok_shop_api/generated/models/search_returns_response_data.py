from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_returns_response_data_return_order import SearchReturnsResponseDataReturnOrder





T = TypeVar("T", bound="SearchReturnsResponseData")



@_attrs_define
class SearchReturnsResponseData:
    """ 
        Attributes:
            return_orders (list[SearchReturnsResponseDataReturnOrder] | Unset): List of returns in the current page. This
                field is omitted when the current page contains no return records.
            total_count (int | Unset): The number of returns that meet the query conditions.
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. If
                `next_page_token` is non-empty, provide it in the `page_token` parameter of the next request. If
                `next_page_token` is empty, stop pagination.
     """

    return_orders: list[SearchReturnsResponseDataReturnOrder] | Unset = UNSET
    total_count: int | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_returns_response_data_return_order import SearchReturnsResponseDataReturnOrder # noqa: PLC0415
        return_orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.return_orders, Unset):
            return_orders = []
            for return_orders_item_data in self.return_orders:
                return_orders_item = return_orders_item_data.to_dict()
                return_orders.append(return_orders_item)



        total_count = self.total_count

        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if return_orders is not UNSET:
            field_dict["return_orders"] = return_orders
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_returns_response_data_return_order import SearchReturnsResponseDataReturnOrder # noqa: PLC0415
        d = dict(src_dict)
        _return_orders = d.pop("return_orders", UNSET)
        return_orders: list[SearchReturnsResponseDataReturnOrder] | Unset = UNSET
        if _return_orders is not UNSET:
            return_orders = []
            for return_orders_item_data in _return_orders:
                return_orders_item = SearchReturnsResponseDataReturnOrder.from_dict(return_orders_item_data)



                return_orders.append(return_orders_item)


        total_count = d.pop("total_count", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        search_returns_response_data = cls(
            return_orders=return_orders,
            total_count=total_count,
            next_page_token=next_page_token,
        )


        search_returns_response_data.additional_properties = d
        return search_returns_response_data

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
