from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.price_detail import PriceDetail
  from ..models.product_image import ProductImage





T = TypeVar("T", bound="ExchangeOrderLine")



@_attrs_define
class ExchangeOrderLine:
    """ 
        Attributes:
            order_line_id (str | Unset): Ignore this field. It is not yet supported.
            sku_id (str | Unset): Ignore this field. It is not yet supported.
            sku_name (str | Unset): Ignore this field. It is not yet supported.
            product_name (str | Unset): Ignore this field. It is not yet supported.
            seller_sku_name (str | Unset): Ignore this field. It is not yet supported.
            product_image (ProductImage | Unset):
            price_detail (PriceDetail | Unset):
     """

    order_line_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    sku_name: str | Unset = UNSET
    product_name: str | Unset = UNSET
    seller_sku_name: str | Unset = UNSET
    product_image: ProductImage | Unset = UNSET
    price_detail: PriceDetail | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.price_detail import PriceDetail # noqa: PLC0415
        from ..models.product_image import ProductImage # noqa: PLC0415
        order_line_id = self.order_line_id

        sku_id = self.sku_id

        sku_name = self.sku_name

        product_name = self.product_name

        seller_sku_name = self.seller_sku_name

        product_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_image, Unset):
            product_image = self.product_image.to_dict()

        price_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price_detail, Unset):
            price_detail = self.price_detail.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_line_id is not UNSET:
            field_dict["order_line_id"] = order_line_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if sku_name is not UNSET:
            field_dict["sku_name"] = sku_name
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if seller_sku_name is not UNSET:
            field_dict["seller_sku_name"] = seller_sku_name
        if product_image is not UNSET:
            field_dict["product_image"] = product_image
        if price_detail is not UNSET:
            field_dict["price_detail"] = price_detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.price_detail import PriceDetail # noqa: PLC0415
        from ..models.product_image import ProductImage # noqa: PLC0415
        d = dict(src_dict)
        order_line_id = d.pop("order_line_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        sku_name = d.pop("sku_name", UNSET)

        product_name = d.pop("product_name", UNSET)

        seller_sku_name = d.pop("seller_sku_name", UNSET)

        _product_image = d.pop("product_image", UNSET)
        product_image: ProductImage | Unset
        if isinstance(_product_image,  Unset):
            product_image = UNSET
        else:
            product_image = ProductImage.from_dict(_product_image)




        _price_detail = d.pop("price_detail", UNSET)
        price_detail: PriceDetail | Unset
        if isinstance(_price_detail,  Unset):
            price_detail = UNSET
        else:
            price_detail = PriceDetail.from_dict(_price_detail)




        exchange_order_line = cls(
            order_line_id=order_line_id,
            sku_id=sku_id,
            sku_name=sku_name,
            product_name=product_name,
            seller_sku_name=seller_sku_name,
            product_image=product_image,
            price_detail=price_detail,
        )


        exchange_order_line.additional_properties = d
        return exchange_order_line

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
