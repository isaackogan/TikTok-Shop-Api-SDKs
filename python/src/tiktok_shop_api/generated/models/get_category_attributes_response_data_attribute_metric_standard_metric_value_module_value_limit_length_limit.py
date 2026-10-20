from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitLengthLimit")



@_attrs_define
class GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitLengthLimit:
    """ 
        Attributes:
            min_length (int | Unset): Metric value min length.
            max_length (int | Unset): Metric value max length.
     """

    min_length: int | Unset = UNSET
    max_length: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_length = self.min_length

        max_length = self.max_length


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_length is not UNSET:
            field_dict["min_length"] = min_length
        if max_length is not UNSET:
            field_dict["max_length"] = max_length

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_length = d.pop("min_length", UNSET)

        max_length = d.pop("max_length", UNSET)

        get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_length_limit = cls(
            min_length=min_length,
            max_length=max_length,
        )


        get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_length_limit.additional_properties = d
        return get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_length_limit

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
