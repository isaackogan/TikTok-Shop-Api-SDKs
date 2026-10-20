from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateSizeChartV2ResponseData")



@_attrs_define
class CreateSizeChartV2ResponseData:
    """ 
        Attributes:
            size_chart_id (str | Unset): The ID of the created size chart. For REUSABLE_TEMPLATE mode, use this value as
                size_chart.template.id in subsequent product APIs. For PRODUCT_SCOPED mode, this ID identifies a size chart
                specific to a single product and cannot be reused as a template ID.
     """

    size_chart_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        size_chart_id = self.size_chart_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if size_chart_id is not UNSET:
            field_dict["size_chart_id"] = size_chart_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        size_chart_id = d.pop("size_chart_id", UNSET)

        create_size_chart_v2_response_data = cls(
            size_chart_id=size_chart_id,
        )


        create_size_chart_v2_response_data.additional_properties = d
        return create_size_chart_v2_response_data

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
