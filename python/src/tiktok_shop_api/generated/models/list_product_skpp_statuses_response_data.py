from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_product_skpp_statuses_response_data_product import ListProductSKPPStatusesResponseDataProduct





T = TypeVar("T", bound="ListProductSKPPStatusesResponseData")



@_attrs_define
class ListProductSKPPStatusesResponseData:
    """ 
        Attributes:
            products (list[ListProductSKPPStatusesResponseDataProduct] | Unset): Product list, each with its SKPP status.。
            total_count (int | Unset): Total products matching the filter.
            update_time (int | Unset): Date of the offline data snapshot that total_score and rewards are derived from,
                returned as a Unix timestamp in seconds, pinned to the last second of that date in UTC (23:59:59Z). The value is
                date-level only — the time component is always 23:59:59 UTC — because the SKPP scoring runs in an offline
                pipeline with no intraday granularity. Latency is typically T+1 (the evening of day N publishes the day N−1
                snapshot) and at most T+2.
     """

    products: list[ListProductSKPPStatusesResponseDataProduct] | Unset = UNSET
    total_count: int | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_product_skpp_statuses_response_data_product import ListProductSKPPStatusesResponseDataProduct # noqa: PLC0415
        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)



        total_count = self.total_count

        update_time = self.update_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if products is not UNSET:
            field_dict["products"] = products
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_product_skpp_statuses_response_data_product import ListProductSKPPStatusesResponseDataProduct # noqa: PLC0415
        d = dict(src_dict)
        _products = d.pop("products", UNSET)
        products: list[ListProductSKPPStatusesResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = ListProductSKPPStatusesResponseDataProduct.from_dict(products_item_data)



                products.append(products_item)


        total_count = d.pop("total_count", UNSET)

        update_time = d.pop("update_time", UNSET)

        list_product_skpp_statuses_response_data = cls(
            products=products,
            total_count=total_count,
            update_time=update_time,
        )


        list_product_skpp_statuses_response_data.additional_properties = d
        return list_product_skpp_statuses_response_data

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
