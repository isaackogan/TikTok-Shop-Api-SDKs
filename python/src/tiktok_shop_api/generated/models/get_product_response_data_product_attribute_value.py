from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_product_response_data_product_attribute_value_metric_standard_info import GetProductResponseDataProductAttributeValueMetricStandardInfo





T = TypeVar("T", bound="GetProductResponseDataProductAttributeValue")



@_attrs_define
class GetProductResponseDataProductAttributeValue:
    """ 
        Attributes:
            id (str | Unset): The product attribute value ID.
            name (str | Unset): The product attribute value name.
            metric_standard_info (GetProductResponseDataProductAttributeValueMetricStandardInfo | Unset):
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    metric_standard_info: GetProductResponseDataProductAttributeValueMetricStandardInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_response_data_product_attribute_value_metric_standard_info import GetProductResponseDataProductAttributeValueMetricStandardInfo # noqa: PLC0415
        id = self.id

        name = self.name

        metric_standard_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metric_standard_info, Unset):
            metric_standard_info = self.metric_standard_info.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if metric_standard_info is not UNSET:
            field_dict["metric_standard_info"] = metric_standard_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_response_data_product_attribute_value_metric_standard_info import GetProductResponseDataProductAttributeValueMetricStandardInfo # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _metric_standard_info = d.pop("metric_standard_info", UNSET)
        metric_standard_info: GetProductResponseDataProductAttributeValueMetricStandardInfo | Unset
        if isinstance(_metric_standard_info,  Unset):
            metric_standard_info = UNSET
        else:
            metric_standard_info = GetProductResponseDataProductAttributeValueMetricStandardInfo.from_dict(_metric_standard_info)




        get_product_response_data_product_attribute_value = cls(
            id=id,
            name=name,
            metric_standard_info=metric_standard_info,
        )


        get_product_response_data_product_attribute_value.additional_properties = d
        return get_product_response_data_product_attribute_value

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
