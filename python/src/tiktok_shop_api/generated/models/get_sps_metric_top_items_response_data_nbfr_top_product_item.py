from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSPSMetricTopItemsResponseDataNbfrTopProductItem")


@_attrs_define
class GetSPSMetricTopItemsResponseDataNbfrTopProductItem:
    """
    Attributes:
        product_id (str | Unset): Product ID.
        product_name (str | Unset): Product name.
        return_order_count (int | Unset): Number of return or refund orders.
        top_reason_order_count (int | Unset): Number of orders associated with the top return or refund reason.
        top_return_reasons (list[str] | Unset): Top return or refund reasons.
        image_url (str | Unset): Product image URL.
    """

    product_id: str | Unset = UNSET
    product_name: str | Unset = UNSET
    return_order_count: int | Unset = UNSET
    top_reason_order_count: int | Unset = UNSET
    top_return_reasons: list[str] | Unset = UNSET
    image_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        product_name = self.product_name

        return_order_count = self.return_order_count

        top_reason_order_count = self.top_reason_order_count

        top_return_reasons: list[str] | Unset = UNSET
        if not isinstance(self.top_return_reasons, Unset):
            top_return_reasons = self.top_return_reasons

        image_url = self.image_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if return_order_count is not UNSET:
            field_dict["return_order_count"] = return_order_count
        if top_reason_order_count is not UNSET:
            field_dict["top_reason_order_count"] = top_reason_order_count
        if top_return_reasons is not UNSET:
            field_dict["top_return_reasons"] = top_return_reasons
        if image_url is not UNSET:
            field_dict["image_url"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        return_order_count = d.pop("return_order_count", UNSET)

        top_reason_order_count = d.pop("top_reason_order_count", UNSET)

        top_return_reasons = cast(list[str], d.pop("top_return_reasons", UNSET))

        image_url = d.pop("image_url", UNSET)

        get_sps_metric_top_items_response_data_nbfr_top_product_item = cls(
            product_id=product_id,
            product_name=product_name,
            return_order_count=return_order_count,
            top_reason_order_count=top_reason_order_count,
            top_return_reasons=top_return_reasons,
            image_url=image_url,
        )

        get_sps_metric_top_items_response_data_nbfr_top_product_item.additional_properties = d
        return get_sps_metric_top_items_response_data_nbfr_top_product_item

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
