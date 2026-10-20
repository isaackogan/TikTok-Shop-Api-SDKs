from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_length_limit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitLengthLimit
  from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_num_limit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitNumLimit





T = TypeVar("T", bound="GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimit")



@_attrs_define
class GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimit:
    """ 
        Attributes:
            num_limit (GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitNumLimit | Unset):
            length_limit (GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitLengthLimit |
                Unset):
     """

    num_limit: GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitNumLimit | Unset = UNSET
    length_limit: GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitLengthLimit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_length_limit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitLengthLimit # noqa: PLC0415
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_num_limit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitNumLimit # noqa: PLC0415
        num_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.num_limit, Unset):
            num_limit = self.num_limit.to_dict()

        length_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.length_limit, Unset):
            length_limit = self.length_limit.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if num_limit is not UNSET:
            field_dict["num_limit"] = num_limit
        if length_limit is not UNSET:
            field_dict["length_limit"] = length_limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_length_limit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitLengthLimit # noqa: PLC0415
        from ..models.get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit_num_limit import GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitNumLimit # noqa: PLC0415
        d = dict(src_dict)
        _num_limit = d.pop("num_limit", UNSET)
        num_limit: GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitNumLimit | Unset
        if isinstance(_num_limit,  Unset):
            num_limit = UNSET
        else:
            num_limit = GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitNumLimit.from_dict(_num_limit)




        _length_limit = d.pop("length_limit", UNSET)
        length_limit: GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitLengthLimit | Unset
        if isinstance(_length_limit,  Unset):
            length_limit = UNSET
        else:
            length_limit = GetCategoryAttributesResponseDataAttributeMetricStandardMetricValueModuleValueLimitLengthLimit.from_dict(_length_limit)




        get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit = cls(
            num_limit=num_limit,
            length_limit=length_limit,
        )


        get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit.additional_properties = d
        return get_category_attributes_response_data_attribute_metric_standard_metric_value_module_value_limit

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
