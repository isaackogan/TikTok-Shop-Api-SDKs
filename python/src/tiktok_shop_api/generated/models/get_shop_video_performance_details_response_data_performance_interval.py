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
  from ..models.get_shop_video_performance_details_response_data_performance_interval_sale import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSale
  from ..models.get_shop_video_performance_details_response_data_performance_interval_traffic import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalTraffic





T = TypeVar("T", bound="GetShopVideoPerformanceDetailsResponseDataPerformanceInterval")



@_attrs_define
class GetShopVideoPerformanceDetailsResponseDataPerformanceInterval:
    """ 
        Attributes:
            start_date (datetime.date | Unset): Start date of the interval (ISO 8601 YYYY-MM-DD format) in shop registered
                timezone, inclusive.
            end_date (datetime.date | Unset): End date of the interval (ISO 8601 YYYY-MM-DD format) in shop registered
                timezone, exclusive.
            sales (GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSale | Unset):
            traffic (GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalTraffic | Unset):
     """

    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    sales: GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSale | Unset = UNSET
    traffic: GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalTraffic | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_video_performance_details_response_data_performance_interval_sale import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSale # noqa: PLC0415
        from ..models.get_shop_video_performance_details_response_data_performance_interval_traffic import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalTraffic # noqa: PLC0415
        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        sales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sales, Unset):
            sales = self.sales.to_dict()

        traffic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic, Unset):
            traffic = self.traffic.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if sales is not UNSET:
            field_dict["sales"] = sales
        if traffic is not UNSET:
            field_dict["traffic"] = traffic

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_video_performance_details_response_data_performance_interval_sale import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSale # noqa: PLC0415
        from ..models.get_shop_video_performance_details_response_data_performance_interval_traffic import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalTraffic # noqa: PLC0415
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




        _sales = d.pop("sales", UNSET)
        sales: GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSale | Unset
        if isinstance(_sales,  Unset):
            sales = UNSET
        else:
            sales = GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSale.from_dict(_sales)




        _traffic = d.pop("traffic", UNSET)
        traffic: GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalTraffic | Unset
        if isinstance(_traffic,  Unset):
            traffic = UNSET
        else:
            traffic = GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalTraffic.from_dict(_traffic)




        get_shop_video_performance_details_response_data_performance_interval = cls(
            start_date=start_date,
            end_date=end_date,
            sales=sales,
            traffic=traffic,
        )


        get_shop_video_performance_details_response_data_performance_interval.additional_properties = d
        return get_shop_video_performance_details_response_data_performance_interval

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
