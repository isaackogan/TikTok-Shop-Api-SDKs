from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.shipping_discount_threshold_type import ShippingDiscountThresholdType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.area_scope import AreaScope





T = TypeVar("T", bound="ShippingDiscount")



@_attrs_define
class ShippingDiscount:
    """ 
        Attributes:
            threshold_type (ShippingDiscountThresholdType): The type of purchase criteria. Possible enumerations are:
                - `NO_THRESHOLD`: No minimum purchase criteria.
                - `MINIMAL_ITEM_QUANTITY`: Buyer must meet or exceed the minimum spend criteria with eligible products.
                - `MINIMAL_ORDER_AMOUNT`: Buyer must meet or exceed the minimum spend criteria with eligible order.
                `MINIMAL_ITEM_QUANTITY` and `MINIMAL_ORDER_AMOUNT` can only be set when `product_level==SHOP`.
            type_ (str): The shipping benefit type.
                - `FREE_SHIPPING`: Reduce the buyer's shipping fee to zero.
                - `DISCOUNT_SHIPPING_FEE`: Reduce the buyer's shipping fee by up to the amount specified in
                `shipping_discount.value`.
            area_scope (AreaScope):
            threshold_value (str | Unset): The purchase threshold of the discount, based on `threshold_type`, for example,
                `3`. Determined by the user.
                - When `threshold_type==NO_THRESHOLD`, this value is not required.
                - When `threshold_type==MINIMAL_ITEM_QUANTITY`, the buyer must purchase at least the specified number of
                eligible products (for example, 3 eligible products). If it represents a quantity, it must be an integer.
                - When `threshold_type==MINIMAL_ORDER_AMOUNT`, the eligible-product subtotal must meet or exceed the specified
                value in local currency (for example, 3 units of local currency). If it represents an order value, it must be
                limited to two decimal places.
            value (str | Unset): The shipping discount value determined by `type`.
                - When `type==FREE_SHIPPING`, omit this value.
                - When `type==DISCOUNT_SHIPPING_FEE`, enter the maximum amount deducted from the buyer's shipping fee in local
                currency, with at most two decimal places.
            shipping_method (str | Unset): The shipping methods to which this promotion applies.
                - When `STANDARD_SHIPPING`: Only applies to Standard Shipping methods, including Economy.
                - `EXPRESS_SHIPPING`: Only applies to Express Shipping methods.
                - `ALL_SHIPPING_METHOD`: Applies to all shipping methods that the shop offers.
                Default: `STANDARD_SHIPPING`
            inventory_type (str | Unset): The inventory types to which the promotion activity applies:
                - `SELF_FULFILLED`: Only applies to Inventory fulfilled from seller warehouses
                - `FULFILLED_BY_TIKTOK`: Only applies to Inventory fulfilled by TikTok from FBT (Fulfilled by TikTok)
                warehouses.
                - `ALL`:  Applies to all inventory of eligible products.
                Default: `SELF_FULFILLED`
                `FULFILLED_BY_TIKTOK` and `ALL` can only be set when `product_level`==`SHOP` and `threshold_type=NO_THRESHOLD`.
     """

    threshold_type: ShippingDiscountThresholdType
    type_: str
    area_scope: AreaScope
    threshold_value: str | Unset = UNSET
    value: str | Unset = UNSET
    shipping_method: str | Unset = UNSET
    inventory_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.area_scope import AreaScope # noqa: PLC0415
        threshold_type = self.threshold_type.value

        type_ = self.type_

        area_scope = self.area_scope.to_dict()

        threshold_value = self.threshold_value

        value = self.value

        shipping_method = self.shipping_method

        inventory_type = self.inventory_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "threshold_type": threshold_type,
            "type": type_,
            "area_scope": area_scope,
        })
        if threshold_value is not UNSET:
            field_dict["threshold_value"] = threshold_value
        if value is not UNSET:
            field_dict["value"] = value
        if shipping_method is not UNSET:
            field_dict["shipping_method"] = shipping_method
        if inventory_type is not UNSET:
            field_dict["inventory_type"] = inventory_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.area_scope import AreaScope # noqa: PLC0415
        d = dict(src_dict)
        threshold_type = ShippingDiscountThresholdType(d.pop("threshold_type"))




        type_ = d.pop("type")

        area_scope = AreaScope.from_dict(d.pop("area_scope"))




        threshold_value = d.pop("threshold_value", UNSET)

        value = d.pop("value", UNSET)

        shipping_method = d.pop("shipping_method", UNSET)

        inventory_type = d.pop("inventory_type", UNSET)

        shipping_discount = cls(
            threshold_type=threshold_type,
            type_=type_,
            area_scope=area_scope,
            threshold_value=threshold_value,
            value=value,
            shipping_method=shipping_method,
            inventory_type=inventory_type,
        )


        shipping_discount.additional_properties = d
        return shipping_discount

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
