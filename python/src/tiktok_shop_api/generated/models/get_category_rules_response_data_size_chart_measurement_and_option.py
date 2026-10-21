from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_category_rules_response_data_size_chart_measurement_and_option_option import GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOption





T = TypeVar("T", bound="GetCategoryRulesResponseDataSizeChartMeasurementAndOption")



@_attrs_define
class GetCategoryRulesResponseDataSizeChartMeasurementAndOption:
    """ 
        Attributes:
            size_systems (list[str] | Unset): Size system IDs supported by the current shop, determined by the shop region
                and seller type. Use these IDs for size-system columns in size_chart_data.table.headers[].id when creating or
                editing a size chart. The available list is configuration-dependent and may change; do not hardcode it. This
                field is omitted when size charts are unsupported or no size systems are returned.
            measurement_type (str | Unset): Possible values: GENERIC_MEASUREMENTS: generic measurements for categories that
                do not distinguish body and product measurements; BODY_MEASUREMENTS: shopper body measurements;
                PRODUCT_MEASUREMENTS: finished-product or garment measurements.
            options (list[GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOption] | Unset): Online measurement
                options for this group.
     """

    size_systems: list[str] | Unset = UNSET
    measurement_type: str | Unset = UNSET
    options: list[GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOption] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_category_rules_response_data_size_chart_measurement_and_option_option import GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOption # noqa: PLC0415
        size_systems: list[str] | Unset = UNSET
        if not isinstance(self.size_systems, Unset):
            size_systems = self.size_systems



        measurement_type = self.measurement_type

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if size_systems is not UNSET:
            field_dict["size_systems"] = size_systems
        if measurement_type is not UNSET:
            field_dict["measurement_type"] = measurement_type
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_category_rules_response_data_size_chart_measurement_and_option_option import GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOption # noqa: PLC0415
        d = dict(src_dict)
        size_systems = cast(list[str], d.pop("size_systems", UNSET))


        measurement_type = d.pop("measurement_type", UNSET)

        _options = d.pop("options", UNSET)
        options: list[GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = GetCategoryRulesResponseDataSizeChartMeasurementAndOptionOption.from_dict(options_item_data)



                options.append(options_item)


        get_category_rules_response_data_size_chart_measurement_and_option = cls(
            size_systems=size_systems,
            measurement_type=measurement_type,
            options=options,
        )


        get_category_rules_response_data_size_chart_measurement_and_option.additional_properties = d
        return get_category_rules_response_data_size_chart_measurement_and_option

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
