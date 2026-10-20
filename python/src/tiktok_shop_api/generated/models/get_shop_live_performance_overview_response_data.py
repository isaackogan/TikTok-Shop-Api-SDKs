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
  from ..models.get_shop_live_performance_overview_response_data_performance import GetShopLIVEPerformanceOverviewResponseDataPerformance





T = TypeVar("T", bound="GetShopLIVEPerformanceOverviewResponseData")



@_attrs_define
class GetShopLIVEPerformanceOverviewResponseData:
    """ 
        Attributes:
            latest_available_date (datetime.date | Unset): Latest date in local timezone where data is ready (ISO 8601
                format).
            performance (GetShopLIVEPerformanceOverviewResponseDataPerformance | Unset):
            updated_at (str | Unset): Time when the data was last updated in shop registered timezone.
     """

    latest_available_date: datetime.date | Unset = UNSET
    performance: GetShopLIVEPerformanceOverviewResponseDataPerformance | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_live_performance_overview_response_data_performance import GetShopLIVEPerformanceOverviewResponseDataPerformance # noqa: PLC0415
        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.performance, Unset):
            performance = self.performance.to_dict()

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if performance is not UNSET:
            field_dict["performance"] = performance
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_live_performance_overview_response_data_performance import GetShopLIVEPerformanceOverviewResponseDataPerformance # noqa: PLC0415
        d = dict(src_dict)
        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date,  Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)




        _performance = d.pop("performance", UNSET)
        performance: GetShopLIVEPerformanceOverviewResponseDataPerformance | Unset
        if isinstance(_performance,  Unset):
            performance = UNSET
        else:
            performance = GetShopLIVEPerformanceOverviewResponseDataPerformance.from_dict(_performance)




        updated_at = d.pop("updated_at", UNSET)

        get_shop_live_performance_overview_response_data = cls(
            latest_available_date=latest_available_date,
            performance=performance,
            updated_at=updated_at,
        )


        get_shop_live_performance_overview_response_data.additional_properties = d
        return get_shop_live_performance_overview_response_data

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
