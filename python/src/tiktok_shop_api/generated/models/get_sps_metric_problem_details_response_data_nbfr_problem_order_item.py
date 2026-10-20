from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSPSMetricProblemDetailsResponseDataNbfrProblemOrderItem")


@_attrs_define
class GetSPSMetricProblemDetailsResponseDataNbfrProblemOrderItem:
    """
    Attributes:
        deliver_time (int | Unset): Delivery time. Unix timestamp in seconds.
        order_create_time (int | Unset): Order creation time. Unix timestamp in seconds.
        order_id (str | Unset): Order ID.
        product_id (str | Unset): Product ID, when available.
        product_name (str | Unset): Product name.
        return_refund_reason (str | Unset): Return or refund reason.
        sku_id (str | Unset): SKU ID.
    """

    deliver_time: int | Unset = UNSET
    order_create_time: int | Unset = UNSET
    order_id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    product_name: str | Unset = UNSET
    return_refund_reason: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deliver_time = self.deliver_time

        order_create_time = self.order_create_time

        order_id = self.order_id

        product_id = self.product_id

        product_name = self.product_name

        return_refund_reason = self.return_refund_reason

        sku_id = self.sku_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deliver_time is not UNSET:
            field_dict["deliver_time"] = deliver_time
        if order_create_time is not UNSET:
            field_dict["order_create_time"] = order_create_time
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if return_refund_reason is not UNSET:
            field_dict["return_refund_reason"] = return_refund_reason
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deliver_time = d.pop("deliver_time", UNSET)

        order_create_time = d.pop("order_create_time", UNSET)

        order_id = d.pop("order_id", UNSET)

        product_id = d.pop("product_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        return_refund_reason = d.pop("return_refund_reason", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        get_sps_metric_problem_details_response_data_nbfr_problem_order_item = cls(
            deliver_time=deliver_time,
            order_create_time=order_create_time,
            order_id=order_id,
            product_id=product_id,
            product_name=product_name,
            return_refund_reason=return_refund_reason,
            sku_id=sku_id,
        )

        get_sps_metric_problem_details_response_data_nbfr_problem_order_item.additional_properties = d
        return get_sps_metric_problem_details_response_data_nbfr_problem_order_item

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
