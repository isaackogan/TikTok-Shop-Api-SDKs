from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partial_refund import PartialRefund
    from ..models.refund_amount import RefundAmount
    from ..models.return_warehouse_address import ReturnWarehouseAddress
    from ..models.search_returns_response_data_return_order_discount_amount import (
        SearchReturnsResponseDataReturnOrderDiscountAmount,
    )
    from ..models.search_returns_response_data_return_order_return_line_item import (
        SearchReturnsResponseDataReturnOrderReturnLineItem,
    )
    from ..models.search_returns_response_data_return_order_shipping_fee_amount import (
        SearchReturnsResponseDataReturnOrderShippingFeeAmount,
    )
    from ..models.seller_next_action_response import SellerNextActionResponse


T = TypeVar("T", bound="SearchReturnsResponseDataReturnOrder")


@_attrs_define
class SearchReturnsResponseDataReturnOrder:
    """
    Attributes:
        order_id (str | Unset): TikTok Shop order ID.
        return_id (str | Unset): The identifier of a specific return.
        return_type (str | Unset): Return type.
            Available values:
            - `REFUND`: Seller will issue a refund without return. The buyer is not required to send the item(s) back to the
            seller.
            - `RETURN_AND_REFUND`: Buyer is required to send the item(s) back to the seller. The seller will need to review
            the condition of the returned item(s) before a refund can be issued to the buyer.
            - `REPLACEMENT`: The buyer requires the seller to replace the item(s).
            - `EXCHANGE`: The buyer requires the seller to exchange the item(s).
        return_status (str | Unset): Return status.
            Available values:
            - `RETURN_OR_REFUND_REQUEST_PENDING`: Buyer has initiated a return or refund request. The request is pending
            review by seller or platform.
            - `REFUND_OR_RETURN_REQUEST_REJECT`: The return or refund request was rejected.
            - `AWAITING_BUYER_SHIP`: The return request was approved. The seller is waiting for the buyer to ship the
            approved items to the seller. If the buyer doesn't ship the items to the seller before the deadline, the
            platform will close the request.
            - `BUYER_SHIPPED_ITEM`: Buyer has shipped the approved items to seller.
            - `REJECT_RECEIVE_PACKAGE`: Seller inspected the returned items and rejected the return package.
            - `RETURN_OR_REFUND_REQUEST_SUCCESS`: The return/refund request was approved. The buyer will be refunded.
            - `RETURN_OR_REFUND_REQUEST_CANCEL`: The request has been cancelled by the buyer or system.
            - `RETURN_OR_REFUND_REQUEST_COMPLETE`: The return/refund was processed successfully. The buyer has been
            refunded.
            - `REPLACEMENT_REQUEST_PENDING`: Buyer has initiated a replacement request. The request is pending review by
            seller.
            - `REPLACEMENT_REQUEST_REJECT`: Seller reject the buyer replacement request.
            - `REPLACEMENT_REQUEST_REFUND_SUCCESS`: Buyer's replacement request was resolved by refund due to insufficient
            inventory.
            - `REPLACEMENT_REQUEST_CANCEL`: Buyer canceled the replacement request.
            - `REPLACEMENT_REQUEST_COMPLETE`: Seller has approved the buyer's replacement request, platform will generate a
            new order for seller to fulfill.
            - `AWAITING_BUYER_RESPONSE`: Seller offer another return type to the buyer, and waiting buyer response. Seller
            proposed return type can check the `seller_proposed_return_type`.
            - `EXCHANGE_REQUEST_PENDING`: Buyer has initiated an exchange request. The request is pending review by seller.
            - `EXCHANGE_REQUEST_REFUND_SUCCESS`: Buyer's exchange request was resolved by refund due to insufficient
            inventory.
            - `EXCHANGE_REQUEST_CANCEL`: Buyer canceled the exchange request.
            - `EXCHANGE_REQUEST_COMPLETE`: Seller has approved the buyer's exchange request, platform will generate a new
            order for seller to fulfill.
        arbitration_status (str | Unset): Arbitration status.
            Available values:
            - `IN_PROGRESS`: The TikTok Shop platform operator is processing arbitration and may request additional
            information from the seller.
            - `SUPPORT_BUYER`: The platform operator supports the buyer.
            - `SUPPORT_SELLER`: The platform operator supports the seller.
            - `CLOSED`: Arbitration is closed.
        role (str | Unset): Return initiation role.
            Available values:
            - `BUYER`
            - `SELLER`
            - `OPERATOR` : TikTok Shop platform operator.
            - `SYSTEM`:  TikTok Shop system.
            Please see "API overview" to learn more about roles.
        return_reason (str | Unset): Machine-readable reason code for the return. Use `return_reason_text` for localized
            display text.
        return_reason_text (str | Unset): Reason for return, in localized text.
            You can change language using the locale request parameter.
        shipment_type (str | Unset): The shipment method selected by the buyer for sending the item(s) back to the
            seller.
            Available values:
            - `PLATFORM`: The buyer uses TikTok Shop's shipping service. See `handover_method` for whether the buyer uses
            `DROP_OFF` or `PICKUP`.
            - `BUYER_ARRANGE`: The buyer arranges the return shipment.
        handover_method (str | Unset): The handover method buyer chooses to use when returning item(s) to seller using
            platform's shipping service.
            - `DROP_OFF`: buyer will drop off the item(s) at courier
            - `PICKUP`: buyer is scheduling a pick up service offered by the courier.
        return_tracking_number (str | Unset): The tracking number of parcels when buyer returns the item(s).
        return_provider_name (str | Unset): The provider name of parcel when buyer returns the item(s).
        return_provider_id (str | Unset): The provider ID of parcel when buyer returns the items.
        pre_return_id (str | Unset): The previous return ID the current return order is edited from.
        next_return_id (str | Unset): The next return ID the current return order is edited to.
        can_buyer_keep_item (bool | Unset): Indicates whether the buyer may keep the item(s). This field is returned as
            `true` for replacement requests and is omitted for other return types.
        update_time (int | Unset): The time when the return was last updated, as a Unix timestamp in seconds.
        seller_next_action_response (list[SellerNextActionResponse] | Unset): Seller's next action and deadline.
        create_time (int | Unset): The time when the return was created, as a Unix timestamp in seconds.
        return_line_items (list[SearchReturnsResponseDataReturnOrderReturnLineItem] | Unset): Return order lines items.
        discount_amount (list[SearchReturnsResponseDataReturnOrderDiscountAmount] | Unset): Discount refund details.
        shipping_fee_amount (list[SearchReturnsResponseDataReturnOrderShippingFeeAmount] | Unset): The return shipping
            fee details.
        refund_amount (RefundAmount | Unset):
        return_shipping_document_type (str | Unset): The type of return shipping document selected by the buyer.
            Available values:
            - `SHIPPING_LABEL`
            - `QR_CODE` - QR Code with Box
            - `QR_CODE_NBNL` - QR Code with No Box No Label
        return_method (str | Unset): Return method:
            - `SELLER_SHIPPED`: Seller offers the return shipping service.
            - `BUYER_SHIPPED`: Buyer offers the return shipping service.
            - `PLATFORM_SHIPPED`: TikTok Shop offers the return shipping service.
        is_combined_return (bool | Unset): This field will return true if the buyer is asking to combine multiple
            returns into one return package.
        combined_return_id (str | Unset): If `is_combined_return` is `true`, this field will return the
            `combined_return_id` associated with the combined return.
        seller_proposed_return_type (str | Unset): Seller proposed return type:
            - `PARTIAL_REFUND`
        partial_refund (PartialRefund | Unset):
        buyer_rejected_partial_refund (bool | Unset): Only return this field when seller initiated the partial refund.
            Available values:
            - `TRUE`: Buyer reject the seller partial refund offer.
            - `FALSE`: Buyer accept the seller partial refund offer or awaiting buyer response.
        return_warehouse_address (ReturnWarehouseAddress | Unset):
        is_quick_refund (bool | Unset): If the return hit the quick refund strategy, the seller cannot reject the
            received package
    """

    order_id: str | Unset = UNSET
    return_id: str | Unset = UNSET
    return_type: str | Unset = UNSET
    return_status: str | Unset = UNSET
    arbitration_status: str | Unset = UNSET
    role: str | Unset = UNSET
    return_reason: str | Unset = UNSET
    return_reason_text: str | Unset = UNSET
    shipment_type: str | Unset = UNSET
    handover_method: str | Unset = UNSET
    return_tracking_number: str | Unset = UNSET
    return_provider_name: str | Unset = UNSET
    return_provider_id: str | Unset = UNSET
    pre_return_id: str | Unset = UNSET
    next_return_id: str | Unset = UNSET
    can_buyer_keep_item: bool | Unset = UNSET
    update_time: int | Unset = UNSET
    seller_next_action_response: list[SellerNextActionResponse] | Unset = UNSET
    create_time: int | Unset = UNSET
    return_line_items: list[SearchReturnsResponseDataReturnOrderReturnLineItem] | Unset = UNSET
    discount_amount: list[SearchReturnsResponseDataReturnOrderDiscountAmount] | Unset = UNSET
    shipping_fee_amount: list[SearchReturnsResponseDataReturnOrderShippingFeeAmount] | Unset = UNSET
    refund_amount: RefundAmount | Unset = UNSET
    return_shipping_document_type: str | Unset = UNSET
    return_method: str | Unset = UNSET
    is_combined_return: bool | Unset = UNSET
    combined_return_id: str | Unset = UNSET
    seller_proposed_return_type: str | Unset = UNSET
    partial_refund: PartialRefund | Unset = UNSET
    buyer_rejected_partial_refund: bool | Unset = UNSET
    return_warehouse_address: ReturnWarehouseAddress | Unset = UNSET
    is_quick_refund: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        return_id = self.return_id

        return_type = self.return_type

        return_status = self.return_status

        arbitration_status = self.arbitration_status

        role = self.role

        return_reason = self.return_reason

        return_reason_text = self.return_reason_text

        shipment_type = self.shipment_type

        handover_method = self.handover_method

        return_tracking_number = self.return_tracking_number

        return_provider_name = self.return_provider_name

        return_provider_id = self.return_provider_id

        pre_return_id = self.pre_return_id

        next_return_id = self.next_return_id

        can_buyer_keep_item = self.can_buyer_keep_item

        update_time = self.update_time

        seller_next_action_response: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.seller_next_action_response, Unset):
            seller_next_action_response = []
            for seller_next_action_response_item_data in self.seller_next_action_response:
                seller_next_action_response_item = seller_next_action_response_item_data.to_dict()
                seller_next_action_response.append(seller_next_action_response_item)

        create_time = self.create_time

        return_line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.return_line_items, Unset):
            return_line_items = []
            for return_line_items_item_data in self.return_line_items:
                return_line_items_item = return_line_items_item_data.to_dict()
                return_line_items.append(return_line_items_item)

        discount_amount: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.discount_amount, Unset):
            discount_amount = []
            for discount_amount_item_data in self.discount_amount:
                discount_amount_item = discount_amount_item_data.to_dict()
                discount_amount.append(discount_amount_item)

        shipping_fee_amount: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shipping_fee_amount, Unset):
            shipping_fee_amount = []
            for shipping_fee_amount_item_data in self.shipping_fee_amount:
                shipping_fee_amount_item = shipping_fee_amount_item_data.to_dict()
                shipping_fee_amount.append(shipping_fee_amount_item)

        refund_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refund_amount, Unset):
            refund_amount = self.refund_amount.to_dict()

        return_shipping_document_type = self.return_shipping_document_type

        return_method = self.return_method

        is_combined_return = self.is_combined_return

        combined_return_id = self.combined_return_id

        seller_proposed_return_type = self.seller_proposed_return_type

        partial_refund: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partial_refund, Unset):
            partial_refund = self.partial_refund.to_dict()

        buyer_rejected_partial_refund = self.buyer_rejected_partial_refund

        return_warehouse_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.return_warehouse_address, Unset):
            return_warehouse_address = self.return_warehouse_address.to_dict()

        is_quick_refund = self.is_quick_refund

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if return_id is not UNSET:
            field_dict["return_id"] = return_id
        if return_type is not UNSET:
            field_dict["return_type"] = return_type
        if return_status is not UNSET:
            field_dict["return_status"] = return_status
        if arbitration_status is not UNSET:
            field_dict["arbitration_status"] = arbitration_status
        if role is not UNSET:
            field_dict["role"] = role
        if return_reason is not UNSET:
            field_dict["return_reason"] = return_reason
        if return_reason_text is not UNSET:
            field_dict["return_reason_text"] = return_reason_text
        if shipment_type is not UNSET:
            field_dict["shipment_type"] = shipment_type
        if handover_method is not UNSET:
            field_dict["handover_method"] = handover_method
        if return_tracking_number is not UNSET:
            field_dict["return_tracking_number"] = return_tracking_number
        if return_provider_name is not UNSET:
            field_dict["return_provider_name"] = return_provider_name
        if return_provider_id is not UNSET:
            field_dict["return_provider_id"] = return_provider_id
        if pre_return_id is not UNSET:
            field_dict["pre_return_id"] = pre_return_id
        if next_return_id is not UNSET:
            field_dict["next_return_id"] = next_return_id
        if can_buyer_keep_item is not UNSET:
            field_dict["can_buyer_keep_item"] = can_buyer_keep_item
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if seller_next_action_response is not UNSET:
            field_dict["seller_next_action_response"] = seller_next_action_response
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if return_line_items is not UNSET:
            field_dict["return_line_items"] = return_line_items
        if discount_amount is not UNSET:
            field_dict["discount_amount"] = discount_amount
        if shipping_fee_amount is not UNSET:
            field_dict["shipping_fee_amount"] = shipping_fee_amount
        if refund_amount is not UNSET:
            field_dict["refund_amount"] = refund_amount
        if return_shipping_document_type is not UNSET:
            field_dict["return_shipping_document_type"] = return_shipping_document_type
        if return_method is not UNSET:
            field_dict["return_method"] = return_method
        if is_combined_return is not UNSET:
            field_dict["is_combined_return"] = is_combined_return
        if combined_return_id is not UNSET:
            field_dict["combined_return_id"] = combined_return_id
        if seller_proposed_return_type is not UNSET:
            field_dict["seller_proposed_return_type"] = seller_proposed_return_type
        if partial_refund is not UNSET:
            field_dict["partial_refund"] = partial_refund
        if buyer_rejected_partial_refund is not UNSET:
            field_dict["buyer_rejected_partial_refund"] = buyer_rejected_partial_refund
        if return_warehouse_address is not UNSET:
            field_dict["return_warehouse_address"] = return_warehouse_address
        if is_quick_refund is not UNSET:
            field_dict["is_quick_refund"] = is_quick_refund

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partial_refund import PartialRefund  # noqa: PLC0415
        from ..models.refund_amount import RefundAmount  # noqa: PLC0415
        from ..models.return_warehouse_address import ReturnWarehouseAddress  # noqa: PLC0415
        from ..models.search_returns_response_data_return_order_discount_amount import (
            SearchReturnsResponseDataReturnOrderDiscountAmount,  # noqa: PLC0415
        )
        from ..models.search_returns_response_data_return_order_return_line_item import (
            SearchReturnsResponseDataReturnOrderReturnLineItem,  # noqa: PLC0415
        )
        from ..models.search_returns_response_data_return_order_shipping_fee_amount import (
            SearchReturnsResponseDataReturnOrderShippingFeeAmount,  # noqa: PLC0415
        )
        from ..models.seller_next_action_response import SellerNextActionResponse  # noqa: PLC0415

        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        return_id = d.pop("return_id", UNSET)

        return_type = d.pop("return_type", UNSET)

        return_status = d.pop("return_status", UNSET)

        arbitration_status = d.pop("arbitration_status", UNSET)

        role = d.pop("role", UNSET)

        return_reason = d.pop("return_reason", UNSET)

        return_reason_text = d.pop("return_reason_text", UNSET)

        shipment_type = d.pop("shipment_type", UNSET)

        handover_method = d.pop("handover_method", UNSET)

        return_tracking_number = d.pop("return_tracking_number", UNSET)

        return_provider_name = d.pop("return_provider_name", UNSET)

        return_provider_id = d.pop("return_provider_id", UNSET)

        pre_return_id = d.pop("pre_return_id", UNSET)

        next_return_id = d.pop("next_return_id", UNSET)

        can_buyer_keep_item = d.pop("can_buyer_keep_item", UNSET)

        update_time = d.pop("update_time", UNSET)

        _seller_next_action_response = d.pop("seller_next_action_response", UNSET)
        seller_next_action_response: list[SellerNextActionResponse] | Unset = UNSET
        if _seller_next_action_response is not UNSET:
            seller_next_action_response = []
            for seller_next_action_response_item_data in _seller_next_action_response:
                seller_next_action_response_item = SellerNextActionResponse.from_dict(
                    seller_next_action_response_item_data
                )

                seller_next_action_response.append(seller_next_action_response_item)

        create_time = d.pop("create_time", UNSET)

        _return_line_items = d.pop("return_line_items", UNSET)
        return_line_items: list[SearchReturnsResponseDataReturnOrderReturnLineItem] | Unset = UNSET
        if _return_line_items is not UNSET:
            return_line_items = []
            for return_line_items_item_data in _return_line_items:
                return_line_items_item = SearchReturnsResponseDataReturnOrderReturnLineItem.from_dict(
                    return_line_items_item_data
                )

                return_line_items.append(return_line_items_item)

        _discount_amount = d.pop("discount_amount", UNSET)
        discount_amount: list[SearchReturnsResponseDataReturnOrderDiscountAmount] | Unset = UNSET
        if _discount_amount is not UNSET:
            discount_amount = []
            for discount_amount_item_data in _discount_amount:
                discount_amount_item = SearchReturnsResponseDataReturnOrderDiscountAmount.from_dict(
                    discount_amount_item_data
                )

                discount_amount.append(discount_amount_item)

        _shipping_fee_amount = d.pop("shipping_fee_amount", UNSET)
        shipping_fee_amount: list[SearchReturnsResponseDataReturnOrderShippingFeeAmount] | Unset = UNSET
        if _shipping_fee_amount is not UNSET:
            shipping_fee_amount = []
            for shipping_fee_amount_item_data in _shipping_fee_amount:
                shipping_fee_amount_item = SearchReturnsResponseDataReturnOrderShippingFeeAmount.from_dict(
                    shipping_fee_amount_item_data
                )

                shipping_fee_amount.append(shipping_fee_amount_item)

        _refund_amount = d.pop("refund_amount", UNSET)
        refund_amount: RefundAmount | Unset
        if isinstance(_refund_amount, Unset):
            refund_amount = UNSET
        else:
            refund_amount = RefundAmount.from_dict(_refund_amount)

        return_shipping_document_type = d.pop("return_shipping_document_type", UNSET)

        return_method = d.pop("return_method", UNSET)

        is_combined_return = d.pop("is_combined_return", UNSET)

        combined_return_id = d.pop("combined_return_id", UNSET)

        seller_proposed_return_type = d.pop("seller_proposed_return_type", UNSET)

        _partial_refund = d.pop("partial_refund", UNSET)
        partial_refund: PartialRefund | Unset
        if isinstance(_partial_refund, Unset):
            partial_refund = UNSET
        else:
            partial_refund = PartialRefund.from_dict(_partial_refund)

        buyer_rejected_partial_refund = d.pop("buyer_rejected_partial_refund", UNSET)

        _return_warehouse_address = d.pop("return_warehouse_address", UNSET)
        return_warehouse_address: ReturnWarehouseAddress | Unset
        if isinstance(_return_warehouse_address, Unset):
            return_warehouse_address = UNSET
        else:
            return_warehouse_address = ReturnWarehouseAddress.from_dict(_return_warehouse_address)

        is_quick_refund = d.pop("is_quick_refund", UNSET)

        search_returns_response_data_return_order = cls(
            order_id=order_id,
            return_id=return_id,
            return_type=return_type,
            return_status=return_status,
            arbitration_status=arbitration_status,
            role=role,
            return_reason=return_reason,
            return_reason_text=return_reason_text,
            shipment_type=shipment_type,
            handover_method=handover_method,
            return_tracking_number=return_tracking_number,
            return_provider_name=return_provider_name,
            return_provider_id=return_provider_id,
            pre_return_id=pre_return_id,
            next_return_id=next_return_id,
            can_buyer_keep_item=can_buyer_keep_item,
            update_time=update_time,
            seller_next_action_response=seller_next_action_response,
            create_time=create_time,
            return_line_items=return_line_items,
            discount_amount=discount_amount,
            shipping_fee_amount=shipping_fee_amount,
            refund_amount=refund_amount,
            return_shipping_document_type=return_shipping_document_type,
            return_method=return_method,
            is_combined_return=is_combined_return,
            combined_return_id=combined_return_id,
            seller_proposed_return_type=seller_proposed_return_type,
            partial_refund=partial_refund,
            buyer_rejected_partial_refund=buyer_rejected_partial_refund,
            return_warehouse_address=return_warehouse_address,
            is_quick_refund=is_quick_refund,
        )

        search_returns_response_data_return_order.additional_properties = d
        return search_returns_response_data_return_order

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
