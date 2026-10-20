from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoWeight")


@_attrs_define
class SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoWeight:
    """
    Attributes:
        value (str | Unset): Weight value, up to three decimal places.
        unit (str | Unset): Weight unit.
            Possible values:
            - MILLIGRAM
            - GRAM
            - KILOGRAM
            - POUND
            - OUNCE
    """

    value: str | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        unit = d.pop("unit", UNSET)

        search_goods_info_response_data_good_merchant_declaration_info_weight = cls(
            value=value,
            unit=unit,
        )

        search_goods_info_response_data_good_merchant_declaration_info_weight.additional_properties = d
        return search_goods_info_response_data_good_merchant_declaration_info_weight

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
