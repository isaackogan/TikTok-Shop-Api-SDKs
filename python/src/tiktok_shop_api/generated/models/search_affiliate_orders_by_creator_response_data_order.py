from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_affiliate_orders_by_creator_response_data_order_sku import (
        SearchAffiliateOrdersByCreatorResponseDataOrderSku,
    )


T = TypeVar("T", bound="SearchAffiliateOrdersByCreatorResponseDataOrder")


@_attrs_define
class SearchAffiliateOrdersByCreatorResponseDataOrder:
    """
    Attributes:
        id (int | Unset): The order identifier.
        status (str | Unset): The current status of the order. Possible values:
            - UNSPECIFIED: The status is undefined and may be updated later.
            - ORDERED: The order has been placed, but commission has not been settled. The estimated commission is
            available.
            - SETTLED: The commission has been settled. Actual commission values are populated when the corresponding
            settled amounts are available.
            - REFUNDED: The order was returned, refunded, or canceled by the buyer; actual commission and actual commission
            base amounts are returned as localized zero values.
            - FROZEN: Possible fraud was detected. Commission remains frozen until the issue is resolved.
            - DEDUCTED: An additional deduction was made from the balance account.

            For statuses other than SETTLED or REFUNDED, actual commission values can be empty. Bonus, shop ads, and creator
            commission reward amounts are populated only when the corresponding commission data exists; their availability
            is not determined by order status alone.
        skus (list[SearchAffiliateOrdersByCreatorResponseDataOrderSku] | Unset): A list of SKUs associated with the
            order.
        create_time (int | Unset): Time and date of order created, UTC+0 timing
        delivery_time (int | Unset): Time and date order delivered, UTC+0 timing
    """

    id: int | Unset = UNSET
    status: str | Unset = UNSET
    skus: list[SearchAffiliateOrdersByCreatorResponseDataOrderSku] | Unset = UNSET
    create_time: int | Unset = UNSET
    delivery_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)

        create_time = self.create_time

        delivery_time = self.delivery_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if skus is not UNSET:
            field_dict["skus"] = skus
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if delivery_time is not UNSET:
            field_dict["delivery_time"] = delivery_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_affiliate_orders_by_creator_response_data_order_sku import (
            SearchAffiliateOrdersByCreatorResponseDataOrderSku,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        _skus = d.pop("skus", UNSET)
        skus: list[SearchAffiliateOrdersByCreatorResponseDataOrderSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = SearchAffiliateOrdersByCreatorResponseDataOrderSku.from_dict(skus_item_data)

                skus.append(skus_item)

        create_time = d.pop("create_time", UNSET)

        delivery_time = d.pop("delivery_time", UNSET)

        search_affiliate_orders_by_creator_response_data_order = cls(
            id=id,
            status=status,
            skus=skus,
            create_time=create_time,
            delivery_time=delivery_time,
        )

        search_affiliate_orders_by_creator_response_data_order.additional_properties = d
        return search_affiliate_orders_by_creator_response_data_order

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
