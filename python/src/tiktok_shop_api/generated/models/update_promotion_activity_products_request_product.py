from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_promotion_activity_products_request_product_sku import (
        UpdatePromotionActivityProductsRequestProductSku,
    )


T = TypeVar("T", bound="UpdatePromotionActivityProductsRequestProduct")


@_attrs_define
class UpdatePromotionActivityProductsRequestProduct:
    """
    Attributes:
        id (str): TikTok Shop product ID
        quantity_limit (int): The quantity limit of the products involved in the activity. The range is `[1, 99]`, or
            you can use `-1` for unlimited. If you are updating the value of an existing product, the value cannot be less
            than the current value.
            When `product_level==VARIATION`, you must specify `-1`.
        quantity_per_user (int): Limit of product purchase per buyer. The range is `[1, 99]`, or you can use `-1` for
            unlimited. If you are updating the value of an existing product, the value cannot be less than the current
            value.
            When `product_level==VARIATION`, you must specify `-1`.
        activity_price_amount (str | Unset): Deal price in the product's currency. Specify this field when
            `product_level==PRODUCT` and `activity_type` is `FIXED_PRICE` or `FLASHSALE`. Do not specify it when
            `activity_type==DIRECT_DISCOUNT` or when `product_level==VARIATION`.
        discount (str | Unset): Discount value. If the product is 10% off, the value is `10`.
            You must specify the value when `product_level==PRODUCT` and `activity_type==DIRECT_DISCOUNT`; and you must not
            specify it when it's not.
        skus (list[UpdatePromotionActivityProductsRequestProductSku] | Unset): The SKUs to add to the list or to edit.
            The number of the SKUs across all products must not exceed 300 in an API call.
            For a product-discount or flash-deal activity with `product_level==VARIATION`, every product must contain at
            least one SKU. For those activity types with `product_level==PRODUCT`, specify `[]`.
    """

    id: str
    quantity_limit: int
    quantity_per_user: int
    activity_price_amount: str | Unset = UNSET
    discount: str | Unset = UNSET
    skus: list[UpdatePromotionActivityProductsRequestProductSku] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quantity_limit = self.quantity_limit

        quantity_per_user = self.quantity_per_user

        activity_price_amount = self.activity_price_amount

        discount = self.discount

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "quantity_limit": quantity_limit,
                "quantity_per_user": quantity_per_user,
            }
        )
        if activity_price_amount is not UNSET:
            field_dict["activity_price_amount"] = activity_price_amount
        if discount is not UNSET:
            field_dict["discount"] = discount
        if skus is not UNSET:
            field_dict["skus"] = skus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_promotion_activity_products_request_product_sku import (
            UpdatePromotionActivityProductsRequestProductSku,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        quantity_limit = d.pop("quantity_limit")

        quantity_per_user = d.pop("quantity_per_user")

        activity_price_amount = d.pop("activity_price_amount", UNSET)

        discount = d.pop("discount", UNSET)

        _skus = d.pop("skus", UNSET)
        skus: list[UpdatePromotionActivityProductsRequestProductSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = UpdatePromotionActivityProductsRequestProductSku.from_dict(skus_item_data)

                skus.append(skus_item)

        update_promotion_activity_products_request_product = cls(
            id=id,
            quantity_limit=quantity_limit,
            quantity_per_user=quantity_per_user,
            activity_price_amount=activity_price_amount,
            discount=discount,
            skus=skus,
        )

        update_promotion_activity_products_request_product.additional_properties = d
        return update_promotion_activity_products_request_product

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
