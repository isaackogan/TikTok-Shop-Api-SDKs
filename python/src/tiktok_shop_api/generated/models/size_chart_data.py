from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.size_chart_data_measurement_type import SizeChartDataMeasurementType
from ..models.size_chart_data_unit_system import SizeChartDataUnitSystem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table import Table


T = TypeVar("T", bound="SizeChartData")


@_attrs_define
class SizeChartData:
    """
    Attributes:
        table (Table):
        measurement_type (SizeChartDataMeasurementType): Possible values: GENERIC_MEASUREMENTS: generic measurements;
            BODY_MEASUREMENTS: shopper body measurements; PRODUCT_MEASUREMENTS: finished-product measurements.
        unit_system (SizeChartDataUnitSystem): Possible values: METRIC: metric units; IMPERIAL: imperial units.
        size_types (list[str] | Unset): Possible values: size_chart_common_size_type: Common;
            size_chart_size_type_regular: Regular; size_chart_size_type_juniors: Juniors; size_chart_size_type_plus: Plus;
            size_chart_size_type_big&tall: Big & Tall; size_chart_size_type_petite: Petite. Available values depend on the
            category.
        description (str | Unset): Additional size chart description.
        is_one_size (bool | Unset): Whether this is a one-size chart.
    """

    table: Table
    measurement_type: SizeChartDataMeasurementType
    unit_system: SizeChartDataUnitSystem
    size_types: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    is_one_size: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        table = self.table.to_dict()

        measurement_type = self.measurement_type.value

        unit_system = self.unit_system.value

        size_types: list[str] | Unset = UNSET
        if not isinstance(self.size_types, Unset):
            size_types = self.size_types

        description = self.description

        is_one_size = self.is_one_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "table": table,
                "measurement_type": measurement_type,
                "unit_system": unit_system,
            }
        )
        if size_types is not UNSET:
            field_dict["size_types"] = size_types
        if description is not UNSET:
            field_dict["description"] = description
        if is_one_size is not UNSET:
            field_dict["is_one_size"] = is_one_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table import Table  # noqa: PLC0415

        d = dict(src_dict)
        table = Table.from_dict(d.pop("table"))

        measurement_type = SizeChartDataMeasurementType(d.pop("measurement_type"))

        unit_system = SizeChartDataUnitSystem(d.pop("unit_system"))

        size_types = cast(list[str], d.pop("size_types", UNSET))

        description = d.pop("description", UNSET)

        is_one_size = d.pop("is_one_size", UNSET)

        size_chart_data = cls(
            table=table,
            measurement_type=measurement_type,
            unit_system=unit_system,
            size_types=size_types,
            description=description,
            is_one_size=is_one_size,
        )

        size_chart_data.additional_properties = d
        return size_chart_data

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
