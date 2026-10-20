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
        measurement_type (SizeChartDataMeasurementType): Possible values: GENERIC_MEASUREMENTS: generic measurements;
            BODY_MEASUREMENTS: shopper body measurements; PRODUCT_MEASUREMENTS: finished-product measurements.
        table (Table):
        unit_system (SizeChartDataUnitSystem): Possible values: METRIC: metric units; IMPERIAL: imperial units.
        description (str | Unset): Additional size chart description.
        is_one_size (bool | Unset): Whether this is a one-size chart.
        size_types (list[str] | Unset): Possible values: size_chart_common_size_type: Common;
            size_chart_size_type_regular: Regular; size_chart_size_type_juniors: Juniors; size_chart_size_type_plus: Plus;
            size_chart_size_type_big&tall: Big & Tall; size_chart_size_type_petite: Petite. Available values depend on the
            category.
    """

    measurement_type: SizeChartDataMeasurementType
    table: Table
    unit_system: SizeChartDataUnitSystem
    description: str | Unset = UNSET
    is_one_size: bool | Unset = UNSET
    size_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_type = self.measurement_type.value

        table = self.table.to_dict()

        unit_system = self.unit_system.value

        description = self.description

        is_one_size = self.is_one_size

        size_types: list[str] | Unset = UNSET
        if not isinstance(self.size_types, Unset):
            size_types = self.size_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "measurement_type": measurement_type,
                "table": table,
                "unit_system": unit_system,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_one_size is not UNSET:
            field_dict["is_one_size"] = is_one_size
        if size_types is not UNSET:
            field_dict["size_types"] = size_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table import Table  # noqa: PLC0415

        d = dict(src_dict)
        measurement_type = SizeChartDataMeasurementType(d.pop("measurement_type"))

        table = Table.from_dict(d.pop("table"))

        unit_system = SizeChartDataUnitSystem(d.pop("unit_system"))

        description = d.pop("description", UNSET)

        is_one_size = d.pop("is_one_size", UNSET)

        size_types = cast(list[str], d.pop("size_types", UNSET))

        size_chart_data = cls(
            measurement_type=measurement_type,
            table=table,
            unit_system=unit_system,
            description=description,
            is_one_size=is_one_size,
            size_types=size_types,
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
