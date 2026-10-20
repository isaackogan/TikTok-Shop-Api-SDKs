from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.exchange_order_line import ExchangeOrderLine
  from ..models.partial_refund_amount import PartialRefundAmount
  from ..models.refund_amount import RefundAmount
  from ..models.return_line_item import ReturnLineItem
  from ..models.return_sub_line_item import ReturnSubLineItem
  from ..models.return_warehouse_address import ReturnWarehouseAddress
  from ..models.search_aftersales_requests_response_data_aftersales_request_sku_return_request_discount import SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestDiscount
  from ..models.search_aftersales_requests_response_data_aftersales_request_sku_return_request_shipping_fee import SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestShippingFee
  from ..models.seller_next_action_response import SellerNextActionResponse





T = TypeVar("T", bound="SkuReturnRequest")



@_attrs_define
class SkuReturnRequest:
    """ 
        Attributes:
            order_id (str | Unset): TikTok Shop main order ID associated with this SKU return request.
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
                - `SYSTEM`: TikTok Shop system.
                Please see "API overview" to learn more about roles.
            return_reason (str | Unset): Machine-readable reason code for the return. Use `return_reason_text` for localized
                display text.
            return_reason_text (str | Unset): Reason for return, in localized text.
                You can change language using the locale request parameter.
            seller_next_action_response (list[SellerNextActionResponse] | Unset): Seller's next action and deadline.
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
            refund_amount (RefundAmount | Unset):
            return_line_items (list[ReturnLineItem] | Unset): Return order lines items.
            create_time (int | Unset): The time when the return was created, as a Unix timestamp in seconds.
            update_time (int | Unset): The time when the return was last updated, as a Unix timestamp in seconds.
            discount (SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestDiscount | Unset):
            shipping_fee (SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestShippingFee | Unset):
            buyer_keep_item (bool | Unset): Indicates whether the buyer may keep the item(s). This field is returned as
                `true` for replacement requests and is omitted for other return types.
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
            partial_refund_amount (PartialRefundAmount | Unset):
            buyer_rejected_partial_refund (bool | Unset): Only return this field when seller initiated the partial refund.
                Available values:
                - `TRUE`: Buyer reject the seller partial refund offer.
                - `FALSE`: Buyer accept the seller partial refund offer or awaiting buyer response.
            return_warehouse_address (ReturnWarehouseAddress | Unset):
            exchange_order_lines (list[ExchangeOrderLine] | Unset): Ignore this field. It is not yet supported.
            reshipment_order_id (str | Unset): Ignore this field. It is not yet supported.
            is_quick_refund (bool | Unset): If the return hit the quick refund strategy, the seller cannot reject the
                received package
            return_sub_line_items (list[ReturnSubLineItem] | Unset): Deprecated. Do not use this field.
     """

    order_id: str | Unset = UNSET
    return_id: str | Unset = UNSET
    return_type: str | Unset = UNSET
    return_status: str | Unset = UNSET
    arbitration_status: str | Unset = UNSET
    role: str | Unset = UNSET
    return_reason: str | Unset = UNSET
    return_reason_text: str | Unset = UNSET
    seller_next_action_response: list[SellerNextActionResponse] | Unset = UNSET
    shipment_type: str | Unset = UNSET
    handover_method: str | Unset = UNSET
    return_tracking_number: str | Unset = UNSET
    return_provider_name: str | Unset = UNSET
    return_provider_id: str | Unset = UNSET
    pre_return_id: str | Unset = UNSET
    next_return_id: str | Unset = UNSET
    refund_amount: RefundAmount | Unset = UNSET
    return_line_items: list[ReturnLineItem] | Unset = UNSET
    create_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    discount: SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestDiscount | Unset = UNSET
    shipping_fee: SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestShippingFee | Unset = UNSET
    buyer_keep_item: bool | Unset = UNSET
    return_shipping_document_type: str | Unset = UNSET
    return_method: str | Unset = UNSET
    is_combined_return: bool | Unset = UNSET
    combined_return_id: str | Unset = UNSET
    seller_proposed_return_type: str | Unset = UNSET
    partial_refund_amount: PartialRefundAmount | Unset = UNSET
    buyer_rejected_partial_refund: bool | Unset = UNSET
    return_warehouse_address: ReturnWarehouseAddress | Unset = UNSET
    exchange_order_lines: list[ExchangeOrderLine] | Unset = UNSET
    reshipment_order_id: str | Unset = UNSET
    is_quick_refund: bool | Unset = UNSET
    return_sub_line_items: list[ReturnSubLineItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.exchange_order_line import ExchangeOrderLine # noqa: PLC0415
        from ..models.partial_refund_amount import PartialRefundAmount # noqa: PLC0415
        from ..models.refund_amount import RefundAmount # noqa: PLC0415
        from ..models.return_line_item import ReturnLineItem # noqa: PLC0415
        from ..models.return_sub_line_item import ReturnSubLineItem # noqa: PLC0415
        from ..models.return_warehouse_address import ReturnWarehouseAddress # noqa: PLC0415
        from ..models.search_aftersales_requests_response_data_aftersales_request_sku_return_request_discount import SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestDiscount # noqa: PLC0415
        from ..models.search_aftersales_requests_response_data_aftersales_request_sku_return_request_shipping_fee import SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestShippingFee # noqa: PLC0415
        from ..models.seller_next_action_response import SellerNextActionResponse # noqa: PLC0415
        order_id = self.order_id

        return_id = self.return_id

        return_type = self.return_type

        return_status = self.return_status

        arbitration_status = self.arbitration_status

        role = self.role

        return_reason = self.return_reason

        return_reason_text = self.return_reason_text

        seller_next_action_response: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.seller_next_action_response, Unset):
            seller_next_action_response = []
            for seller_next_action_response_item_data in self.seller_next_action_response:
                seller_next_action_response_item = seller_next_action_response_item_data.to_dict()
                seller_next_action_response.append(seller_next_action_response_item)



        shipment_type = self.shipment_type

        handover_method = self.handover_method

        return_tracking_number = self.return_tracking_number

        return_provider_name = self.return_provider_name

        return_provider_id = self.return_provider_id

        pre_return_id = self.pre_return_id

        next_return_id = self.next_return_id

        refund_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refund_amount, Unset):
            refund_amount = self.refund_amount.to_dict()

        return_line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.return_line_items, Unset):
            return_line_items = []
            for return_line_items_item_data in self.return_line_items:
                return_line_items_item = return_line_items_item_data.to_dict()
                return_line_items.append(return_line_items_item)



        create_time = self.create_time

        update_time = self.update_time

        discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        shipping_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping_fee, Unset):
            shipping_fee = self.shipping_fee.to_dict()

        buyer_keep_item = self.buyer_keep_item

        return_shipping_document_type = self.return_shipping_document_type

        return_method = self.return_method

        is_combined_return = self.is_combined_return

        combined_return_id = self.combined_return_id

        seller_proposed_return_type = self.seller_proposed_return_type

        partial_refund_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partial_refund_amount, Unset):
            partial_refund_amount = self.partial_refund_amount.to_dict()

        buyer_rejected_partial_refund = self.buyer_rejected_partial_refund

        return_warehouse_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.return_warehouse_address, Unset):
            return_warehouse_address = self.return_warehouse_address.to_dict()

        exchange_order_lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exchange_order_lines, Unset):
            exchange_order_lines = []
            for exchange_order_lines_item_data in self.exchange_order_lines:
                exchange_order_lines_item = exchange_order_lines_item_data.to_dict()
                exchange_order_lines.append(exchange_order_lines_item)



        reshipment_order_id = self.reshipment_order_id

        is_quick_refund = self.is_quick_refund

        return_sub_line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.return_sub_line_items, Unset):
            return_sub_line_items = []
            for return_sub_line_items_item_data in self.return_sub_line_items:
                return_sub_line_items_item = return_sub_line_items_item_data.to_dict()
                return_sub_line_items.append(return_sub_line_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        if seller_next_action_response is not UNSET:
            field_dict["seller_next_action_response"] = seller_next_action_response
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
        if refund_amount is not UNSET:
            field_dict["refund_amount"] = refund_amount
        if return_line_items is not UNSET:
            field_dict["return_line_items"] = return_line_items
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if discount is not UNSET:
            field_dict["discount"] = discount
        if shipping_fee is not UNSET:
            field_dict["shipping_fee"] = shipping_fee
        if buyer_keep_item is not UNSET:
            field_dict["buyer_keep_item"] = buyer_keep_item
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
        if partial_refund_amount is not UNSET:
            field_dict["partial_refund_amount"] = partial_refund_amount
        if buyer_rejected_partial_refund is not UNSET:
            field_dict["buyer_rejected_partial_refund"] = buyer_rejected_partial_refund
        if return_warehouse_address is not UNSET:
            field_dict["return_warehouse_address"] = return_warehouse_address
        if exchange_order_lines is not UNSET:
            field_dict["exchange_order_lines"] = exchange_order_lines
        if reshipment_order_id is not UNSET:
            field_dict["reshipment_order_id"] = reshipment_order_id
        if is_quick_refund is not UNSET:
            field_dict["is_quick_refund"] = is_quick_refund
        if return_sub_line_items is not UNSET:
            field_dict["return_sub_line_items"] = return_sub_line_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exchange_order_line import ExchangeOrderLine # noqa: PLC0415
        from ..models.partial_refund_amount import PartialRefundAmount # noqa: PLC0415
        from ..models.refund_amount import RefundAmount # noqa: PLC0415
        from ..models.return_line_item import ReturnLineItem # noqa: PLC0415
        from ..models.return_sub_line_item import ReturnSubLineItem # noqa: PLC0415
        from ..models.return_warehouse_address import ReturnWarehouseAddress # noqa: PLC0415
        from ..models.search_aftersales_requests_response_data_aftersales_request_sku_return_request_discount import SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestDiscount # noqa: PLC0415
        from ..models.search_aftersales_requests_response_data_aftersales_request_sku_return_request_shipping_fee import SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestShippingFee # noqa: PLC0415
        from ..models.seller_next_action_response import SellerNextActionResponse # noqa: PLC0415
        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        return_id = d.pop("return_id", UNSET)

        return_type = d.pop("return_type", UNSET)

        return_status = d.pop("return_status", UNSET)

        arbitration_status = d.pop("arbitration_status", UNSET)

        role = d.pop("role", UNSET)

        return_reason = d.pop("return_reason", UNSET)

        return_reason_text = d.pop("return_reason_text", UNSET)

        _seller_next_action_response = d.pop("seller_next_action_response", UNSET)
        seller_next_action_response: list[SellerNextActionResponse] | Unset = UNSET
        if _seller_next_action_response is not UNSET:
            seller_next_action_response = []
            for seller_next_action_response_item_data in _seller_next_action_response:
                seller_next_action_response_item = SellerNextActionResponse.from_dict(seller_next_action_response_item_data)



                seller_next_action_response.append(seller_next_action_response_item)


        shipment_type = d.pop("shipment_type", UNSET)

        handover_method = d.pop("handover_method", UNSET)

        return_tracking_number = d.pop("return_tracking_number", UNSET)

        return_provider_name = d.pop("return_provider_name", UNSET)

        return_provider_id = d.pop("return_provider_id", UNSET)

        pre_return_id = d.pop("pre_return_id", UNSET)

        next_return_id = d.pop("next_return_id", UNSET)

        _refund_amount = d.pop("refund_amount", UNSET)
        refund_amount: RefundAmount | Unset
        if isinstance(_refund_amount,  Unset):
            refund_amount = UNSET
        else:
            refund_amount = RefundAmount.from_dict(_refund_amount)




        _return_line_items = d.pop("return_line_items", UNSET)
        return_line_items: list[ReturnLineItem] | Unset = UNSET
        if _return_line_items is not UNSET:
            return_line_items = []
            for return_line_items_item_data in _return_line_items:
                return_line_items_item = ReturnLineItem.from_dict(return_line_items_item_data)



                return_line_items.append(return_line_items_item)


        create_time = d.pop("create_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        _discount = d.pop("discount", UNSET)
        discount: SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestDiscount | Unset
        if isinstance(_discount,  Unset):
            discount = UNSET
        else:
            discount = SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestDiscount.from_dict(_discount)




        _shipping_fee = d.pop("shipping_fee", UNSET)
        shipping_fee: SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestShippingFee | Unset
        if isinstance(_shipping_fee,  Unset):
            shipping_fee = UNSET
        else:
            shipping_fee = SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestShippingFee.from_dict(_shipping_fee)




        buyer_keep_item = d.pop("buyer_keep_item", UNSET)

        return_shipping_document_type = d.pop("return_shipping_document_type", UNSET)

        return_method = d.pop("return_method", UNSET)

        is_combined_return = d.pop("is_combined_return", UNSET)

        combined_return_id = d.pop("combined_return_id", UNSET)

        seller_proposed_return_type = d.pop("seller_proposed_return_type", UNSET)

        _partial_refund_amount = d.pop("partial_refund_amount", UNSET)
        partial_refund_amount: PartialRefundAmount | Unset
        if isinstance(_partial_refund_amount,  Unset):
            partial_refund_amount = UNSET
        else:
            partial_refund_amount = PartialRefundAmount.from_dict(_partial_refund_amount)




        buyer_rejected_partial_refund = d.pop("buyer_rejected_partial_refund", UNSET)

        _return_warehouse_address = d.pop("return_warehouse_address", UNSET)
        return_warehouse_address: ReturnWarehouseAddress | Unset
        if isinstance(_return_warehouse_address,  Unset):
            return_warehouse_address = UNSET
        else:
            return_warehouse_address = ReturnWarehouseAddress.from_dict(_return_warehouse_address)




        _exchange_order_lines = d.pop("exchange_order_lines", UNSET)
        exchange_order_lines: list[ExchangeOrderLine] | Unset = UNSET
        if _exchange_order_lines is not UNSET:
            exchange_order_lines = []
            for exchange_order_lines_item_data in _exchange_order_lines:
                exchange_order_lines_item = ExchangeOrderLine.from_dict(exchange_order_lines_item_data)



                exchange_order_lines.append(exchange_order_lines_item)


        reshipment_order_id = d.pop("reshipment_order_id", UNSET)

        is_quick_refund = d.pop("is_quick_refund", UNSET)

        _return_sub_line_items = d.pop("return_sub_line_items", UNSET)
        return_sub_line_items: list[ReturnSubLineItem] | Unset = UNSET
        if _return_sub_line_items is not UNSET:
            return_sub_line_items = []
            for return_sub_line_items_item_data in _return_sub_line_items:
                return_sub_line_items_item = ReturnSubLineItem.from_dict(return_sub_line_items_item_data)



                return_sub_line_items.append(return_sub_line_items_item)


        sku_return_request = cls(
            order_id=order_id,
            return_id=return_id,
            return_type=return_type,
            return_status=return_status,
            arbitration_status=arbitration_status,
            role=role,
            return_reason=return_reason,
            return_reason_text=return_reason_text,
            seller_next_action_response=seller_next_action_response,
            shipment_type=shipment_type,
            handover_method=handover_method,
            return_tracking_number=return_tracking_number,
            return_provider_name=return_provider_name,
            return_provider_id=return_provider_id,
            pre_return_id=pre_return_id,
            next_return_id=next_return_id,
            refund_amount=refund_amount,
            return_line_items=return_line_items,
            create_time=create_time,
            update_time=update_time,
            discount=discount,
            shipping_fee=shipping_fee,
            buyer_keep_item=buyer_keep_item,
            return_shipping_document_type=return_shipping_document_type,
            return_method=return_method,
            is_combined_return=is_combined_return,
            combined_return_id=combined_return_id,
            seller_proposed_return_type=seller_proposed_return_type,
            partial_refund_amount=partial_refund_amount,
            buyer_rejected_partial_refund=buyer_rejected_partial_refund,
            return_warehouse_address=return_warehouse_address,
            exchange_order_lines=exchange_order_lines,
            reshipment_order_id=reshipment_order_id,
            is_quick_refund=is_quick_refund,
            return_sub_line_items=return_sub_line_items,
        )


        sku_return_request.additional_properties = d
        return sku_return_request

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
