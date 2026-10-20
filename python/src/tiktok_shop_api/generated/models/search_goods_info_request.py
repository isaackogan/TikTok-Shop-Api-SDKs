from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchGoodsInfoRequest")



@_attrs_define
class SearchGoodsInfoRequest:
    """ 
        Attributes:
            goods_ids (list[str] | Unset): Fulfilled by TikTok goods IDs used to filter the results. Each ID must be a
                positive decimal string. Maximum: 100 IDs per request.
            product_ids (list[str] | Unset): TikTok Shop product IDs used to filter the results. Each ID must be a positive
                decimal string. Maximum: 100 IDs per request.
            reference_codes (list[str] | Unset): Merchant-defined goods reference codes used to filter the results. Maximum:
                100 codes per request.
            sku_ids (list[str] | Unset): TikTok Shop SKU IDs used to filter the results. Each ID must be a positive decimal
                string. Maximum: 100 IDs per request.
     """

    goods_ids: list[str] | Unset = UNSET
    product_ids: list[str] | Unset = UNSET
    reference_codes: list[str] | Unset = UNSET
    sku_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        goods_ids: list[str] | Unset = UNSET
        if not isinstance(self.goods_ids, Unset):
            goods_ids = self.goods_ids



        product_ids: list[str] | Unset = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids



        reference_codes: list[str] | Unset = UNSET
        if not isinstance(self.reference_codes, Unset):
            reference_codes = self.reference_codes



        sku_ids: list[str] | Unset = UNSET
        if not isinstance(self.sku_ids, Unset):
            sku_ids = self.sku_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if goods_ids is not UNSET:
            field_dict["goods_ids"] = goods_ids
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids
        if reference_codes is not UNSET:
            field_dict["reference_codes"] = reference_codes
        if sku_ids is not UNSET:
            field_dict["sku_ids"] = sku_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goods_ids = cast(list[str], d.pop("goods_ids", UNSET))


        product_ids = cast(list[str], d.pop("product_ids", UNSET))


        reference_codes = cast(list[str], d.pop("reference_codes", UNSET))


        sku_ids = cast(list[str], d.pop("sku_ids", UNSET))


        search_goods_info_request = cls(
            goods_ids=goods_ids,
            product_ids=product_ids,
            reference_codes=reference_codes,
            sku_ids=sku_ids,
        )


        search_goods_info_request.additional_properties = d
        return search_goods_info_request

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
