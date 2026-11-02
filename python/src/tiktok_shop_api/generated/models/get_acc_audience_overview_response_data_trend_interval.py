from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GetACCAudienceOverviewResponseDataTrendInterval")



@_attrs_define
class GetACCAudienceOverviewResponseDataTrendInterval:
    """ 
        Attributes:
            benchmark (int | Unset): Average audience count for this metric and date among the selected industry's top N
                brands, where N is the benchmark request parameter. Unit: people.
            date (datetime.date | Unset): UTC date of this data point, in `YYYY-MM-DD` format.
            value (int | Unset): Audience count for this metric on the data point date.
     """

    benchmark: int | Unset = UNSET
    date: datetime.date | Unset = UNSET
    value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        benchmark = self.benchmark

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if benchmark is not UNSET:
            field_dict["benchmark"] = benchmark
        if date is not UNSET:
            field_dict["date"] = date
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        benchmark = d.pop("benchmark", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date,  Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)




        value = d.pop("value", UNSET)

        get_acc_audience_overview_response_data_trend_interval = cls(
            benchmark=benchmark,
            date=date,
            value=value,
        )


        get_acc_audience_overview_response_data_trend_interval.additional_properties = d
        return get_acc_audience_overview_response_data_trend_interval

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
