from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_return_records_response_data_record_image import GetReturnRecordsResponseDataRecordImage
    from ..models.price import Price


T = TypeVar("T", bound="GetShopProductsResponseDataProduct")


@_attrs_define
class GetShopProductsResponseDataProduct:
    """
    Attributes:
        id (str | Unset): TikTok product ID.
        title (str | Unset): Product name.
        price (Price | Unset):
        added_status (str | Unset): Showcase add status with possible values:
            - ADDABLE
            - ADDED
            - REJECTED
        brand_name (str | Unset): The brand name a seller has set for a product.
        images (list[GetReturnRecordsResponseDataRecordImage] | Unset): Images of a product.
        sales_count (int | Unset): The number of products that have been sold.
    """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    price: Price | Unset = UNSET
    added_status: str | Unset = UNSET
    brand_name: str | Unset = UNSET
    images: list[GetReturnRecordsResponseDataRecordImage] | Unset = UNSET
    sales_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        added_status = self.added_status

        brand_name = self.brand_name

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        sales_count = self.sales_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if price is not UNSET:
            field_dict["price"] = price
        if added_status is not UNSET:
            field_dict["added_status"] = added_status
        if brand_name is not UNSET:
            field_dict["brand_name"] = brand_name
        if images is not UNSET:
            field_dict["images"] = images
        if sales_count is not UNSET:
            field_dict["sales_count"] = sales_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_return_records_response_data_record_image import (
            GetReturnRecordsResponseDataRecordImage,  # noqa: PLC0415
        )
        from ..models.price import Price  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        _price = d.pop("price", UNSET)
        price: Price | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = Price.from_dict(_price)

        added_status = d.pop("added_status", UNSET)

        brand_name = d.pop("brand_name", UNSET)

        _images = d.pop("images", UNSET)
        images: list[GetReturnRecordsResponseDataRecordImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = GetReturnRecordsResponseDataRecordImage.from_dict(images_item_data)

                images.append(images_item)

        sales_count = d.pop("sales_count", UNSET)

        get_shop_products_response_data_product = cls(
            id=id,
            title=title,
            price=price,
            added_status=added_status,
            brand_name=brand_name,
            images=images,
            sales_count=sales_count,
        )

        get_shop_products_response_data_product.additional_properties = d
        return get_shop_products_response_data_product

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
