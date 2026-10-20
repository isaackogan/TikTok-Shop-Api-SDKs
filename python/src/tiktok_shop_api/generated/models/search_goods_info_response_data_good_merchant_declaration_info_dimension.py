from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoDimension")



@_attrs_define
class SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoDimension:
    """ 
        Attributes:
            width (str | Unset): Width value, up to three decimal places.
            length (str | Unset): Length value, up to three decimal places.
            height (str | Unset): Height value, up to three decimal places.
            unit (str | Unset): Dimension unit.
                Possible values:
                - MILLIMETER
                - CENTIMETER
                - METER
                - FOOT
                - INCH
                - MICROMETER
     """

    width: str | Unset = UNSET
    length: str | Unset = UNSET
    height: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        width = self.width

        length = self.length

        height = self.height

        unit = self.unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if width is not UNSET:
            field_dict["width"] = width
        if length is not UNSET:
            field_dict["length"] = length
        if height is not UNSET:
            field_dict["height"] = height
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width", UNSET)

        length = d.pop("length", UNSET)

        height = d.pop("height", UNSET)

        unit = d.pop("unit", UNSET)

        search_goods_info_response_data_good_merchant_declaration_info_dimension = cls(
            width=width,
            length=length,
            height=height,
            unit=unit,
        )


        search_goods_info_response_data_good_merchant_declaration_info_dimension.additional_properties = d
        return search_goods_info_response_data_good_merchant_declaration_info_dimension

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
