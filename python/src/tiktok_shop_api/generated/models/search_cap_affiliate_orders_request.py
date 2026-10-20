from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchCAPAffiliateOrdersRequest")



@_attrs_define
class SearchCAPAffiliateOrdersRequest:
    """ 
        Attributes:
            order_id (str | Unset): Transaction main order ID
            product_id (str | Unset): Unique identifier for Product
            settle_status (int | Unset): Filter orders by settlement status. Send one of the following integer values; the
                response `settle_status` field uses the corresponding label:
                - `1` → `CUSTOMER UNPAID`: The customer has not paid for the order.
                - `2` → `PENDING`: The customer can still return the order or request a refund, so earnings are estimated and
                awaiting settlement.
                - `3` → `SETTLED`: Earnings have been settled to your account.
                - `4` → `INELIGIBLE`: The order was returned, refunded, or canceled, so no commission will be settled.
                - `5` → `FROZEN`: Possible fraud was detected; the commission will be unfrozen after the fraud is resolved.
            create_time_ge (int | Unset): Filter orders created at or after this time. Unix timestamp in seconds.
                `create_time_ge` and `create_time_lt` must be provided together. An explicitly supplied range can span at most
                92 days. If neither field is provided, the API searches from three calendar months before the request time
                through the request time.
            create_time_lt (int | Unset): Filter orders created before this time. Unix timestamp in seconds.
                `create_time_ge` and `create_time_lt` must be provided together.
     """

    order_id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    settle_status: int | Unset = UNSET
    create_time_ge: int | Unset = UNSET
    create_time_lt: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        product_id = self.product_id

        settle_status = self.settle_status

        create_time_ge = self.create_time_ge

        create_time_lt = self.create_time_lt


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if settle_status is not UNSET:
            field_dict["settle_status"] = settle_status
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if create_time_lt is not UNSET:
            field_dict["create_time_lt"] = create_time_lt

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        product_id = d.pop("product_id", UNSET)

        settle_status = d.pop("settle_status", UNSET)

        create_time_ge = d.pop("create_time_ge", UNSET)

        create_time_lt = d.pop("create_time_lt", UNSET)

        search_cap_affiliate_orders_request = cls(
            order_id=order_id,
            product_id=product_id,
            settle_status=settle_status,
            create_time_ge=create_time_ge,
            create_time_lt=create_time_lt,
        )


        search_cap_affiliate_orders_request.additional_properties = d
        return search_cap_affiliate_orders_request

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
