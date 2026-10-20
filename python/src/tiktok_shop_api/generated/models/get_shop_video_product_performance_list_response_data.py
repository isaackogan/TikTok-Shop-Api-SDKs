from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_video_product_performance_list_response_data_product import (
        GetShopVideoProductPerformanceListResponseDataProduct,
    )


T = TypeVar("T", bound="GetShopVideoProductPerformanceListResponseData")


@_attrs_define
class GetShopVideoProductPerformanceListResponseData:
    """
    Attributes:
        latest_available_date (datetime.date | Unset): Latest date in local timezone where data is ready (ISO 8601
            format).
        next_page_token (str | Unset): Page token for the next page request. If this value is nonempty, pass it as
            `page_token` in the next request and reuse the same `video_id`, `start_date_ge`, `end_date_lt`, `sort_field`,
            `sort_order`, `currency`, and `page_size` values. An empty value means that there are no more pages.
        products (list[GetShopVideoProductPerformanceListResponseDataProduct] | Unset): List of product performance
            metrics.
        total_count (int | Unset): Total number of products matching the request across all pages.
    """

    latest_available_date: datetime.date | Unset = UNSET
    next_page_token: str | Unset = UNSET
    products: list[GetShopVideoProductPerformanceListResponseDataProduct] | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        next_page_token = self.next_page_token

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if products is not UNSET:
            field_dict["products"] = products
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_video_product_performance_list_response_data_product import (
            GetShopVideoProductPerformanceListResponseDataProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date, Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)

        next_page_token = d.pop("next_page_token", UNSET)

        _products = d.pop("products", UNSET)
        products: list[GetShopVideoProductPerformanceListResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = GetShopVideoProductPerformanceListResponseDataProduct.from_dict(products_item_data)

                products.append(products_item)

        total_count = d.pop("total_count", UNSET)

        get_shop_video_product_performance_list_response_data = cls(
            latest_available_date=latest_available_date,
            next_page_token=next_page_token,
            products=products,
            total_count=total_count,
        )

        get_shop_video_product_performance_list_response_data.additional_properties = d
        return get_shop_video_product_performance_list_response_data

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
