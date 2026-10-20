from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_category_rules_response_data_size_chart_measurement_and_option import GetCategoryRulesResponseDataSizeChartMeasurementAndOption





T = TypeVar("T", bound="GetCategoryRulesResponseDataSizeChart")



@_attrs_define
class GetCategoryRulesResponseDataSizeChart:
    """ 
        Attributes:
            is_supported (bool | Unset): A flag to indicate whether size charts are supported.

                **Note**: If size charts are not supported, even if you provide a size chart when creating or editing a product,
                the size chart will not be saved.
            is_required (bool | Unset): A flag to indicate whether a size chart is required.
            measurement_and_options (list[GetCategoryRulesResponseDataSizeChartMeasurementAndOption] | Unset): Measurement
                rules grouped by measurement basis.
            size_types (list[str] | Unset): Available size types configured for this category. Use values returned in this
                list for size_chart_data.size_types when creating or editing a size chart. Possible values include:
                size_chart_common_size_type: Common; size_chart_size_type_regular: Regular; size_chart_size_type_juniors:
                Juniors; size_chart_size_type_plus: Plus; size_chart_size_type_big&tall: Big & Tall;
                size_chart_size_type_petite: Petite. This field is omitted when size types do not apply to the category.
     """

    is_supported: bool | Unset = UNSET
    is_required: bool | Unset = UNSET
    measurement_and_options: list[GetCategoryRulesResponseDataSizeChartMeasurementAndOption] | Unset = UNSET
    size_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_category_rules_response_data_size_chart_measurement_and_option import GetCategoryRulesResponseDataSizeChartMeasurementAndOption # noqa: PLC0415
        is_supported = self.is_supported

        is_required = self.is_required

        measurement_and_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.measurement_and_options, Unset):
            measurement_and_options = []
            for measurement_and_options_item_data in self.measurement_and_options:
                measurement_and_options_item = measurement_and_options_item_data.to_dict()
                measurement_and_options.append(measurement_and_options_item)



        size_types: list[str] | Unset = UNSET
        if not isinstance(self.size_types, Unset):
            size_types = self.size_types




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_supported is not UNSET:
            field_dict["is_supported"] = is_supported
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if measurement_and_options is not UNSET:
            field_dict["measurement_and_options"] = measurement_and_options
        if size_types is not UNSET:
            field_dict["size_types"] = size_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_category_rules_response_data_size_chart_measurement_and_option import GetCategoryRulesResponseDataSizeChartMeasurementAndOption # noqa: PLC0415
        d = dict(src_dict)
        is_supported = d.pop("is_supported", UNSET)

        is_required = d.pop("is_required", UNSET)

        _measurement_and_options = d.pop("measurement_and_options", UNSET)
        measurement_and_options: list[GetCategoryRulesResponseDataSizeChartMeasurementAndOption] | Unset = UNSET
        if _measurement_and_options is not UNSET:
            measurement_and_options = []
            for measurement_and_options_item_data in _measurement_and_options:
                measurement_and_options_item = GetCategoryRulesResponseDataSizeChartMeasurementAndOption.from_dict(measurement_and_options_item_data)



                measurement_and_options.append(measurement_and_options_item)


        size_types = cast(list[str], d.pop("size_types", UNSET))


        get_category_rules_response_data_size_chart = cls(
            is_supported=is_supported,
            is_required=is_required,
            measurement_and_options=measurement_and_options,
            size_types=size_types,
        )


        get_category_rules_response_data_size_chart.additional_properties = d
        return get_category_rules_response_data_size_chart

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
