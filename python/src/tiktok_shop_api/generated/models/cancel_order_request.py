from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order_line_list import OrderLineList
    from ..models.sku import Sku


T = TypeVar("T", bound="CancelOrderRequest")


@_attrs_define
class CancelOrderRequest:
    """
    Attributes:
        order_id (str): TikTok Shop order id
        cancel_reason (str): Reason for canceling the order. To obtain a reason for this order, call `GET
            /return_refund/202602/orders/{order_id}/aftersale_eligibility` with the same `order_id`,
            `initiate_aftersale_user=SELLER`, and `request_types=CANCEL`. From the corresponding
            `data.sku_eligibility[].line_item_eligibility[]` result, pass an exact value from `available_reason_names` as
            `cancel_reason`. See "Return API Overview" for additional guidance on seller cancellation reasons.
        skus (list[Sku] | Unset): List of SKU to cancel
        order_line_item_ids (list[str] | Unset): List of order line item IDs to cancel. In the US and UK markets, when
            an item is out of stock, partial cancellation at the individual item level is supported. To initiate a partial
            cancellation, specify the item's order line ID. **Note:** This is a legacy field. For new integrations, use
            `order_line_list` instead. Do not provide non-empty values in both `order_line_item_ids` and `order_line_list`
            in the same request.
        order_line_list (list[OrderLineList] | Unset): List of order lines or sub-order lines to cancel. In the US and
            UK markets, when an item is out of stock, partial cancellation at the individual item level is supported.
            **Note:** This field is completely backward compatible with the previous `order_line_item_ids` field. Do not
            provide non-empty values in both `order_line_list` and `order_line_item_ids` in the same request.
    """

    order_id: str
    cancel_reason: str
    skus: list[Sku] | Unset = UNSET
    order_line_item_ids: list[str] | Unset = UNSET
    order_line_list: list[OrderLineList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        cancel_reason = self.cancel_reason

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)

        order_line_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_line_item_ids, Unset):
            order_line_item_ids = self.order_line_item_ids

        order_line_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.order_line_list, Unset):
            order_line_list = []
            for order_line_list_item_data in self.order_line_list:
                order_line_list_item = order_line_list_item_data.to_dict()
                order_line_list.append(order_line_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order_id": order_id,
                "cancel_reason": cancel_reason,
            }
        )
        if skus is not UNSET:
            field_dict["skus"] = skus
        if order_line_item_ids is not UNSET:
            field_dict["order_line_item_ids"] = order_line_item_ids
        if order_line_list is not UNSET:
            field_dict["order_line_list"] = order_line_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_line_list import OrderLineList  # noqa: PLC0415
        from ..models.sku import Sku  # noqa: PLC0415

        d = dict(src_dict)
        order_id = d.pop("order_id")

        cancel_reason = d.pop("cancel_reason")

        _skus = d.pop("skus", UNSET)
        skus: list[Sku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = Sku.from_dict(skus_item_data)

                skus.append(skus_item)

        order_line_item_ids = cast(list[str], d.pop("order_line_item_ids", UNSET))

        _order_line_list = d.pop("order_line_list", UNSET)
        order_line_list: list[OrderLineList] | Unset = UNSET
        if _order_line_list is not UNSET:
            order_line_list = []
            for order_line_list_item_data in _order_line_list:
                order_line_list_item = OrderLineList.from_dict(order_line_list_item_data)

                order_line_list.append(order_line_list_item)

        cancel_order_request = cls(
            order_id=order_id,
            cancel_reason=cancel_reason,
            skus=skus,
            order_line_item_ids=order_line_item_ids,
            order_line_list=order_line_list,
        )

        cancel_order_request.additional_properties = d
        return cancel_order_request

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
