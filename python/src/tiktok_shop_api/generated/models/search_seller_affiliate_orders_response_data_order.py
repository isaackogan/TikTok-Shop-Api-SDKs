from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_seller_affiliate_orders_response_data_order_sku import (
        SearchSellerAffiliateOrdersResponseDataOrderSku,
    )


T = TypeVar("T", bound="SearchSellerAffiliateOrdersResponseDataOrder")


@_attrs_define
class SearchSellerAffiliateOrdersResponseDataOrder:
    """
    Attributes:
        id (str | Unset): The order ID.
        delivery_time (int | Unset): The date and time when the order was delivered. Unix timestamp.
        create_time (int | Unset): The Unix timestamp, in seconds, when the order was created.
        status (str | Unset): Deprecated. This field is not returned. Use each SKU's `settlement_status` instead.
        skus (list[SearchSellerAffiliateOrdersResponseDataOrderSku] | Unset): The list of SKUs that are included in this
            order.
    """

    id: str | Unset = UNSET
    delivery_time: int | Unset = UNSET
    create_time: int | Unset = UNSET
    status: str | Unset = UNSET
    skus: list[SearchSellerAffiliateOrdersResponseDataOrderSku] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        delivery_time = self.delivery_time

        create_time = self.create_time

        status = self.status

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if delivery_time is not UNSET:
            field_dict["delivery_time"] = delivery_time
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if status is not UNSET:
            field_dict["status"] = status
        if skus is not UNSET:
            field_dict["skus"] = skus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_seller_affiliate_orders_response_data_order_sku import (
            SearchSellerAffiliateOrdersResponseDataOrderSku,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        delivery_time = d.pop("delivery_time", UNSET)

        create_time = d.pop("create_time", UNSET)

        status = d.pop("status", UNSET)

        _skus = d.pop("skus", UNSET)
        skus: list[SearchSellerAffiliateOrdersResponseDataOrderSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = SearchSellerAffiliateOrdersResponseDataOrderSku.from_dict(skus_item_data)

                skus.append(skus_item)

        search_seller_affiliate_orders_response_data_order = cls(
            id=id,
            delivery_time=delivery_time,
            create_time=create_time,
            status=status,
            skus=skus,
        )

        search_seller_affiliate_orders_response_data_order.additional_properties = d
        return search_seller_affiliate_orders_response_data_order

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
