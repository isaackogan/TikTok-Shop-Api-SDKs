from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CreateFBTGoodsRequestCreateGoodsDtoListDimensionAndWeightBaseInfo")



@_attrs_define
class CreateFBTGoodsRequestCreateGoodsDtoListDimensionAndWeightBaseInfo:
    """ 
        Attributes:
            weight_value (str): Weight of the goods in the specified weight_unit.
            length_value (str): Length of the goods in the specified dimension_unit.
            width_value (str): Width of the goods in the specified dimension_unit.
            height_value (str): Height of the goods in the specified dimension_unit.
            weight_unit (str): Weight unit. Possible values: MILLIGRAM (mg), GRAM (g), KILOGRAM (kg), POUND (lb), OUNCE
                (oz).
            dimension_unit (str): Dimension unit. Possible values: MILLIMETER (mm), CENTIMETER (cm), METER (m), FOOT (ft),
                INCH (in).
     """

    weight_value: str
    length_value: str
    width_value: str
    height_value: str
    weight_unit: str
    dimension_unit: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        weight_value = self.weight_value

        length_value = self.length_value

        width_value = self.width_value

        height_value = self.height_value

        weight_unit = self.weight_unit

        dimension_unit = self.dimension_unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "weight_value": weight_value,
            "length_value": length_value,
            "width_value": width_value,
            "height_value": height_value,
            "weight_unit": weight_unit,
            "dimension_unit": dimension_unit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weight_value = d.pop("weight_value")

        length_value = d.pop("length_value")

        width_value = d.pop("width_value")

        height_value = d.pop("height_value")

        weight_unit = d.pop("weight_unit")

        dimension_unit = d.pop("dimension_unit")

        create_fbt_goods_request_create_goods_dto_list_dimension_and_weight_base_info = cls(
            weight_value=weight_value,
            length_value=length_value,
            width_value=width_value,
            height_value=height_value,
            weight_unit=weight_unit,
            dimension_unit=dimension_unit,
        )


        create_fbt_goods_request_create_goods_dto_list_dimension_and_weight_base_info.additional_properties = d
        return create_fbt_goods_request_create_goods_dto_list_dimension_and_weight_base_info

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
