from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_global_products_response_data_global_product import (
        SearchGlobalProductsResponseDataGlobalProduct,
    )


T = TypeVar("T", bound="SearchGlobalProductsResponseData")


@_attrs_define
class SearchGlobalProductsResponseData:
    """
    Attributes:
        next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. Provide
            this value in the `page_token` parameter of your request if the current response does not return all the
            results.
        total_count (int | Unset): The total number of global products that meet the query conditions.
        global_products (list[SearchGlobalProductsResponseDataGlobalProduct] | Unset): The list of global products that
            meet the query conditions.
    """

    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    global_products: list[SearchGlobalProductsResponseDataGlobalProduct] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        total_count = self.total_count

        global_products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.global_products, Unset):
            global_products = []
            for global_products_item_data in self.global_products:
                global_products_item = global_products_item_data.to_dict()
                global_products.append(global_products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if global_products is not UNSET:
            field_dict["global_products"] = global_products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_global_products_response_data_global_product import (
            SearchGlobalProductsResponseDataGlobalProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _global_products = d.pop("global_products", UNSET)
        global_products: list[SearchGlobalProductsResponseDataGlobalProduct] | Unset = UNSET
        if _global_products is not UNSET:
            global_products = []
            for global_products_item_data in _global_products:
                global_products_item = SearchGlobalProductsResponseDataGlobalProduct.from_dict(
                    global_products_item_data
                )

                global_products.append(global_products_item)

        search_global_products_response_data = cls(
            next_page_token=next_page_token,
            total_count=total_count,
            global_products=global_products,
        )

        search_global_products_response_data.additional_properties = d
        return search_global_products_response_data

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
