from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_tokopedia_and_tik_tok_shop_product_id_mappings_response_data_error import GetTokopediaAndTikTokShopProductIDMappingsResponseDataError
  from ..models.product import Product





T = TypeVar("T", bound="GetTokopediaAndTikTokShopProductIDMappingsResponseData")



@_attrs_define
class GetTokopediaAndTikTokShopProductIDMappingsResponseData:
    """ 
        Attributes:
            error (GetTokopediaAndTikTokShopProductIDMappingsResponseDataError | Unset):
            product (list[Product] | Unset): list of product data
     """

    error: GetTokopediaAndTikTokShopProductIDMappingsResponseDataError | Unset = UNSET
    product: list[Product] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_tokopedia_and_tik_tok_shop_product_id_mappings_response_data_error import GetTokopediaAndTikTokShopProductIDMappingsResponseDataError # noqa: PLC0415
        from ..models.product import Product # noqa: PLC0415
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        product: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = []
            for product_item_data in self.product:
                product_item = product_item_data.to_dict()
                product.append(product_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error is not UNSET:
            field_dict["error"] = error
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_tokopedia_and_tik_tok_shop_product_id_mappings_response_data_error import GetTokopediaAndTikTokShopProductIDMappingsResponseDataError # noqa: PLC0415
        from ..models.product import Product # noqa: PLC0415
        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: GetTokopediaAndTikTokShopProductIDMappingsResponseDataError | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = GetTokopediaAndTikTokShopProductIDMappingsResponseDataError.from_dict(_error)




        _product = d.pop("product", UNSET)
        product: list[Product] | Unset = UNSET
        if _product is not UNSET:
            product = []
            for product_item_data in _product:
                product_item = Product.from_dict(product_item_data)



                product.append(product_item)


        get_tokopedia_and_tik_tok_shop_product_id_mappings_response_data = cls(
            error=error,
            product=product,
        )


        get_tokopedia_and_tik_tok_shop_product_id_mappings_response_data.additional_properties = d
        return get_tokopedia_and_tik_tok_shop_product_id_mappings_response_data

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
