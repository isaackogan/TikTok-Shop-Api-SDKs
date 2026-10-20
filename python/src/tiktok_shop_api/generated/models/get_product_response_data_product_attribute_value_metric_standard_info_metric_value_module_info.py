from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataProductAttributeValueMetricStandardInfoMetricValueModuleInfo")


@_attrs_define
class GetProductResponseDataProductAttributeValueMetricStandardInfoMetricValueModuleInfo:
    """
    Attributes:
        id (str | Unset): The unique ID of a metric item within the measurement template. This ID identifies which
            metric the submitted value belongs to.
        value (str | Unset): The seller-provided value for the specified metric item in the measurement template.
        unit_id (str | Unset): Metric value module unit id.
        unit_name (str | Unset): Metric value module unit name.
        suffix (str | Unset): Metric value suffix.
        prefix (str | Unset): Metric value prefix.
    """

    id: str | Unset = UNSET
    value: str | Unset = UNSET
    unit_id: str | Unset = UNSET
    unit_name: str | Unset = UNSET
    suffix: str | Unset = UNSET
    prefix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value = self.value

        unit_id = self.unit_id

        unit_name = self.unit_name

        suffix = self.suffix

        prefix = self.prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if value is not UNSET:
            field_dict["value"] = value
        if unit_id is not UNSET:
            field_dict["unit_id"] = unit_id
        if unit_name is not UNSET:
            field_dict["unit_name"] = unit_name
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if prefix is not UNSET:
            field_dict["prefix"] = prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        value = d.pop("value", UNSET)

        unit_id = d.pop("unit_id", UNSET)

        unit_name = d.pop("unit_name", UNSET)

        suffix = d.pop("suffix", UNSET)

        prefix = d.pop("prefix", UNSET)

        get_product_response_data_product_attribute_value_metric_standard_info_metric_value_module_info = cls(
            id=id,
            value=value,
            unit_id=unit_id,
            unit_name=unit_name,
            suffix=suffix,
            prefix=prefix,
        )

        get_product_response_data_product_attribute_value_metric_standard_info_metric_value_module_info.additional_properties = d
        return get_product_response_data_product_attribute_value_metric_standard_info_metric_value_module_info

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
