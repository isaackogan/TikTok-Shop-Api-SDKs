from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module import (
        GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModule,
    )


T = TypeVar("T", bound="GetCategoryAttributesResponseDataAttributeMetricStandard")


@_attrs_define
class GetCategoryAttributesResponseDataAttributeMetricStandard:
    """
    Attributes:
        id (str | Unset): The unique ID of the measurement template. Use this ID to identify which measurement standard
            template applies to the product.
        name (str | Unset): The name of the measurement template.
        metric_value_modules (list[GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModule] | Unset):
            Metric value modules.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    metric_value_modules: list[GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModule] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        metric_value_modules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metric_value_modules, Unset):
            metric_value_modules = []
            for metric_value_modules_item_data in self.metric_value_modules:
                metric_value_modules_item = metric_value_modules_item_data.to_dict()
                metric_value_modules.append(metric_value_modules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if metric_value_modules is not UNSET:
            field_dict["metric_value_modules"] = metric_value_modules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module import (
            GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModule,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _metric_value_modules = d.pop("metric_value_modules", UNSET)
        metric_value_modules: (
            list[GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModule] | Unset
        ) = UNSET
        if _metric_value_modules is not UNSET:
            metric_value_modules = []
            for metric_value_modules_item_data in _metric_value_modules:
                metric_value_modules_item = (
                    GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModule.from_dict(
                        metric_value_modules_item_data
                    )
                )

                metric_value_modules.append(metric_value_modules_item)

        get_category_attributes_response_data_attribute_metric_standard = cls(
            id=id,
            name=name,
            metric_value_modules=metric_value_modules,
        )

        get_category_attributes_response_data_attribute_metric_standard.additional_properties = d
        return get_category_attributes_response_data_attribute_metric_standard

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
