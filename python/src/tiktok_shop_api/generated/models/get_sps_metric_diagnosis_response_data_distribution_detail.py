from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSPSMetricDiagnosisResponseDataDistributionDetail")



@_attrs_define
class GetSPSMetricDiagnosisResponseDataDistributionDetail:
    """ 
        Attributes:
            count (int | Unset): Number of items in the distribution bucket.
            name (str | Unset): Distribution detail name.
            percent (str | Unset): Percentage of items in the distribution bucket, from 0 to 100.
     """

    count: int | Unset = UNSET
    name: str | Unset = UNSET
    percent: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        name = self.name

        percent = self.percent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if name is not UNSET:
            field_dict["name"] = name
        if percent is not UNSET:
            field_dict["percent"] = percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        name = d.pop("name", UNSET)

        percent = d.pop("percent", UNSET)

        get_sps_metric_diagnosis_response_data_distribution_detail = cls(
            count=count,
            name=name,
            percent=percent,
        )


        get_sps_metric_diagnosis_response_data_distribution_detail.additional_properties = d
        return get_sps_metric_diagnosis_response_data_distribution_detail

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
