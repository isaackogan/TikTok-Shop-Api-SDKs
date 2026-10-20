from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_activity_response_data_discount_shipping_discount_area_scope import GetActivityResponseDataDiscountShippingDiscountAreaScope





T = TypeVar("T", bound="GetActivityResponseDataDiscountShippingDiscount")



@_attrs_define
class GetActivityResponseDataDiscountShippingDiscount:
    """ 
        Attributes:
            threshold_type (str | Unset): The type of purchase criteria. Possible enumerations are:
                - `NO_THRESHOLD`: No minimum purchase criteria.
                - `MINIMAL_ITEM_QUANTITY`: Buyer must meet or exceed the minimum spend criteria with eligible products.
                - `MINIMAL_ORDER_AMOUNT`: Buyer must meet or exceed the minimum spend criteria with eligible order.
                `MINIMAL_ITEM_QUANTITY` and `MINIMAL_ORDER_AMOUNT` can only be set when `product_level==SHOP`.
            threshold_value (str | Unset): The purchase threshold returned for the shipping discount, based on
                `threshold_type`.
                - When `threshold_type==NO_THRESHOLD`, this value is not required.
                - When `threshold_type==MINIMAL_ITEM_QUANTITY`, this is the number of eligible products the buyer must purchase
                and must be an integer.
                - When `threshold_type==MINIMAL_ORDER_AMOUNT`, this is the eligible-product subtotal the buyer must reach in
                local currency (for example, 3 units of local currency) and must have no more than two decimal places.
            type_ (str | Unset): The type of shipping discount returned for the promotion activity.
                - FREE_SHIPPING: The buyer's shipping charge is fully covered.
                - DISCOUNT_SHIPPING_FEE: The buyer's shipping charge is reduced by up to the amount in value.
            value (str | Unset): Value of the discount.
                - When `type==FREE_SHIPPING`, this value is not required.
                - `type==DISCOUNT_SHIPPING_FEE`, this value is the maximum amount deducted from the buyer's price of shipping in
                local currency.
                The value should be limited to two decimal places.
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
            area_scope (GetActivityResponseDataDiscountShippingDiscountAreaScope | Unset):
     """

    threshold_type: str | Unset = UNSET
    threshold_value: str | Unset = UNSET
    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    shipping_method: str | Unset = UNSET
    inventory_type: str | Unset = UNSET
    area_scope: GetActivityResponseDataDiscountShippingDiscountAreaScope | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_activity_response_data_discount_shipping_discount_area_scope import GetActivityResponseDataDiscountShippingDiscountAreaScope # noqa: PLC0415
        threshold_type = self.threshold_type

        threshold_value = self.threshold_value

        type_ = self.type_

        value = self.value

        shipping_method = self.shipping_method

        inventory_type = self.inventory_type

        area_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.area_scope, Unset):
            area_scope = self.area_scope.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if threshold_type is not UNSET:
            field_dict["threshold_type"] = threshold_type
        if threshold_value is not UNSET:
            field_dict["threshold_value"] = threshold_value
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value
        if shipping_method is not UNSET:
            field_dict["shipping_method"] = shipping_method
        if inventory_type is not UNSET:
            field_dict["inventory_type"] = inventory_type
        if area_scope is not UNSET:
            field_dict["area_scope"] = area_scope

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_activity_response_data_discount_shipping_discount_area_scope import GetActivityResponseDataDiscountShippingDiscountAreaScope # noqa: PLC0415
        d = dict(src_dict)
        threshold_type = d.pop("threshold_type", UNSET)

        threshold_value = d.pop("threshold_value", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        shipping_method = d.pop("shipping_method", UNSET)

        inventory_type = d.pop("inventory_type", UNSET)

        _area_scope = d.pop("area_scope", UNSET)
        area_scope: GetActivityResponseDataDiscountShippingDiscountAreaScope | Unset
        if isinstance(_area_scope,  Unset):
            area_scope = UNSET
        else:
            area_scope = GetActivityResponseDataDiscountShippingDiscountAreaScope.from_dict(_area_scope)




        get_activity_response_data_discount_shipping_discount = cls(
            threshold_type=threshold_type,
            threshold_value=threshold_value,
            type_=type_,
            value=value,
            shipping_method=shipping_method,
            inventory_type=inventory_type,
            area_scope=area_scope,
        )


        get_activity_response_data_discount_shipping_discount.additional_properties = d
        return get_activity_response_data_discount_shipping_discount

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
