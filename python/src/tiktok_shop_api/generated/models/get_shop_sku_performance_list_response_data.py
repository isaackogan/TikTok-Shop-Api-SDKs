from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_shop_sku_performance_list_response_data_sku import GetShopSKUPerformanceListResponseDataSku





T = TypeVar("T", bound="GetShopSKUPerformanceListResponseData")



@_attrs_define
class GetShopSKUPerformanceListResponseData:
    """ 
        Attributes:
            skus (list[GetShopSKUPerformanceListResponseDataSku] | Unset): List of SKU performance metrics.
            next_page_token (str | Unset): If nonempty, pass this token unchanged as `page_token` in the next request and
                reuse the same `start_date_ge`, `end_date_lt`, `page_size`, `sort_field`, `sort_order`, `currency`,
                `category_filter`, `product_status_filter`, and `product_ids` values. For optional parameters, preserve whether
                each parameter was omitted or present. An empty string means there are no more pages.
            total_count (int | Unset): Total number of SKUs matching the request filters across all pages.
            latest_available_date (datetime.date | Unset): Latest date in local timezone where data is ready (ISO 8601
                format).
     """

    skus: list[GetShopSKUPerformanceListResponseDataSku] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_sku_performance_list_response_data_sku import GetShopSKUPerformanceListResponseDataSku # noqa: PLC0415
        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)



        next_page_token = self.next_page_token

        total_count = self.total_count

        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if skus is not UNSET:
            field_dict["skus"] = skus
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_sku_performance_list_response_data_sku import GetShopSKUPerformanceListResponseDataSku # noqa: PLC0415
        d = dict(src_dict)
        _skus = d.pop("skus", UNSET)
        skus: list[GetShopSKUPerformanceListResponseDataSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = GetShopSKUPerformanceListResponseDataSku.from_dict(skus_item_data)



                skus.append(skus_item)


        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date,  Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)




        get_shop_sku_performance_list_response_data = cls(
            skus=skus,
            next_page_token=next_page_token,
            total_count=total_count,
            latest_available_date=latest_available_date,
        )


        get_shop_sku_performance_list_response_data.additional_properties = d
        return get_shop_sku_performance_list_response_data

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
