from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetACCAudienceOverviewResponseDataKeyMetricConversion")



@_attrs_define
class GetACCAudienceOverviewResponseDataKeyMetricConversion:
    """ 
        Attributes:
            benchmark (int | Unset): Average audience count for this metric among the selected industry's top N brands,
                where N is the benchmark request parameter. Unit: people.
            dod_change_rate (str | Unset): Percentage change in this audience count from the previous UTC calendar day,
                calculated as (current - previous) / previous * 100 and returned as a percentage string, for example "9.21%".
                Unavailable when comparison data is unavailable or the previous count is zero.
            value (int | Unset): Audience count for this metric on the selected date.
     """

    benchmark: int | Unset = UNSET
    dod_change_rate: str | Unset = UNSET
    value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        benchmark = self.benchmark

        dod_change_rate = self.dod_change_rate

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if benchmark is not UNSET:
            field_dict["benchmark"] = benchmark
        if dod_change_rate is not UNSET:
            field_dict["dod_change_rate"] = dod_change_rate
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        benchmark = d.pop("benchmark", UNSET)

        dod_change_rate = d.pop("dod_change_rate", UNSET)

        value = d.pop("value", UNSET)

        get_acc_audience_overview_response_data_key_metric_conversion = cls(
            benchmark=benchmark,
            dod_change_rate=dod_change_rate,
            value=value,
        )


        get_acc_audience_overview_response_data_key_metric_conversion.additional_properties = d
        return get_acc_audience_overview_response_data_key_metric_conversion

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
