from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_category_attributes_response_data_attribute_type import GetCategoryAttributesResponseDataAttributeType
from ..models.get_category_attributes_response_data_attribute_value_data_format import (
    GetCategoryAttributesResponseDataAttributeValueDataFormat,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_category_attributes_response_data_attribute_metric_standard import (
        GetCategoryAttributesResponseDataAttributeMetricStandard,
    )
    from ..models.get_category_attributes_response_data_attribute_value import (
        GetCategoryAttributesResponseDataAttributeValue,
    )
    from ..models.requirement_condition import RequirementCondition


T = TypeVar("T", bound="GetCategoryAttributesResponseDataAttribute")


@_attrs_define
class GetCategoryAttributesResponseDataAttribute:
    """
    Attributes:
        id (str | Unset): The ID of the built-in attribute.
        name (str | Unset): The name of the built-in attribute.
        type_ (GetCategoryAttributesResponseDataAttributeType | Unset): The attribute type.
            Possible values:
            - SALES_PROPERTY: Indicates sales attributes that define product variants.
            - PRODUCT_PROPERTY: Indicates product attributes that describe the product as a whole.
        is_requried (bool | Unset): A flag to indicate if the product attribute is always required when creating or
            editing a product.
            - true: The attribute is always required.
            - false: The attribute is not required, or required only if certain conditions are met. Refer to
            `requirement_conditions` for the specific requirements.

            Applicable only if `type=PRODUCT_PROPERTY`.
        values (list[GetCategoryAttributesResponseDataAttributeValue] | Unset): A list of selectable values for the
            attribute.
        value_data_format (GetCategoryAttributesResponseDataAttributeValueDataFormat | Unset): The data format for a
            free-form attribute value.

            Returned for customizable numeric attributes.

            Possible values:
            - POSITIVE_INT_OR_DECIMAL: Positive integers or decimal numbers.
        is_customizable (bool | Unset): A flag indicating whether sellers can enter a custom value for the attribute
            when creating or editing a product.
        requirement_conditions (list[RequirementCondition] | Unset): A list of conditions that determine if the product
            attribute is required based on the seller's inputs for other attributes. If any of the conditions is met, the
            attribute is required; otherwise, it is optional.

            For example, there's a condition that states that the "Battery type" attribute is required if the seller selects
            the value "Batteries" for the attribute "Contains Batteries or Cells?". For more scenario-based guidance on
            using this parameter, refer to the [Solution Guide - CAT-PRE-
            HAZMAT](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985).

            Applicable only if `type=PRODUCT_PROPERTY` and `is_requried=false`.
        is_multiple_selection (bool | Unset): A flag indicating whether sellers can select multiple values for the
            attribute when creating or editing a product.
        metric_standards (list[GetCategoryAttributesResponseDataAttributeMetricStandard] | Unset): Defines the
            measurement template information used to describe the measurement standards and metric values configured for the
            product.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: GetCategoryAttributesResponseDataAttributeType | Unset = UNSET
    is_requried: bool | Unset = UNSET
    values: list[GetCategoryAttributesResponseDataAttributeValue] | Unset = UNSET
    value_data_format: GetCategoryAttributesResponseDataAttributeValueDataFormat | Unset = UNSET
    is_customizable: bool | Unset = UNSET
    requirement_conditions: list[RequirementCondition] | Unset = UNSET
    is_multiple_selection: bool | Unset = UNSET
    metric_standards: list[GetCategoryAttributesResponseDataAttributeMetricStandard] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        is_requried = self.is_requried

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        value_data_format: str | Unset = UNSET
        if not isinstance(self.value_data_format, Unset):
            value_data_format = self.value_data_format.value

        is_customizable = self.is_customizable

        requirement_conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requirement_conditions, Unset):
            requirement_conditions = []
            for requirement_conditions_item_data in self.requirement_conditions:
                requirement_conditions_item = requirement_conditions_item_data.to_dict()
                requirement_conditions.append(requirement_conditions_item)

        is_multiple_selection = self.is_multiple_selection

        metric_standards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metric_standards, Unset):
            metric_standards = []
            for metric_standards_item_data in self.metric_standards:
                metric_standards_item = metric_standards_item_data.to_dict()
                metric_standards.append(metric_standards_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_requried is not UNSET:
            field_dict["is_requried"] = is_requried
        if values is not UNSET:
            field_dict["values"] = values
        if value_data_format is not UNSET:
            field_dict["value_data_format"] = value_data_format
        if is_customizable is not UNSET:
            field_dict["is_customizable"] = is_customizable
        if requirement_conditions is not UNSET:
            field_dict["requirement_conditions"] = requirement_conditions
        if is_multiple_selection is not UNSET:
            field_dict["is_multiple_selection"] = is_multiple_selection
        if metric_standards is not UNSET:
            field_dict["metric_standards"] = metric_standards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_category_attributes_response_data_attribute_metric_standard import (
            GetCategoryAttributesResponseDataAttributeMetricStandard,  # noqa: PLC0415
        )
        from ..models.get_category_attributes_response_data_attribute_value import (
            GetCategoryAttributesResponseDataAttributeValue,  # noqa: PLC0415
        )
        from ..models.requirement_condition import RequirementCondition  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GetCategoryAttributesResponseDataAttributeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GetCategoryAttributesResponseDataAttributeType(_type_)

        is_requried = d.pop("is_requried", UNSET)

        _values = d.pop("values", UNSET)
        values: list[GetCategoryAttributesResponseDataAttributeValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = GetCategoryAttributesResponseDataAttributeValue.from_dict(values_item_data)

                values.append(values_item)

        _value_data_format = d.pop("value_data_format", UNSET)
        value_data_format: GetCategoryAttributesResponseDataAttributeValueDataFormat | Unset
        if isinstance(_value_data_format, Unset):
            value_data_format = UNSET
        else:
            value_data_format = GetCategoryAttributesResponseDataAttributeValueDataFormat(_value_data_format)

        is_customizable = d.pop("is_customizable", UNSET)

        _requirement_conditions = d.pop("requirement_conditions", UNSET)
        requirement_conditions: list[RequirementCondition] | Unset = UNSET
        if _requirement_conditions is not UNSET:
            requirement_conditions = []
            for requirement_conditions_item_data in _requirement_conditions:
                requirement_conditions_item = RequirementCondition.from_dict(requirement_conditions_item_data)

                requirement_conditions.append(requirement_conditions_item)

        is_multiple_selection = d.pop("is_multiple_selection", UNSET)

        _metric_standards = d.pop("metric_standards", UNSET)
        metric_standards: list[GetCategoryAttributesResponseDataAttributeMetricStandard] | Unset = UNSET
        if _metric_standards is not UNSET:
            metric_standards = []
            for metric_standards_item_data in _metric_standards:
                metric_standards_item = GetCategoryAttributesResponseDataAttributeMetricStandard.from_dict(
                    metric_standards_item_data
                )

                metric_standards.append(metric_standards_item)

        get_category_attributes_response_data_attribute = cls(
            id=id,
            name=name,
            type_=type_,
            is_requried=is_requried,
            values=values,
            value_data_format=value_data_format,
            is_customizable=is_customizable,
            requirement_conditions=requirement_conditions,
            is_multiple_selection=is_multiple_selection,
            metric_standards=metric_standards,
        )

        get_category_attributes_response_data_attribute.additional_properties = d
        return get_category_attributes_response_data_attribute

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
