from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_product_response_data_product_attribute_value_metric_standard_info_metric_value_module_info import (
        GetProductResponseDataProductAttributeValueMetricStandardInfoMetricValueModuleInfo,
    )


T = TypeVar("T", bound="GetProductResponseDataProductAttributeValueMetricStandardInfo")


@_attrs_define
class GetProductResponseDataProductAttributeValueMetricStandardInfo:
    """
    Attributes:
        id (str | Unset): The unique ID of the measurement template. Use this ID to identify which measurement standard
            template applies to the product.
        metric_value_module_infos
            (list[GetProductResponseDataProductAttributeValueMetricStandardInfoMetricValueModuleInfo] | Unset): The list of
            metric value entries under the measurement template. Each object represents the value submitted by the seller
            for a specific metric in the template.
    """

    id: str | Unset = UNSET
    metric_value_module_infos: (
        list[GetProductResponseDataProductAttributeValueMetricStandardInfoMetricValueModuleInfo] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        metric_value_module_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metric_value_module_infos, Unset):
            metric_value_module_infos = []
            for metric_value_module_infos_item_data in self.metric_value_module_infos:
                metric_value_module_infos_item = metric_value_module_infos_item_data.to_dict()
                metric_value_module_infos.append(metric_value_module_infos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if metric_value_module_infos is not UNSET:
            field_dict["metric_value_module_infos"] = metric_value_module_infos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_response_data_product_attribute_value_metric_standard_info_metric_value_module_info import (
            GetProductResponseDataProductAttributeValueMetricStandardInfoMetricValueModuleInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _metric_value_module_infos = d.pop("metric_value_module_infos", UNSET)
        metric_value_module_infos: (
            list[GetProductResponseDataProductAttributeValueMetricStandardInfoMetricValueModuleInfo] | Unset
        ) = UNSET
        if _metric_value_module_infos is not UNSET:
            metric_value_module_infos = []
            for metric_value_module_infos_item_data in _metric_value_module_infos:
                metric_value_module_infos_item = (
                    GetProductResponseDataProductAttributeValueMetricStandardInfoMetricValueModuleInfo.from_dict(
                        metric_value_module_infos_item_data
                    )
                )

                metric_value_module_infos.append(metric_value_module_infos_item)

        get_product_response_data_product_attribute_value_metric_standard_info = cls(
            id=id,
            metric_value_module_infos=metric_value_module_infos,
        )

        get_product_response_data_product_attribute_value_metric_standard_info.additional_properties = d
        return get_product_response_data_product_attribute_value_metric_standard_info

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
