from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_videos_performance_details_response_data_video_performance_interval_sale import (
        GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSale,
    )
    from ..models.get_shop_videos_performance_details_response_data_video_performance_interval_traffic import (
        GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalTraffic,
    )


T = TypeVar("T", bound="GetShopVideosPerformanceDetailsResponseDataVideoPerformanceInterval")


@_attrs_define
class GetShopVideosPerformanceDetailsResponseDataVideoPerformanceInterval:
    """
    Attributes:
        end_date (datetime.date | Unset): End date of the interval, exclusive.
        sales (GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSale | Unset):
        start_date (datetime.date | Unset): Start date of the interval, inclusive.
        traffic (GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalTraffic | Unset):
    """

    end_date: datetime.date | Unset = UNSET
    sales: GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSale | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    traffic: GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalTraffic | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        sales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sales, Unset):
            sales = self.sales.to_dict()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        traffic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic, Unset):
            traffic = self.traffic.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if sales is not UNSET:
            field_dict["sales"] = sales
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if traffic is not UNSET:
            field_dict["traffic"] = traffic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_videos_performance_details_response_data_video_performance_interval_sale import (
            GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSale,  # noqa: PLC0415
        )
        from ..models.get_shop_videos_performance_details_response_data_video_performance_interval_traffic import (
            GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalTraffic,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)

        _sales = d.pop("sales", UNSET)
        sales: GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSale | Unset
        if isinstance(_sales, Unset):
            sales = UNSET
        else:
            sales = GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSale.from_dict(_sales)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)

        _traffic = d.pop("traffic", UNSET)
        traffic: GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalTraffic | Unset
        if isinstance(_traffic, Unset):
            traffic = UNSET
        else:
            traffic = GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalTraffic.from_dict(_traffic)

        get_shop_videos_performance_details_response_data_video_performance_interval = cls(
            end_date=end_date,
            sales=sales,
            start_date=start_date,
            traffic=traffic,
        )

        get_shop_videos_performance_details_response_data_video_performance_interval.additional_properties = d
        return get_shop_videos_performance_details_response_data_video_performance_interval

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
