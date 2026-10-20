from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_showcase_products_response_data_product_price_original_price import (
        GetShowcaseProductsResponseDataProductPriceOriginalPrice,
    )
    from ..models.get_showcase_products_response_data_product_price_platform_discount_price import (
        GetShowcaseProductsResponseDataProductPricePlatformDiscountPrice,
    )
    from ..models.get_showcase_products_response_data_product_price_seller_discount_price import (
        GetShowcaseProductsResponseDataProductPriceSellerDiscountPrice,
    )


T = TypeVar("T", bound="GetShowcaseProductsResponseDataProductPrice")


@_attrs_define
class GetShowcaseProductsResponseDataProductPrice:
    """
    Attributes:
        original_price (GetShowcaseProductsResponseDataProductPriceOriginalPrice | Unset):
        seller_discount_price (GetShowcaseProductsResponseDataProductPriceSellerDiscountPrice | Unset):
        platform_discount_price (GetShowcaseProductsResponseDataProductPricePlatformDiscountPrice | Unset):
    """

    original_price: GetShowcaseProductsResponseDataProductPriceOriginalPrice | Unset = UNSET
    seller_discount_price: GetShowcaseProductsResponseDataProductPriceSellerDiscountPrice | Unset = UNSET
    platform_discount_price: GetShowcaseProductsResponseDataProductPricePlatformDiscountPrice | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        original_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_price, Unset):
            original_price = self.original_price.to_dict()

        seller_discount_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_discount_price, Unset):
            seller_discount_price = self.seller_discount_price.to_dict()

        platform_discount_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.platform_discount_price, Unset):
            platform_discount_price = self.platform_discount_price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original_price is not UNSET:
            field_dict["original_price"] = original_price
        if seller_discount_price is not UNSET:
            field_dict["seller_discount_price"] = seller_discount_price
        if platform_discount_price is not UNSET:
            field_dict["platform_discount_price"] = platform_discount_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_showcase_products_response_data_product_price_original_price import (
            GetShowcaseProductsResponseDataProductPriceOriginalPrice,  # noqa: PLC0415
        )
        from ..models.get_showcase_products_response_data_product_price_platform_discount_price import (
            GetShowcaseProductsResponseDataProductPricePlatformDiscountPrice,  # noqa: PLC0415
        )
        from ..models.get_showcase_products_response_data_product_price_seller_discount_price import (
            GetShowcaseProductsResponseDataProductPriceSellerDiscountPrice,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _original_price = d.pop("original_price", UNSET)
        original_price: GetShowcaseProductsResponseDataProductPriceOriginalPrice | Unset
        if isinstance(_original_price, Unset):
            original_price = UNSET
        else:
            original_price = GetShowcaseProductsResponseDataProductPriceOriginalPrice.from_dict(_original_price)

        _seller_discount_price = d.pop("seller_discount_price", UNSET)
        seller_discount_price: GetShowcaseProductsResponseDataProductPriceSellerDiscountPrice | Unset
        if isinstance(_seller_discount_price, Unset):
            seller_discount_price = UNSET
        else:
            seller_discount_price = GetShowcaseProductsResponseDataProductPriceSellerDiscountPrice.from_dict(
                _seller_discount_price
            )

        _platform_discount_price = d.pop("platform_discount_price", UNSET)
        platform_discount_price: GetShowcaseProductsResponseDataProductPricePlatformDiscountPrice | Unset
        if isinstance(_platform_discount_price, Unset):
            platform_discount_price = UNSET
        else:
            platform_discount_price = GetShowcaseProductsResponseDataProductPricePlatformDiscountPrice.from_dict(
                _platform_discount_price
            )

        get_showcase_products_response_data_product_price = cls(
            original_price=original_price,
            seller_discount_price=seller_discount_price,
            platform_discount_price=platform_discount_price,
        )

        get_showcase_products_response_data_product_price.additional_properties = d
        return get_showcase_products_response_data_product_price

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
