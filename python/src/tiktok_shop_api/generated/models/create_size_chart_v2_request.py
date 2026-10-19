from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_size_chart_v2_request_size_chart_data import CreateSizeChartV2RequestSizeChartData


T = TypeVar("T", bound="CreateSizeChartV2Request")


@_attrs_define
class CreateSizeChartV2Request:
    """
    Attributes:
        category_id (str): The leaf category for which to create the size chart. The category must support size charts.
        size_chart_data (CreateSizeChartV2RequestSizeChartData):
        size_chart_mode (str): Possible values:
            REUSABLE_TEMPLATE: A size chart template that can be reused across multiple products.
            PRODUCT_SCOPED: A size chart created for and used by a single product.
        template_name (str | Unset): Template name. Required when size_chart_mode is REUSABLE_TEMPLATE.
            When size_chart_mode is PRODUCT_SCOPED, any value provided for this field is discarded and is not stored.
    """

    category_id: str
    size_chart_data: CreateSizeChartV2RequestSizeChartData
    size_chart_mode: str
    template_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        size_chart_data = self.size_chart_data.to_dict()

        size_chart_mode = self.size_chart_mode

        template_name = self.template_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category_id": category_id,
                "size_chart_data": size_chart_data,
                "size_chart_mode": size_chart_mode,
            }
        )
        if template_name is not UNSET:
            field_dict["template_name"] = template_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_size_chart_v2_request_size_chart_data import (
            CreateSizeChartV2RequestSizeChartData,  # noqa: PLC0415
        )

        d = dict(src_dict)
        category_id = d.pop("category_id")

        size_chart_data = CreateSizeChartV2RequestSizeChartData.from_dict(d.pop("size_chart_data"))

        size_chart_mode = d.pop("size_chart_mode")

        template_name = d.pop("template_name", UNSET)

        create_size_chart_v2_request = cls(
            category_id=category_id,
            size_chart_data=size_chart_data,
            size_chart_mode=size_chart_mode,
            template_name=template_name,
        )

        create_size_chart_v2_request.additional_properties = d
        return create_size_chart_v2_request

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
