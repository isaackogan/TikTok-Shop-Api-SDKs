from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_order_list_request_order_status import GetOrderListRequestOrderStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetOrderListRequest")



@_attrs_define
class GetOrderListRequest:
    """ 
        Attributes:
            order_status (GetOrderListRequestOrderStatus | Unset): Specific order status.
                Available values:
                - `UNPAID`: The order has been placed, but payment has not been completed.
                - `ON_HOLD`: The order has been accepted and is awaiting fulfillment. The buyer may still cancel without the
                seller’s approval. If `order_type=PRE_ORDER`, the product is still awaiting release so payment will only be
                authorized 1 day before the release, but the seller should start preparing for the release.
                - `AWAITING_SHIPMENT`: The order is ready to be shipped, but no items have been shipped yet.
                - `PARTIALLY_SHIPPING`: Some items in the order have been shipped, but not all.
                - `AWAITING_COLLECTION`: Shipping has been arranged, but the package is waiting to be collected by the carrier.
                - `IN_TRANSIT`: The package has been collected by the carrier and delivery is in progress.
                - `DELIVERED`: The package has been delivered to the buyer.
                - `COMPLETED`: The order has been completed, and no further returns or refunds are allowed.
                - `CANCELLED`: The order has been cancelled.
            create_time_ge (int | Unset): Filter orders to show only those that are created on or after the specified date
                and time. Unix timestamp.

                Note:
                `create_time_ge` and `create_time_lt` together constitute the creation time filter condition.
                - If `create_time_ge` is filled but `create_time_lt` is empty, `create_time_lt` will default to the current
                time.
                - If `create_time_lt` is filled but `create_time_ge` is empty, `create_time_ge` will default to the earliest
                shop time.
            create_time_lt (int | Unset): Filter orders to show only those that are created before the specified date and
                time. Unix timestamp.
                Refer to notes in `create_time_ge` for more usage information.
            update_time_ge (int | Unset): Filter orders to show only those that are updated on or after the specified date
                and time. Unix timestamp.

                Note:
                `update_time_ge` and `update_time_lt` together define the update time filter condition.
                - If `update_time_ge` is filled but `update_time_lt` is empty, `update_time_lt` will default to the current
                time.
                - If `update_time_lt` is filled but `update_time_ge` is empty, `update_time_ge` will default to the earliest
                shop time.

                Update times may exceed the selected search range due to ongoing data refreshes during the search process.
            update_time_lt (int | Unset): Filter orders to show only those that are updated before the specified date and
                time. Unix timestamp.
                Refer to notes in `update_time_ge` for more usage information.

                Update times may exceed the selected search range due to ongoing data refreshes during the search process.
            shipping_type (str | Unset): The delivery method.
                - `TIKTOK`: Shipping service provided by TikTok. The seller should obtain a shipping label from TikTok.
                - `SELLER`: Seller provides shipping, including through 3rd party fulfillment providers on behalf of the seller.
                - `TIKTOK_DIGITAL`: Tiktok delivers virtual goods directly to buyers. There is no action needed.
                - `IN-STORE PICKUP` : Buyer pickup the goods directly at seller location. Available for SEA market only.
            buyer_user_id (str | Unset): Buyer user ID.
            is_buyer_request_cancel (bool | Unset): Whether the buyer has initiated an order cancellation request.
            warehouse_ids (list[str] | Unset): Filter orders by pickup/sales warehouse IDs.
                Applicable only if the multi-warehouse feature is enabled.
                Max count: 100
     """

    order_status: GetOrderListRequestOrderStatus | Unset = UNSET
    create_time_ge: int | Unset = UNSET
    create_time_lt: int | Unset = UNSET
    update_time_ge: int | Unset = UNSET
    update_time_lt: int | Unset = UNSET
    shipping_type: str | Unset = UNSET
    buyer_user_id: str | Unset = UNSET
    is_buyer_request_cancel: bool | Unset = UNSET
    warehouse_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_status: str | Unset = UNSET
        if not isinstance(self.order_status, Unset):
            order_status = self.order_status.value


        create_time_ge = self.create_time_ge

        create_time_lt = self.create_time_lt

        update_time_ge = self.update_time_ge

        update_time_lt = self.update_time_lt

        shipping_type = self.shipping_type

        buyer_user_id = self.buyer_user_id

        is_buyer_request_cancel = self.is_buyer_request_cancel

        warehouse_ids: list[str] | Unset = UNSET
        if not isinstance(self.warehouse_ids, Unset):
            warehouse_ids = self.warehouse_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_status is not UNSET:
            field_dict["order_status"] = order_status
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if create_time_lt is not UNSET:
            field_dict["create_time_lt"] = create_time_lt
        if update_time_ge is not UNSET:
            field_dict["update_time_ge"] = update_time_ge
        if update_time_lt is not UNSET:
            field_dict["update_time_lt"] = update_time_lt
        if shipping_type is not UNSET:
            field_dict["shipping_type"] = shipping_type
        if buyer_user_id is not UNSET:
            field_dict["buyer_user_id"] = buyer_user_id
        if is_buyer_request_cancel is not UNSET:
            field_dict["is_buyer_request_cancel"] = is_buyer_request_cancel
        if warehouse_ids is not UNSET:
            field_dict["warehouse_ids"] = warehouse_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _order_status = d.pop("order_status", UNSET)
        order_status: GetOrderListRequestOrderStatus | Unset
        if isinstance(_order_status,  Unset):
            order_status = UNSET
        else:
            order_status = GetOrderListRequestOrderStatus(_order_status)




        create_time_ge = d.pop("create_time_ge", UNSET)

        create_time_lt = d.pop("create_time_lt", UNSET)

        update_time_ge = d.pop("update_time_ge", UNSET)

        update_time_lt = d.pop("update_time_lt", UNSET)

        shipping_type = d.pop("shipping_type", UNSET)

        buyer_user_id = d.pop("buyer_user_id", UNSET)

        is_buyer_request_cancel = d.pop("is_buyer_request_cancel", UNSET)

        warehouse_ids = cast(list[str], d.pop("warehouse_ids", UNSET))


        get_order_list_request = cls(
            order_status=order_status,
            create_time_ge=create_time_ge,
            create_time_lt=create_time_lt,
            update_time_ge=update_time_ge,
            update_time_lt=update_time_lt,
            shipping_type=shipping_type,
            buyer_user_id=buyer_user_id,
            is_buyer_request_cancel=is_buyer_request_cancel,
            warehouse_ids=warehouse_ids,
        )


        get_order_list_request.additional_properties = d
        return get_order_list_request

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
