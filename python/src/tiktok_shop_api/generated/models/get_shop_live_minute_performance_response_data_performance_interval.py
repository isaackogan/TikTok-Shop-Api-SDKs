from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shop_live_minute_performance_response_data_performance_interval_conversion import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversion
  from ..models.get_shop_live_minute_performance_response_data_performance_interval_interaction import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalInteraction
  from ..models.get_shop_live_minute_performance_response_data_performance_interval_sale import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalSale
  from ..models.get_shop_live_minute_performance_response_data_performance_interval_traffic import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalTraffic





T = TypeVar("T", bound="GetShopLIVEMinutePerformanceResponseDataPerformanceInterval")



@_attrs_define
class GetShopLIVEMinutePerformanceResponseDataPerformanceInterval:
    """ 
        Attributes:
            start_time (int | Unset): Start time of this interval as a Unix timestamp in seconds (UTC).
            end_time (int | Unset): End time of this interval as a Unix timestamp in seconds (UTC).
            sales (GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalSale | Unset):
            traffic (GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalTraffic | Unset):
            interactions (GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalInteraction | Unset):
            conversion (GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversion | Unset):
     """

    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    sales: GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalSale | Unset = UNSET
    traffic: GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalTraffic | Unset = UNSET
    interactions: GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalInteraction | Unset = UNSET
    conversion: GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_live_minute_performance_response_data_performance_interval_conversion import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversion # noqa: PLC0415
        from ..models.get_shop_live_minute_performance_response_data_performance_interval_interaction import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalInteraction # noqa: PLC0415
        from ..models.get_shop_live_minute_performance_response_data_performance_interval_sale import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalSale # noqa: PLC0415
        from ..models.get_shop_live_minute_performance_response_data_performance_interval_traffic import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalTraffic # noqa: PLC0415
        start_time = self.start_time

        end_time = self.end_time

        sales: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sales, Unset):
            sales = self.sales.to_dict()

        traffic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic, Unset):
            traffic = self.traffic.to_dict()

        interactions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interactions, Unset):
            interactions = self.interactions.to_dict()

        conversion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conversion, Unset):
            conversion = self.conversion.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if sales is not UNSET:
            field_dict["sales"] = sales
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if interactions is not UNSET:
            field_dict["interactions"] = interactions
        if conversion is not UNSET:
            field_dict["conversion"] = conversion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_live_minute_performance_response_data_performance_interval_conversion import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversion # noqa: PLC0415
        from ..models.get_shop_live_minute_performance_response_data_performance_interval_interaction import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalInteraction # noqa: PLC0415
        from ..models.get_shop_live_minute_performance_response_data_performance_interval_sale import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalSale # noqa: PLC0415
        from ..models.get_shop_live_minute_performance_response_data_performance_interval_traffic import GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalTraffic # noqa: PLC0415
        d = dict(src_dict)
        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        _sales = d.pop("sales", UNSET)
        sales: GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalSale | Unset
        if isinstance(_sales,  Unset):
            sales = UNSET
        else:
            sales = GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalSale.from_dict(_sales)




        _traffic = d.pop("traffic", UNSET)
        traffic: GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalTraffic | Unset
        if isinstance(_traffic,  Unset):
            traffic = UNSET
        else:
            traffic = GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalTraffic.from_dict(_traffic)




        _interactions = d.pop("interactions", UNSET)
        interactions: GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalInteraction | Unset
        if isinstance(_interactions,  Unset):
            interactions = UNSET
        else:
            interactions = GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalInteraction.from_dict(_interactions)




        _conversion = d.pop("conversion", UNSET)
        conversion: GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversion | Unset
        if isinstance(_conversion,  Unset):
            conversion = UNSET
        else:
            conversion = GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalConversion.from_dict(_conversion)




        get_shop_live_minute_performance_response_data_performance_interval = cls(
            start_time=start_time,
            end_time=end_time,
            sales=sales,
            traffic=traffic,
            interactions=interactions,
            conversion=conversion,
        )


        get_shop_live_minute_performance_response_data_performance_interval.additional_properties = d
        return get_shop_live_minute_performance_response_data_performance_interval

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
