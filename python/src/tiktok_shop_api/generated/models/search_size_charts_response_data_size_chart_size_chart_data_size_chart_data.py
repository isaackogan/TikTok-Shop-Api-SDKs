from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table import SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTable





T = TypeVar("T", bound="SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartData")



@_attrs_define
class SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartData:
    """ 
        Attributes:
            table (SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTable | Unset):
            description (str | Unset): Additional size chart description.
            is_one_size (bool | Unset): Whether this is a one-size chart.
            measurement_type (str | Unset): Possible values: GENERIC_MEASUREMENTS: generic measurements; BODY_MEASUREMENTS:
                shopper body measurements; PRODUCT_MEASUREMENTS: finished-product measurements.
            unit_system (str | Unset): Possible values: METRIC: metric units; IMPERIAL: imperial units.
            size_types (list[str] | Unset): Possible values include: size_chart_common_size_type: Common;
                size_chart_size_type_regular: Regular; size_chart_size_type_juniors: Juniors; size_chart_size_type_plus: Plus;
                size_chart_size_type_big&tall: Big & Tall; size_chart_size_type_petite: Petite. Available values depend on the
                category.
     """

    table: SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTable | Unset = UNSET
    description: str | Unset = UNSET
    is_one_size: bool | Unset = UNSET
    measurement_type: str | Unset = UNSET
    unit_system: str | Unset = UNSET
    size_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table import SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTable # noqa: PLC0415
        table: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table, Unset):
            table = self.table.to_dict()

        description = self.description

        is_one_size = self.is_one_size

        measurement_type = self.measurement_type

        unit_system = self.unit_system

        size_types: list[str] | Unset = UNSET
        if not isinstance(self.size_types, Unset):
            size_types = self.size_types




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if table is not UNSET:
            field_dict["table"] = table
        if description is not UNSET:
            field_dict["description"] = description
        if is_one_size is not UNSET:
            field_dict["is_one_size"] = is_one_size
        if measurement_type is not UNSET:
            field_dict["measurement_type"] = measurement_type
        if unit_system is not UNSET:
            field_dict["unit_system"] = unit_system
        if size_types is not UNSET:
            field_dict["size_types"] = size_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_size_charts_response_data_size_chart_size_chart_data_size_chart_data_table import SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTable # noqa: PLC0415
        d = dict(src_dict)
        _table = d.pop("table", UNSET)
        table: SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTable | Unset
        if isinstance(_table,  Unset):
            table = UNSET
        else:
            table = SearchSizeChartsResponseDataSizeChartSizeChartDataSizeChartDataTable.from_dict(_table)




        description = d.pop("description", UNSET)

        is_one_size = d.pop("is_one_size", UNSET)

        measurement_type = d.pop("measurement_type", UNSET)

        unit_system = d.pop("unit_system", UNSET)

        size_types = cast(list[str], d.pop("size_types", UNSET))


        search_size_charts_response_data_size_chart_size_chart_data_size_chart_data = cls(
            table=table,
            description=description,
            is_one_size=is_one_size,
            measurement_type=measurement_type,
            unit_system=unit_system,
            size_types=size_types,
        )


        search_size_charts_response_data_size_chart_size_chart_data_size_chart_data.additional_properties = d
        return search_size_charts_response_data_size_chart_size_chart_data_size_chart_data

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
