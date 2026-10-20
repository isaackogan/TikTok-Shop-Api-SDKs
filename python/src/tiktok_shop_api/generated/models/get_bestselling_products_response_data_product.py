from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_bestselling_products_response_data_product_product_image import GetBestsellingProductsResponseDataProductProductImage





T = TypeVar("T", bound="GetBestsellingProductsResponseDataProduct")



@_attrs_define
class GetBestsellingProductsResponseDataProduct:
    """ 
        Attributes:
            rank (int | Unset): GMV rank of the product.
            gmv_range (str | Unset): GMV range of the product, in the currency specified by currency.
            id (str | Unset): Product ID
            name (str | Unset): Product name
            rating (str | Unset): Product rating in history
            product_image (GetBestsellingProductsResponseDataProductProductImage | Unset):
            shop_name (str | Unset): The TikTok Shop name.
            shop_id (str | Unset): The ID of the TikTok Shop associated with the product.
     """

    rank: int | Unset = UNSET
    gmv_range: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    rating: str | Unset = UNSET
    product_image: GetBestsellingProductsResponseDataProductProductImage | Unset = UNSET
    shop_name: str | Unset = UNSET
    shop_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_bestselling_products_response_data_product_product_image import GetBestsellingProductsResponseDataProductProductImage # noqa: PLC0415
        rank = self.rank

        gmv_range = self.gmv_range

        id = self.id

        name = self.name

        rating = self.rating

        product_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_image, Unset):
            product_image = self.product_image.to_dict()

        shop_name = self.shop_name

        shop_id = self.shop_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rank is not UNSET:
            field_dict["rank"] = rank
        if gmv_range is not UNSET:
            field_dict["gmv_range"] = gmv_range
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if rating is not UNSET:
            field_dict["rating"] = rating
        if product_image is not UNSET:
            field_dict["product_image"] = product_image
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_bestselling_products_response_data_product_product_image import GetBestsellingProductsResponseDataProductProductImage # noqa: PLC0415
        d = dict(src_dict)
        rank = d.pop("rank", UNSET)

        gmv_range = d.pop("gmv_range", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        rating = d.pop("rating", UNSET)

        _product_image = d.pop("product_image", UNSET)
        product_image: GetBestsellingProductsResponseDataProductProductImage | Unset
        if isinstance(_product_image,  Unset):
            product_image = UNSET
        else:
            product_image = GetBestsellingProductsResponseDataProductProductImage.from_dict(_product_image)




        shop_name = d.pop("shop_name", UNSET)

        shop_id = d.pop("shop_id", UNSET)

        get_bestselling_products_response_data_product = cls(
            rank=rank,
            gmv_range=gmv_range,
            id=id,
            name=name,
            rating=rating,
            product_image=product_image,
            shop_name=shop_name,
            shop_id=shop_id,
        )


        get_bestselling_products_response_data_product.additional_properties = d
        return get_bestselling_products_response_data_product

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
