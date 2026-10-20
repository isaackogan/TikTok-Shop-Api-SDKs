from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.refund_amount import RefundAmount
  from ..models.search_cancellations_response_data_cancellation_cancel_line_item import SearchCancellationsResponseDataCancellationCancelLineItem
  from ..models.search_cancellations_response_data_cancellation_seller_next_action_response import SearchCancellationsResponseDataCancellationSellerNextActionResponse





T = TypeVar("T", bound="SearchCancellationsResponseDataCancellation")



@_attrs_define
class SearchCancellationsResponseDataCancellation:
    """ 
        Attributes:
            order_id (str | Unset): TikTok Shop order ID.
            cancel_type (str | Unset): Order cancellation type.
                Possible values:
                - `CANCEL`: Cancel by seller or system.
                - `BUYER_CANCEL`: Cancel by buyer. Need to be approved by seller or system.
            cancel_status (str | Unset): Order cancellation status.
                Possible values:
                - `CANCELLATION_REQUEST_PENDING`
                - `CANCELLATION_REQUEST_SUCCESS`
                - `CANCELLATION_REQUEST_CANCEL`
                - `CANCELLATION_REQUEST_COMPLETE`
            role (str | Unset): Order cancellation initiator.
                Possible values:
                - `BUYER`
                - `SELLER`
                - `OPERATOR`
                - `SYSTEM`
            cancel_reason (str | Unset): Order cancellation reason.
            cancel_reason_text (str | Unset): Order cancellation reason, localized to another language.
                You can change language using the locale field in the request parameter.
            create_time (int | Unset): The time when the order cancellation was created. Unix timestamp in seconds.
            update_time (int | Unset): The time when the order cancellation was last updated. Unix timestamp in seconds.
            seller_next_action_response (list[SearchCancellationsResponseDataCancellationSellerNextActionResponse] | Unset):
                Seller's next action and deadline.
            refund_amount (RefundAmount | Unset):
            cancel_line_items (list[SearchCancellationsResponseDataCancellationCancelLineItem] | Unset): Cancellation line
                items.
            cancel_id (str | Unset): The identifier of a specific order cancellation.
            should_replenish_stock (bool | Unset): Should seller replenish the stock when order cancelled successfully.
     """

    order_id: str | Unset = UNSET
    cancel_type: str | Unset = UNSET
    cancel_status: str | Unset = UNSET
    role: str | Unset = UNSET
    cancel_reason: str | Unset = UNSET
    cancel_reason_text: str | Unset = UNSET
    create_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    seller_next_action_response: list[SearchCancellationsResponseDataCancellationSellerNextActionResponse] | Unset = UNSET
    refund_amount: RefundAmount | Unset = UNSET
    cancel_line_items: list[SearchCancellationsResponseDataCancellationCancelLineItem] | Unset = UNSET
    cancel_id: str | Unset = UNSET
    should_replenish_stock: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.refund_amount import RefundAmount # noqa: PLC0415
        from ..models.search_cancellations_response_data_cancellation_cancel_line_item import SearchCancellationsResponseDataCancellationCancelLineItem # noqa: PLC0415
        from ..models.search_cancellations_response_data_cancellation_seller_next_action_response import SearchCancellationsResponseDataCancellationSellerNextActionResponse # noqa: PLC0415
        order_id = self.order_id

        cancel_type = self.cancel_type

        cancel_status = self.cancel_status

        role = self.role

        cancel_reason = self.cancel_reason

        cancel_reason_text = self.cancel_reason_text

        create_time = self.create_time

        update_time = self.update_time

        seller_next_action_response: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.seller_next_action_response, Unset):
            seller_next_action_response = []
            for seller_next_action_response_item_data in self.seller_next_action_response:
                seller_next_action_response_item = seller_next_action_response_item_data.to_dict()
                seller_next_action_response.append(seller_next_action_response_item)



        refund_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refund_amount, Unset):
            refund_amount = self.refund_amount.to_dict()

        cancel_line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cancel_line_items, Unset):
            cancel_line_items = []
            for cancel_line_items_item_data in self.cancel_line_items:
                cancel_line_items_item = cancel_line_items_item_data.to_dict()
                cancel_line_items.append(cancel_line_items_item)



        cancel_id = self.cancel_id

        should_replenish_stock = self.should_replenish_stock


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if cancel_type is not UNSET:
            field_dict["cancel_type"] = cancel_type
        if cancel_status is not UNSET:
            field_dict["cancel_status"] = cancel_status
        if role is not UNSET:
            field_dict["role"] = role
        if cancel_reason is not UNSET:
            field_dict["cancel_reason"] = cancel_reason
        if cancel_reason_text is not UNSET:
            field_dict["cancel_reason_text"] = cancel_reason_text
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if seller_next_action_response is not UNSET:
            field_dict["seller_next_action_response"] = seller_next_action_response
        if refund_amount is not UNSET:
            field_dict["refund_amount"] = refund_amount
        if cancel_line_items is not UNSET:
            field_dict["cancel_line_items"] = cancel_line_items
        if cancel_id is not UNSET:
            field_dict["cancel_id"] = cancel_id
        if should_replenish_stock is not UNSET:
            field_dict["should_replenish_stock"] = should_replenish_stock

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refund_amount import RefundAmount # noqa: PLC0415
        from ..models.search_cancellations_response_data_cancellation_cancel_line_item import SearchCancellationsResponseDataCancellationCancelLineItem # noqa: PLC0415
        from ..models.search_cancellations_response_data_cancellation_seller_next_action_response import SearchCancellationsResponseDataCancellationSellerNextActionResponse # noqa: PLC0415
        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        cancel_type = d.pop("cancel_type", UNSET)

        cancel_status = d.pop("cancel_status", UNSET)

        role = d.pop("role", UNSET)

        cancel_reason = d.pop("cancel_reason", UNSET)

        cancel_reason_text = d.pop("cancel_reason_text", UNSET)

        create_time = d.pop("create_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        _seller_next_action_response = d.pop("seller_next_action_response", UNSET)
        seller_next_action_response: list[SearchCancellationsResponseDataCancellationSellerNextActionResponse] | Unset = UNSET
        if _seller_next_action_response is not UNSET:
            seller_next_action_response = []
            for seller_next_action_response_item_data in _seller_next_action_response:
                seller_next_action_response_item = SearchCancellationsResponseDataCancellationSellerNextActionResponse.from_dict(seller_next_action_response_item_data)



                seller_next_action_response.append(seller_next_action_response_item)


        _refund_amount = d.pop("refund_amount", UNSET)
        refund_amount: RefundAmount | Unset
        if isinstance(_refund_amount,  Unset):
            refund_amount = UNSET
        else:
            refund_amount = RefundAmount.from_dict(_refund_amount)




        _cancel_line_items = d.pop("cancel_line_items", UNSET)
        cancel_line_items: list[SearchCancellationsResponseDataCancellationCancelLineItem] | Unset = UNSET
        if _cancel_line_items is not UNSET:
            cancel_line_items = []
            for cancel_line_items_item_data in _cancel_line_items:
                cancel_line_items_item = SearchCancellationsResponseDataCancellationCancelLineItem.from_dict(cancel_line_items_item_data)



                cancel_line_items.append(cancel_line_items_item)


        cancel_id = d.pop("cancel_id", UNSET)

        should_replenish_stock = d.pop("should_replenish_stock", UNSET)

        search_cancellations_response_data_cancellation = cls(
            order_id=order_id,
            cancel_type=cancel_type,
            cancel_status=cancel_status,
            role=role,
            cancel_reason=cancel_reason,
            cancel_reason_text=cancel_reason_text,
            create_time=create_time,
            update_time=update_time,
            seller_next_action_response=seller_next_action_response,
            refund_amount=refund_amount,
            cancel_line_items=cancel_line_items,
            cancel_id=cancel_id,
            should_replenish_stock=should_replenish_stock,
        )


        search_cancellations_response_data_cancellation.additional_properties = d
        return search_cancellations_response_data_cancellation

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
