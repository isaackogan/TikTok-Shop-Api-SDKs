from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_post_view_search_video_products_response_data_product import GetPostViewSearchVideoProductsResponseDataProduct





T = TypeVar("T", bound="GetPostViewSearchVideoProductsResponseData")



@_attrs_define
class GetPostViewSearchVideoProductsResponseData:
    """ 
        Attributes:
            products (list[GetPostViewSearchVideoProductsResponseDataProduct] | Unset): Currently associated products; empty
                when none are associated.
            video_id (str | Unset): Unique video id.
     """

    products: list[GetPostViewSearchVideoProductsResponseDataProduct] | Unset = UNSET
    video_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_post_view_search_video_products_response_data_product import GetPostViewSearchVideoProductsResponseDataProduct # noqa: PLC0415
        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)



        video_id = self.video_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if products is not UNSET:
            field_dict["products"] = products
        if video_id is not UNSET:
            field_dict["video_id"] = video_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_post_view_search_video_products_response_data_product import GetPostViewSearchVideoProductsResponseDataProduct # noqa: PLC0415
        d = dict(src_dict)
        _products = d.pop("products", UNSET)
        products: list[GetPostViewSearchVideoProductsResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = GetPostViewSearchVideoProductsResponseDataProduct.from_dict(products_item_data)



                products.append(products_item)


        video_id = d.pop("video_id", UNSET)

        get_post_view_search_video_products_response_data = cls(
            products=products,
            video_id=video_id,
        )


        get_post_view_search_video_products_response_data.additional_properties = d
        return get_post_view_search_video_products_response_data

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
