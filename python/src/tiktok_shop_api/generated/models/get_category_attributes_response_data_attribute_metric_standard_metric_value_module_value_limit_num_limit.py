from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitNumLimit")


@_attrs_define
class GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitNumLimit:
    """
    Attributes:
        min_value (int | Unset): Metric value num limit min value.
        max_value (int | Unset): Metric value num limit max value.
    """

    min_value: int | Unset = UNSET
    max_value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_value = self.min_value

        max_value = self.max_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_value = d.pop("min_value", UNSET)

        max_value = d.pop("max_value", UNSET)

        get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_num_limit = cls(
            min_value=min_value,
            max_value=max_value,
        )

        get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_num_limit.additional_properties = d
        return get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_num_limit

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
