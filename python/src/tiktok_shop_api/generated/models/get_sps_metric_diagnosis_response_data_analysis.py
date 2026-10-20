from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetSPSMetricDiagnosisResponseDataAnalysis")



@_attrs_define
class GetSPSMetricDiagnosisResponseDataAnalysis:
    """ 
        Attributes:
            summaries (list[str] | Unset): Summarized causes affecting the selected metric.
            details (list[str] | Unset): Detailed explanations for the selected metric diagnosis.
     """

    summaries: list[str] | Unset = UNSET
    details: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        summaries: list[str] | Unset = UNSET
        if not isinstance(self.summaries, Unset):
            summaries = self.summaries



        details: list[str] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if summaries is not UNSET:
            field_dict["summaries"] = summaries
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        summaries = cast(list[str], d.pop("summaries", UNSET))


        details = cast(list[str], d.pop("details", UNSET))


        get_sps_metric_diagnosis_response_data_analysis = cls(
            summaries=summaries,
            details=details,
        )


        get_sps_metric_diagnosis_response_data_analysis.additional_properties = d
        return get_sps_metric_diagnosis_response_data_analysis

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
