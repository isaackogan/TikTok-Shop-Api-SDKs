from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_goods_info_response_data_good_barcode_type import SearchGoodsInfoResponseDataGoodBarcodeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchGoodsInfoResponseDataGoodBarcode")


@_attrs_define
class SearchGoodsInfoResponseDataGoodBarcode:
    """
    Attributes:
        code (str | Unset): The printable barcode for the goods.
        type_ (SearchGoodsInfoResponseDataGoodBarcodeType | Unset): The barcode type.
            Possible values:
            - UPC
            - EAN
            - GTIN
            - ASIN_OR_FNSKU
            - MERCHANT_SKU_ID
            - FBT_SPECIFIC_BARCODE
    """

    code: str | Unset = UNSET
    type_: SearchGoodsInfoResponseDataGoodBarcodeType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: SearchGoodsInfoResponseDataGoodBarcodeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SearchGoodsInfoResponseDataGoodBarcodeType(_type_)

        search_goods_info_response_data_good_barcode = cls(
            code=code,
            type_=type_,
        )

        search_goods_info_response_data_good_barcode.additional_properties = d
        return search_goods_info_response_data_good_barcode

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
