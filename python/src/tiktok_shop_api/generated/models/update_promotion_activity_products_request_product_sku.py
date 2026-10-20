from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdatePromotionActivityProductsRequestProductSku")



@_attrs_define
class UpdatePromotionActivityProductsRequestProductSku:
    """ 
        Attributes:
            id (str): SKU ID
            quantity_limit (int): The quantity limit of the SKU involved in the activity. The range is `[1, 99]`, or you can
                use `-1` for unlimited. If you are updating the value of an existing SKU, the value cannot be decreased.
            quantity_per_user (int): Limit of SKU purchase per buyer. The range is `[1, 99]`, or you can use `-1` for
                unlimited. If you are updating the value of an existing SKU, the value cannot be decreased.
            activity_price_amount (str | Unset): Deal price in the SKU's currency. Specify this field when
                `product_level==VARIATION` and `activity_type` is `FIXED_PRICE` or `FLASHSALE`. Do not specify it when
                `activity_type==DIRECT_DISCOUNT`.
            discount (str | Unset): Discount value. If the SKU is 10% off, the value is `10`.
                You must specify this value when `product_level==VARIATION` and `activity_type==DIRECT_DISCOUNT`. Do not specify
                it when `activity_type` is `FIXED_PRICE` or `FLASHSALE`.
     """

    id: str
    quantity_limit: int
    quantity_per_user: int
    activity_price_amount: str | Unset = UNSET
    discount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quantity_limit = self.quantity_limit

        quantity_per_user = self.quantity_per_user

        activity_price_amount = self.activity_price_amount

        discount = self.discount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "quantity_limit": quantity_limit,
            "quantity_per_user": quantity_per_user,
        })
        if activity_price_amount is not UNSET:
            field_dict["activity_price_amount"] = activity_price_amount
        if discount is not UNSET:
            field_dict["discount"] = discount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        quantity_limit = d.pop("quantity_limit")

        quantity_per_user = d.pop("quantity_per_user")

        activity_price_amount = d.pop("activity_price_amount", UNSET)

        discount = d.pop("discount", UNSET)

        update_promotion_activity_products_request_product_sku = cls(
            id=id,
            quantity_limit=quantity_limit,
            quantity_per_user=quantity_per_user,
            activity_price_amount=activity_price_amount,
            discount=discount,
        )


        update_promotion_activity_products_request_product_sku.additional_properties = d
        return update_promotion_activity_products_request_product_sku

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
