from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSPSMetricTopItemsResponseDataNrrTopProductItem")


@_attrs_define
class GetSPSMetricTopItemsResponseDataNrrTopProductItem:
    """
    Attributes:
        delivered_order_count (int | Unset): Total number of delivered orders.
        image_url (str | Unset): Product image URL.
        negative_order_count (int | Unset): Number of orders with negative reviews.
        product_id (str | Unset): Product ID.
        product_name (str | Unset): Product name.
        top_review_reasons (list[str] | Unset): Top negative review reasons.
    """

    delivered_order_count: int | Unset = UNSET
    image_url: str | Unset = UNSET
    negative_order_count: int | Unset = UNSET
    product_id: str | Unset = UNSET
    product_name: str | Unset = UNSET
    top_review_reasons: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivered_order_count = self.delivered_order_count

        image_url = self.image_url

        negative_order_count = self.negative_order_count

        product_id = self.product_id

        product_name = self.product_name

        top_review_reasons: list[str] | Unset = UNSET
        if not isinstance(self.top_review_reasons, Unset):
            top_review_reasons = self.top_review_reasons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivered_order_count is not UNSET:
            field_dict["delivered_order_count"] = delivered_order_count
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if negative_order_count is not UNSET:
            field_dict["negative_order_count"] = negative_order_count
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if top_review_reasons is not UNSET:
            field_dict["top_review_reasons"] = top_review_reasons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delivered_order_count = d.pop("delivered_order_count", UNSET)

        image_url = d.pop("image_url", UNSET)

        negative_order_count = d.pop("negative_order_count", UNSET)

        product_id = d.pop("product_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        top_review_reasons = cast(list[str], d.pop("top_review_reasons", UNSET))

        get_sps_metric_top_items_response_data_nrr_top_product_item = cls(
            delivered_order_count=delivered_order_count,
            image_url=image_url,
            negative_order_count=negative_order_count,
            product_id=product_id,
            product_name=product_name,
            top_review_reasons=top_review_reasons,
        )

        get_sps_metric_top_items_response_data_nrr_top_product_item.additional_properties = d
        return get_sps_metric_top_items_response_data_nrr_top_product_item

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
