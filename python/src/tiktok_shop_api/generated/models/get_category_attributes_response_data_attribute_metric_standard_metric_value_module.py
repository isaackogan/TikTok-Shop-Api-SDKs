from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_default_value import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleDefaultValue
  from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_unit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleUnit
  from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimit





T = TypeVar("T", bound="GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModule")



@_attrs_define
class GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModule:
    """ 
        Attributes:
            id (str | Unset): The unique ID of a metric item within the measurement template. This ID identifies which
                metric the submitted value belongs to.
            name (str | Unset): The seller-provided value for the specified metric item in the measurement template.
            input_type (str | Unset): Metric value modules input type.
            data_types (list[str] | Unset): Metric value modules data type.
            default_values (list[GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleDefaultValue] |
                Unset): Metric value modules default values.
            units (list[GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleUnit] | Unset): Metric
                value modules units.
            value_limit (GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimit | Unset):
            prefix (str | Unset): Metric value prefix.
            suffix (str | Unset): Metric value suffix.
            shading_word (str | Unset): Metric value shading word.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    input_type: str | Unset = UNSET
    data_types: list[str] | Unset = UNSET
    default_values: list[GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleDefaultValue] | Unset = UNSET
    units: list[GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleUnit] | Unset = UNSET
    value_limit: GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimit | Unset = UNSET
    prefix: str | Unset = UNSET
    suffix: str | Unset = UNSET
    shading_word: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_default_value import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleDefaultValue # noqa: PLC0415
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_unit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleUnit # noqa: PLC0415
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimit # noqa: PLC0415
        id = self.id

        name = self.name

        input_type = self.input_type

        data_types: list[str] | Unset = UNSET
        if not isinstance(self.data_types, Unset):
            data_types = self.data_types



        default_values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.default_values, Unset):
            default_values = []
            for default_values_item_data in self.default_values:
                default_values_item = default_values_item_data.to_dict()
                default_values.append(default_values_item)



        units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.units, Unset):
            units = []
            for units_item_data in self.units:
                units_item = units_item_data.to_dict()
                units.append(units_item)



        value_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value_limit, Unset):
            value_limit = self.value_limit.to_dict()

        prefix = self.prefix

        suffix = self.suffix

        shading_word = self.shading_word


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if input_type is not UNSET:
            field_dict["input_type"] = input_type
        if data_types is not UNSET:
            field_dict["data_types"] = data_types
        if default_values is not UNSET:
            field_dict["default_values"] = default_values
        if units is not UNSET:
            field_dict["units"] = units
        if value_limit is not UNSET:
            field_dict["value_limit"] = value_limit
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if shading_word is not UNSET:
            field_dict["shading_word"] = shading_word

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_default_value import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleDefaultValue # noqa: PLC0415
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_unit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleUnit # noqa: PLC0415
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimit # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        input_type = d.pop("input_type", UNSET)

        data_types = cast(list[str], d.pop("data_types", UNSET))


        _default_values = d.pop("default_values", UNSET)
        default_values: list[GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleDefaultValue] | Unset = UNSET
        if _default_values is not UNSET:
            default_values = []
            for default_values_item_data in _default_values:
                default_values_item = GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleDefaultValue.from_dict(default_values_item_data)



                default_values.append(default_values_item)


        _units = d.pop("units", UNSET)
        units: list[GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleUnit] | Unset = UNSET
        if _units is not UNSET:
            units = []
            for units_item_data in _units:
                units_item = GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleUnit.from_dict(units_item_data)



                units.append(units_item)


        _value_limit = d.pop("value_limit", UNSET)
        value_limit: GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimit | Unset
        if isinstance(_value_limit,  Unset):
            value_limit = UNSET
        else:
            value_limit = GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimit.from_dict(_value_limit)




        prefix = d.pop("prefix", UNSET)

        suffix = d.pop("suffix", UNSET)

        shading_word = d.pop("shading_word", UNSET)

        get_category_attributes_response_data_attribute_metric_standard_metric_value_module = cls(
            id=id,
            name=name,
            input_type=input_type,
            data_types=data_types,
            default_values=default_values,
            units=units,
            value_limit=value_limit,
            prefix=prefix,
            suffix=suffix,
            shading_word=shading_word,
        )


        get_category_attributes_response_data_attribute_metric_standard_metric_value_module.additional_properties = d
        return get_category_attributes_response_data_attribute_metric_standard_metric_value_module

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
