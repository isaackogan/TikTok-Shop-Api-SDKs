from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSPSMetricDiagnosisResponseDataCalculationRule")



@_attrs_define
class GetSPSMetricDiagnosisResponseDataCalculationRule:
    """ 
        Attributes:
            denominator_label (str | Unset): Denominator label.
            denominator_value (str | Unset): Denominator value.
            numerator_label (str | Unset): Numerator label.
            numerator_value (str | Unset): Numerator value.
     """

    denominator_label: str | Unset = UNSET
    denominator_value: str | Unset = UNSET
    numerator_label: str | Unset = UNSET
    numerator_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        denominator_label = self.denominator_label

        denominator_value = self.denominator_value

        numerator_label = self.numerator_label

        numerator_value = self.numerator_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if denominator_label is not UNSET:
            field_dict["denominator_label"] = denominator_label
        if denominator_value is not UNSET:
            field_dict["denominator_value"] = denominator_value
        if numerator_label is not UNSET:
            field_dict["numerator_label"] = numerator_label
        if numerator_value is not UNSET:
            field_dict["numerator_value"] = numerator_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        denominator_label = d.pop("denominator_label", UNSET)

        denominator_value = d.pop("denominator_value", UNSET)

        numerator_label = d.pop("numerator_label", UNSET)

        numerator_value = d.pop("numerator_value", UNSET)

        get_sps_metric_diagnosis_response_data_calculation_rule = cls(
            denominator_label=denominator_label,
            denominator_value=denominator_value,
            numerator_label=numerator_label,
            numerator_value=numerator_value,
        )


        get_sps_metric_diagnosis_response_data_calculation_rule.additional_properties = d
        return get_sps_metric_diagnosis_response_data_calculation_rule

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
