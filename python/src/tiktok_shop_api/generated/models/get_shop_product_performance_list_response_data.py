from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_product_performance_list_response_data_product import (
        GetShopProductPerformanceListResponseDataProduct,
    )


T = TypeVar("T", bound="GetShopProductPerformanceListResponseData")


@_attrs_define
class GetShopProductPerformanceListResponseData:
    """
    Attributes:
        products (list[GetShopProductPerformanceListResponseDataProduct] | Unset): List of product performance metrics.
        next_page_token (str | Unset): Page token for the next page. Pass this value as `page_token` in the next request
            and reuse the same `start_date_ge`, `end_date_lt`, `sort_field`, `sort_order`, `currency`, `category_filter`,
            `product_status_filter`, and `page_size` values. An empty value means there is no next page.
        total_count (int | Unset): Total number of products that match the request filters across all pages.
        latest_available_date (datetime.date | Unset): Latest date in local timezone where data is ready (ISO 8601
            format).
    """

    products: list[GetShopProductPerformanceListResponseDataProduct] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        next_page_token = self.next_page_token

        total_count = self.total_count

        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if products is not UNSET:
            field_dict["products"] = products
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_product_performance_list_response_data_product import (
            GetShopProductPerformanceListResponseDataProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _products = d.pop("products", UNSET)
        products: list[GetShopProductPerformanceListResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = GetShopProductPerformanceListResponseDataProduct.from_dict(products_item_data)

                products.append(products_item)

        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date, Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)

        get_shop_product_performance_list_response_data = cls(
            products=products,
            next_page_token=next_page_token,
            total_count=total_count,
            latest_available_date=latest_available_date,
        )

        get_shop_product_performance_list_response_data.additional_properties = d
        return get_shop_product_performance_list_response_data

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
