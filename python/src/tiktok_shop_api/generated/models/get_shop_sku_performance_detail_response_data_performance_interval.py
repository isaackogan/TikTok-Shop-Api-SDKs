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
  from ..models.get_shop_sku_performance_detail_response_data_performance_interval_gmv_breakdown import GetShopSKUPerformanceDetailResponseDataPerformanceIntervalGmvBreakdown
  from ..models.get_shop_sku_performance_detail_response_data_performance_interval_items_sold_breakdown import GetShopSKUPerformanceDetailResponseDataPerformanceIntervalItemsSoldBreakdown
  from ..models.gmv import Gmv





T = TypeVar("T", bound="GetShopSKUPerformanceDetailResponseDataPerformanceInterval")



@_attrs_define
class GetShopSKUPerformanceDetailResponseDataPerformanceInterval:
    """ 
        Attributes:
            start_date (datetime.date | Unset): Start date of the interval (ISO 8601 YYYY-MM-DD format) in shop registered
                timezone, inclusive.
            end_date (datetime.date | Unset): End date of the interval (ISO 8601 YYYY-MM-DD format) in shop registered
                timezone, exclusive.
            gmv (Gmv | Unset):
            gmv_breakdown (list[GetShopSKUPerformanceDetailResponseDataPerformanceIntervalGmvBreakdown] | Unset): GMV
                breakdowns for the SKU.
            items_sold (int | Unset): Number of units sold for the SKU.
            items_sold_breakdown (list[GetShopSKUPerformanceDetailResponseDataPerformanceIntervalItemsSoldBreakdown] |
                Unset): Unit sold breakdowns.
            sku_orders (int | Unset): Total (sum of all) orders for the SKU.
     """

    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    gmv_breakdown: list[GetShopSKUPerformanceDetailResponseDataPerformanceIntervalGmvBreakdown] | Unset = UNSET
    items_sold: int | Unset = UNSET
    items_sold_breakdown: list[GetShopSKUPerformanceDetailResponseDataPerformanceIntervalItemsSoldBreakdown] | Unset = UNSET
    sku_orders: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_sku_performance_detail_response_data_performance_interval_gmv_breakdown import GetShopSKUPerformanceDetailResponseDataPerformanceIntervalGmvBreakdown # noqa: PLC0415
        from ..models.get_shop_sku_performance_detail_response_data_performance_interval_items_sold_breakdown import GetShopSKUPerformanceDetailResponseDataPerformanceIntervalItemsSoldBreakdown # noqa: PLC0415
        from ..models.gmv import Gmv # noqa: PLC0415
        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        gmv_breakdown: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gmv_breakdown, Unset):
            gmv_breakdown = []
            for gmv_breakdown_item_data in self.gmv_breakdown:
                gmv_breakdown_item = gmv_breakdown_item_data.to_dict()
                gmv_breakdown.append(gmv_breakdown_item)



        items_sold = self.items_sold

        items_sold_breakdown: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items_sold_breakdown, Unset):
            items_sold_breakdown = []
            for items_sold_breakdown_item_data in self.items_sold_breakdown:
                items_sold_breakdown_item = items_sold_breakdown_item_data.to_dict()
                items_sold_breakdown.append(items_sold_breakdown_item)



        sku_orders = self.sku_orders


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if gmv_breakdown is not UNSET:
            field_dict["gmv_breakdown"] = gmv_breakdown
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if items_sold_breakdown is not UNSET:
            field_dict["items_sold_breakdown"] = items_sold_breakdown
        if sku_orders is not UNSET:
            field_dict["sku_orders"] = sku_orders

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_sku_performance_detail_response_data_performance_interval_gmv_breakdown import GetShopSKUPerformanceDetailResponseDataPerformanceIntervalGmvBreakdown # noqa: PLC0415
        from ..models.get_shop_sku_performance_detail_response_data_performance_interval_items_sold_breakdown import GetShopSKUPerformanceDetailResponseDataPerformanceIntervalItemsSoldBreakdown # noqa: PLC0415
        from ..models.gmv import Gmv # noqa: PLC0415
        d = dict(src_dict)
        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)




        _gmv_breakdown = d.pop("gmv_breakdown", UNSET)
        gmv_breakdown: list[GetShopSKUPerformanceDetailResponseDataPerformanceIntervalGmvBreakdown] | Unset = UNSET
        if _gmv_breakdown is not UNSET:
            gmv_breakdown = []
            for gmv_breakdown_item_data in _gmv_breakdown:
                gmv_breakdown_item = GetShopSKUPerformanceDetailResponseDataPerformanceIntervalGmvBreakdown.from_dict(gmv_breakdown_item_data)



                gmv_breakdown.append(gmv_breakdown_item)


        items_sold = d.pop("items_sold", UNSET)

        _items_sold_breakdown = d.pop("items_sold_breakdown", UNSET)
        items_sold_breakdown: list[GetShopSKUPerformanceDetailResponseDataPerformanceIntervalItemsSoldBreakdown] | Unset = UNSET
        if _items_sold_breakdown is not UNSET:
            items_sold_breakdown = []
            for items_sold_breakdown_item_data in _items_sold_breakdown:
                items_sold_breakdown_item = GetShopSKUPerformanceDetailResponseDataPerformanceIntervalItemsSoldBreakdown.from_dict(items_sold_breakdown_item_data)



                items_sold_breakdown.append(items_sold_breakdown_item)


        sku_orders = d.pop("sku_orders", UNSET)

        get_shop_sku_performance_detail_response_data_performance_interval = cls(
            start_date=start_date,
            end_date=end_date,
            gmv=gmv,
            gmv_breakdown=gmv_breakdown,
            items_sold=items_sold,
            items_sold_breakdown=items_sold_breakdown,
            sku_orders=sku_orders,
        )


        get_shop_sku_performance_detail_response_data_performance_interval.additional_properties = d
        return get_shop_sku_performance_detail_response_data_performance_interval

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
