from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductResponseDataSkuGlobalListingPolicyReplicateSource")



@_attrs_define
class GetProductResponseDataSkuGlobalListingPolicyReplicateSource:
    """ 
        Attributes:
            product_id (str | Unset): The ID of the source product.
            shop_id (str | Unset): The shop ID of the source product.
            sku_id (str | Unset): The SKU ID of the source product.
     """

    product_id: str | Unset = UNSET
    shop_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        shop_id = self.shop_id

        sku_id = self.sku_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        shop_id = d.pop("shop_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        get_product_response_data_sku_global_listing_policy_replicate_source = cls(
            product_id=product_id,
            shop_id=shop_id,
            sku_id=sku_id,
        )


        get_product_response_data_sku_global_listing_policy_replicate_source.additional_properties = d
        return get_product_response_data_sku_global_listing_policy_replicate_source

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
