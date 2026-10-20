from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_list_response_data_order_line_item import GetOrderListResponseDataOrderLineItem
    from ..models.get_order_list_response_data_order_package import GetOrderListResponseDataOrderPackage
    from ..models.get_order_list_response_data_order_recipient_address import (
        GetOrderListResponseDataOrderRecipientAddress,
    )
    from ..models.handling_duration import HandlingDuration
    from ..models.payment import Payment


T = TypeVar("T", bound="GetOrderListResponseDataOrder")


@_attrs_define
class GetOrderListResponseDataOrder:
    """
    Attributes:
        id (str | Unset): TikTok Shop order ID.
        buyer_message (str | Unset): The note from the buyer.
        cancellation_initiator (str | Unset): Cancellation request initiator.
            Available values:
            - `SELLER`
            - `BUYER`
            - `SYSTEM`
        shipping_provider_id (str | Unset): The ID of the current shipping provider.
        create_time (int | Unset): The date and time that the order was created. Unix timestamp.
        shipping_provider (str | Unset): The name of the current shipping provider.
        packages (list[GetOrderListResponseDataOrderPackage] | Unset): List of packages included in this order.
        payment (Payment | Unset):
        recipient_address (GetOrderListResponseDataOrderRecipientAddress | Unset):
        status (str | Unset): Specific order status.
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
        fulfillment_type (str | Unset): Fulfillment type. Only orders with fulfillment type can be shipped by sellers.
            Available values:
            - `FULFILLMENT_BY_SELLER`: a method where sellers fulfill orders directly from their own inventory, without
            using TikTok's fulfillment centers. In this model, the seller is responsible for storing, packaging, and
            shipping the products to customers.
            - `FULFILLMENT_BY_TIKTOK`: a service offered by TikTok where sellers can send their products to TikTok's
            fulfillment centers. TikTok then takes care of storing, picking, packing, and shipping the products to
            customers.
            - `FULFILLMENT_BY_DILAYANI_TOKOPEDIA`: a method where Tokopedia GoTo Logistics provides warehousing and
            logistics services to sellers and charges a fee for the service.
        delivery_type (str | Unset): Indicates whether it is a Pick-Up Drop-Off (PUDO) location. The PUDO location is
            selected by the buyer when placing orders.
            Available values:
            - `HOME_DELIVERY`: not a PUDO location
            - `COLLECTION_POINT`: a PUDO location
        paid_time (int | Unset): The date and time that the order was paid. Unix timestamp.
        rts_sla_time (int | Unset): The latest shipping time specified by the platform. Unix timestamp.
        tts_sla_time (int | Unset): The latest collection time specified by the platform. Unix timestamp.
        cancel_reason (str | Unset): The cancellation reason. Please visit [our list of cancel
            reasons](https://partner.tiktokshop.com/docv2/page/67e61eee427345048595487d) for more information.
        update_time (int | Unset): Time of order status change. Unix timestamp.
        payment_method_name (str | Unset): Payment method name, for display purposes.
        rts_time (int | Unset): The time sellers shipped the order (called [Ship Package
            API](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) successfully). Unix timestamp.
        tracking_number (str | Unset): Tracking number. Available after the package has been shipped.
        split_or_combine_tag (str | Unset): Indicates whether the order is combined or split:
            - `COMBINED`
            - `SPLIT`

            This field will be used in future fulfillment APIs.
        has_updated_recipient_address (bool | Unset): Whether the recipient address has been updated or changed.
        cancel_order_sla_time (int | Unset): The automatic cancellation time for orders specified by the platform.
            Unix timestamp.
        warehouse_id (str | Unset): Seller warehouse ID.
        request_cancel_time (int | Unset): Buyer request cancellation time. Unix timestamp.
        shipping_type (str | Unset): Delivery method.
            Available values:
            - `TIKTOK`: Shipping service provided by TikTok. The seller should obtain shipping label from TikTok.
            - `SELLER`: Seller provides shipping, including through 3rd party fulfillment providers on behalf of the seller.
            - `TIKTOK_DIGITAL`: Tiktok delivers virtual goods directly to buyers. There is no action needed.
        user_id (str | Unset): Buyer user ID.
        seller_note (str | Unset): The seller note from TikTok Shop Seller Center.
        delivery_sla_time (int | Unset): Order should arrive by this date to be considered on-time and to avoid late
            delivery penalties.
        is_cod (bool | Unset): This option is for sellers that accept cash payment on delivery (COD). Buyers will pay in
            cash upon receiving the package.

            Default: FALSE

            Only applicable to countries where COD is supported.
        delivery_option_id (str | Unset): Delivery option ID is mapped to seller configured logistics templates ID.
        cancel_time (int | Unset): The time an order's status was updated to `CANCELLED`. Unix timestamp.
        need_upload_invoice (str | Unset): Whether an invoice needs to be uploaded and uploaded status (only for Brazil
            market).
            - UNKNOWN:  Currently unable to confirm whether an invoice is needed
            - NEED_INVOICE: This order requires an invoice and the invoice has not been uploaded yet
            - NO_NEED：This order does not require an invoice
            - INVOICE_UPLOADED: The invoice for this order has been uploaded and verified. If the order is split, it will be
            marked as "uploaded" once any sub-order's invoice is uploaded.
            - INVOICE_PROCESSING: The invoice for this order is currently being uploaded/cancelled. Please wait for the
            final result and do not repeat the operation
        delivery_option_name (str | Unset): Delivery option name. For display purposes only.
            Available values:
            - `Economy Shipping`
            - `Standard Shipping`
            - `Express Shipping`
        cpf (str | Unset): CPF (invoice number), used to issue an invoice.

            **Note**: Only available in the Brazil market.
        line_items (list[GetOrderListResponseDataOrderLineItem] | Unset): Line item info list.
        buyer_email (str | Unset): The anonymized email address of the buyer. It is not recommended to send messages
            directly to this email address. If you need to contact the buyer, please go to the TikTok Shop Seller Center -
            Buyer Messages page.
        delivery_due_time (int | Unset): If the order hasn't updated its status to `DELIVERED` before this time, the
            order will be automatically canceled by TikTok Shop. Unix timestamp.
        is_sample_order (bool | Unset): Use this field to determine whether the order is a sample order.
        shipping_due_time (int | Unset): If the order hasn't updated its status to `AWAITING_COLLECTION` before this
            time, the order will be automatically canceled by TikTok Shop. Unix timestamp.
        collection_due_time (int | Unset): If the order hasn't updated its status to `IN_TRANSIT` before this time, the
            order will be canceled by TikTok Shop. Unix timestamp.
        delivery_option_required_delivery_time (int | Unset): Order should be delivered before this time. Unix
            timestamp.
        is_on_hold_order (bool | Unset): Indicates whether the order has been changed to or will be updated to `ON_HOLD`
            status.
        delivery_time (int | Unset): The time an order's status changed to `DELIVERED`. Unix timestamp.
        is_replacement_order (bool | Unset): Whether this is a replacement order.
        is_subscription_order (bool | Unset): Subscription orders are recurring orders set up by customers. If TRUE,
            this order is generated from a subscription order
        is_refundable_sample (bool | Unset): This indicates if an order is a refundable sample. Refundable samples lets
            sellers collaborate with creators by refunding product costs only when creators meet sales thresholds.
        authentication_required (bool | Unset): If true, order requires authentication. Use an approved in-house
            authentication service after an order has been placed for verification. This must be completed before shipment.
        collection_time (int | Unset): The time an order's status has been updated to `IN_TRANSIT`. Unix timestamp.
        replaced_order_id (str | Unset): The order Id for the order that is being replaced.

            Returned only if `is_replacement_order = true`.
        is_buyer_request_cancel (bool | Unset): Whether the buyer has a pending cancellation request.
        pick_up_cut_off_time (int | Unset): To avoid LDR, you must ensure the package is picked up by this time. Only
            applicable in South East Asia regions.
        fast_dispatch_sla_time (int | Unset): The latest collection time to gain incentives of NDD (Next Day Delivery)
            project. Unix timestamp.

            **Note**: Only available in Thailand and the Philippines.
        commerce_platform (str | Unset): The platform where the order was placed.
            Possible values:
            - `TIKTOK_SHOP`
            - `TOKOPEDIA`

            **Note**: Available only in the Indonesia market.
        order_type (str | Unset): The order type.
            Possible values based on region:

            **All regions**
            - `NORMAL`: An item that is in stock and available for immediate purchase and fulfillment.
            - `ZERO_LOTTERY`: An order placed during a lottery event in TikTok LIVE.
            - `AUCTION`: An order placed during auction, where the price of the product is not fixed.
            **US**
            - `PRE_ORDER`: An advance order for items that are not yet available or released. Fulfillment starts on a
            specific date in the future.
            - `MADE_TO_ORDER`: An order for items that are produced only after the order is received. Fulfillment starts
            after the product is produced.
            - `BACK_ORDER`: An order for items that are out of stock but expected to be restocked. Fulfillment starts after
            the product is restocked.
            - `VIRTUAL_ORDER`: An order for items that are digital goods, requiring no physical delivery. Fulfillment is
            immediate or automated upon payment confirmation.

            Returns an empty value for standard orders or other types that don't fall into the above categories.
        release_date (int | Unset): The date on which order handling starts and the status of the order changes to
            [`AWAITING_SHIPMENT`](https://partner.tiktokshop.com/docv2/page/650b1b4bbace3e02b76d1011).

            Applicable only if the `order_type` is `PRE_ORDER`.
        handling_duration (HandlingDuration | Unset):
        auto_combine_group_id (str | Unset): An identifier assigned to orders from the same customer during a LIVE
            session to facilitate combined order shipping when "auto-combination" is activated in Seller Center.
        cpf_name (str | Unset): Name belonging to the CPF number for the Brazil market.
        is_exchange_order (bool | Unset): When TRUE, this is an exchange order.

            Note: Only available in US and UK.
        exchange_source_order_id (str | Unset): If the order is an exchange order, this field returns the original
            order's order ID, from which the exchange order was generated.

            Returned only if is_exchange_order = true.

            Note: Only available in US and UK.
        consultation_id (str | Unset): An ID to identify the corresponding ePharmacy consultation.
            Applicable only if an ePharmacy consultation was initiated. Not applicable if the prescription was provided by
            the customer through an image upload.
        fast_delivery_program (str | Unset): A badge presented on the merchandise to tell the buyer that the seller
            participates in the fast delivery program, such that the order should arrive in a promised time period.
            Possible values:
            - `3_DAY_DELIVERY`
            - `3_DAY_POTENTIAL_SHIPPING`
            - `3_DAY_POTENTIAL_TRANSIT`
            Not returned if order did not meet fast delivery
            program requirements.
            Note: Applicable only for the US market.
        fulfillment_priority_level (int | Unset): Fulfillment priority value that can be used to prioritize shipping
            (only available in SEA)
            100 = Instant
            200 = Sameday 8 Hours
            300 = Sameday
            400 = Next Day Delivery
            500 = Express
            600 = Standard
            700 = Economy
            800 = Cargo
        recommended_shipping_time (int | Unset): Recommended time to ship based on the each LSP service type (only
            available in SEA)
        buyer_nickname (str | Unset): The nickname of the TikTok buyer, which is defined by the TikTok user. The
            buyer_nickname can be used to identify the buyer when displaying the unboxing results within the TikTok Live
            Session.
        buyer_avatar (str | Unset): The avatar of the TikTok buyer, which is defined by the TikTok user. The
            buyer_avatar can be used in conjunction with the buyer_nickname when displaying the unboxing results within the
            TikTok Live Session.
        order_rights (list[int] | Unset): Order tag identifier if has certain rights within the order based on the
            program subscribed by sellers.
            1 = Shipping Fee Reimbursement Program
            2 = Horizon+ Program
            Applicable for SEA market only
        instore_pickup_sla_time (int | Unset): The latest buyer pickup time for instore pickup method specified by the
            platform. Currently applicable for SEA market. Unix timestamp.
        fast_rts_sla_time (int | Unset): Indicate fast fulfillment SLA for shipping action. Applicable for SEA market
            only. Unix timestamp
        fast_collection_sla_time (int | Unset): Indicate fast fulfillment SLA for collection action. Applicable for SEA
            market only. Unix timestamp
    """

    id: str | Unset = UNSET
    buyer_message: str | Unset = UNSET
    cancellation_initiator: str | Unset = UNSET
    shipping_provider_id: str | Unset = UNSET
    create_time: int | Unset = UNSET
    shipping_provider: str | Unset = UNSET
    packages: list[GetOrderListResponseDataOrderPackage] | Unset = UNSET
    payment: Payment | Unset = UNSET
    recipient_address: GetOrderListResponseDataOrderRecipientAddress | Unset = UNSET
    status: str | Unset = UNSET
    fulfillment_type: str | Unset = UNSET
    delivery_type: str | Unset = UNSET
    paid_time: int | Unset = UNSET
    rts_sla_time: int | Unset = UNSET
    tts_sla_time: int | Unset = UNSET
    cancel_reason: str | Unset = UNSET
    update_time: int | Unset = UNSET
    payment_method_name: str | Unset = UNSET
    rts_time: int | Unset = UNSET
    tracking_number: str | Unset = UNSET
    split_or_combine_tag: str | Unset = UNSET
    has_updated_recipient_address: bool | Unset = UNSET
    cancel_order_sla_time: int | Unset = UNSET
    warehouse_id: str | Unset = UNSET
    request_cancel_time: int | Unset = UNSET
    shipping_type: str | Unset = UNSET
    user_id: str | Unset = UNSET
    seller_note: str | Unset = UNSET
    delivery_sla_time: int | Unset = UNSET
    is_cod: bool | Unset = UNSET
    delivery_option_id: str | Unset = UNSET
    cancel_time: int | Unset = UNSET
    need_upload_invoice: str | Unset = UNSET
    delivery_option_name: str | Unset = UNSET
    cpf: str | Unset = UNSET
    line_items: list[GetOrderListResponseDataOrderLineItem] | Unset = UNSET
    buyer_email: str | Unset = UNSET
    delivery_due_time: int | Unset = UNSET
    is_sample_order: bool | Unset = UNSET
    shipping_due_time: int | Unset = UNSET
    collection_due_time: int | Unset = UNSET
    delivery_option_required_delivery_time: int | Unset = UNSET
    is_on_hold_order: bool | Unset = UNSET
    delivery_time: int | Unset = UNSET
    is_replacement_order: bool | Unset = UNSET
    is_subscription_order: bool | Unset = UNSET
    is_refundable_sample: bool | Unset = UNSET
    authentication_required: bool | Unset = UNSET
    collection_time: int | Unset = UNSET
    replaced_order_id: str | Unset = UNSET
    is_buyer_request_cancel: bool | Unset = UNSET
    pick_up_cut_off_time: int | Unset = UNSET
    fast_dispatch_sla_time: int | Unset = UNSET
    commerce_platform: str | Unset = UNSET
    order_type: str | Unset = UNSET
    release_date: int | Unset = UNSET
    handling_duration: HandlingDuration | Unset = UNSET
    auto_combine_group_id: str | Unset = UNSET
    cpf_name: str | Unset = UNSET
    is_exchange_order: bool | Unset = UNSET
    exchange_source_order_id: str | Unset = UNSET
    consultation_id: str | Unset = UNSET
    fast_delivery_program: str | Unset = UNSET
    fulfillment_priority_level: int | Unset = UNSET
    recommended_shipping_time: int | Unset = UNSET
    buyer_nickname: str | Unset = UNSET
    buyer_avatar: str | Unset = UNSET
    order_rights: list[int] | Unset = UNSET
    instore_pickup_sla_time: int | Unset = UNSET
    fast_rts_sla_time: int | Unset = UNSET
    fast_collection_sla_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        buyer_message = self.buyer_message

        cancellation_initiator = self.cancellation_initiator

        shipping_provider_id = self.shipping_provider_id

        create_time = self.create_time

        shipping_provider = self.shipping_provider

        packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)

        payment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payment, Unset):
            payment = self.payment.to_dict()

        recipient_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipient_address, Unset):
            recipient_address = self.recipient_address.to_dict()

        status = self.status

        fulfillment_type = self.fulfillment_type

        delivery_type = self.delivery_type

        paid_time = self.paid_time

        rts_sla_time = self.rts_sla_time

        tts_sla_time = self.tts_sla_time

        cancel_reason = self.cancel_reason

        update_time = self.update_time

        payment_method_name = self.payment_method_name

        rts_time = self.rts_time

        tracking_number = self.tracking_number

        split_or_combine_tag = self.split_or_combine_tag

        has_updated_recipient_address = self.has_updated_recipient_address

        cancel_order_sla_time = self.cancel_order_sla_time

        warehouse_id = self.warehouse_id

        request_cancel_time = self.request_cancel_time

        shipping_type = self.shipping_type

        user_id = self.user_id

        seller_note = self.seller_note

        delivery_sla_time = self.delivery_sla_time

        is_cod = self.is_cod

        delivery_option_id = self.delivery_option_id

        cancel_time = self.cancel_time

        need_upload_invoice = self.need_upload_invoice

        delivery_option_name = self.delivery_option_name

        cpf = self.cpf

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)

        buyer_email = self.buyer_email

        delivery_due_time = self.delivery_due_time

        is_sample_order = self.is_sample_order

        shipping_due_time = self.shipping_due_time

        collection_due_time = self.collection_due_time

        delivery_option_required_delivery_time = self.delivery_option_required_delivery_time

        is_on_hold_order = self.is_on_hold_order

        delivery_time = self.delivery_time

        is_replacement_order = self.is_replacement_order

        is_subscription_order = self.is_subscription_order

        is_refundable_sample = self.is_refundable_sample

        authentication_required = self.authentication_required

        collection_time = self.collection_time

        replaced_order_id = self.replaced_order_id

        is_buyer_request_cancel = self.is_buyer_request_cancel

        pick_up_cut_off_time = self.pick_up_cut_off_time

        fast_dispatch_sla_time = self.fast_dispatch_sla_time

        commerce_platform = self.commerce_platform

        order_type = self.order_type

        release_date = self.release_date

        handling_duration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.handling_duration, Unset):
            handling_duration = self.handling_duration.to_dict()

        auto_combine_group_id = self.auto_combine_group_id

        cpf_name = self.cpf_name

        is_exchange_order = self.is_exchange_order

        exchange_source_order_id = self.exchange_source_order_id

        consultation_id = self.consultation_id

        fast_delivery_program = self.fast_delivery_program

        fulfillment_priority_level = self.fulfillment_priority_level

        recommended_shipping_time = self.recommended_shipping_time

        buyer_nickname = self.buyer_nickname

        buyer_avatar = self.buyer_avatar

        order_rights: list[int] | Unset = UNSET
        if not isinstance(self.order_rights, Unset):
            order_rights = self.order_rights

        instore_pickup_sla_time = self.instore_pickup_sla_time

        fast_rts_sla_time = self.fast_rts_sla_time

        fast_collection_sla_time = self.fast_collection_sla_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if buyer_message is not UNSET:
            field_dict["buyer_message"] = buyer_message
        if cancellation_initiator is not UNSET:
            field_dict["cancellation_initiator"] = cancellation_initiator
        if shipping_provider_id is not UNSET:
            field_dict["shipping_provider_id"] = shipping_provider_id
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if shipping_provider is not UNSET:
            field_dict["shipping_provider"] = shipping_provider
        if packages is not UNSET:
            field_dict["packages"] = packages
        if payment is not UNSET:
            field_dict["payment"] = payment
        if recipient_address is not UNSET:
            field_dict["recipient_address"] = recipient_address
        if status is not UNSET:
            field_dict["status"] = status
        if fulfillment_type is not UNSET:
            field_dict["fulfillment_type"] = fulfillment_type
        if delivery_type is not UNSET:
            field_dict["delivery_type"] = delivery_type
        if paid_time is not UNSET:
            field_dict["paid_time"] = paid_time
        if rts_sla_time is not UNSET:
            field_dict["rts_sla_time"] = rts_sla_time
        if tts_sla_time is not UNSET:
            field_dict["tts_sla_time"] = tts_sla_time
        if cancel_reason is not UNSET:
            field_dict["cancel_reason"] = cancel_reason
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if payment_method_name is not UNSET:
            field_dict["payment_method_name"] = payment_method_name
        if rts_time is not UNSET:
            field_dict["rts_time"] = rts_time
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if split_or_combine_tag is not UNSET:
            field_dict["split_or_combine_tag"] = split_or_combine_tag
        if has_updated_recipient_address is not UNSET:
            field_dict["has_updated_recipient_address"] = has_updated_recipient_address
        if cancel_order_sla_time is not UNSET:
            field_dict["cancel_order_sla_time"] = cancel_order_sla_time
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id
        if request_cancel_time is not UNSET:
            field_dict["request_cancel_time"] = request_cancel_time
        if shipping_type is not UNSET:
            field_dict["shipping_type"] = shipping_type
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if seller_note is not UNSET:
            field_dict["seller_note"] = seller_note
        if delivery_sla_time is not UNSET:
            field_dict["delivery_sla_time"] = delivery_sla_time
        if is_cod is not UNSET:
            field_dict["is_cod"] = is_cod
        if delivery_option_id is not UNSET:
            field_dict["delivery_option_id"] = delivery_option_id
        if cancel_time is not UNSET:
            field_dict["cancel_time"] = cancel_time
        if need_upload_invoice is not UNSET:
            field_dict["need_upload_invoice"] = need_upload_invoice
        if delivery_option_name is not UNSET:
            field_dict["delivery_option_name"] = delivery_option_name
        if cpf is not UNSET:
            field_dict["cpf"] = cpf
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if buyer_email is not UNSET:
            field_dict["buyer_email"] = buyer_email
        if delivery_due_time is not UNSET:
            field_dict["delivery_due_time"] = delivery_due_time
        if is_sample_order is not UNSET:
            field_dict["is_sample_order"] = is_sample_order
        if shipping_due_time is not UNSET:
            field_dict["shipping_due_time"] = shipping_due_time
        if collection_due_time is not UNSET:
            field_dict["collection_due_time"] = collection_due_time
        if delivery_option_required_delivery_time is not UNSET:
            field_dict["delivery_option_required_delivery_time"] = delivery_option_required_delivery_time
        if is_on_hold_order is not UNSET:
            field_dict["is_on_hold_order"] = is_on_hold_order
        if delivery_time is not UNSET:
            field_dict["delivery_time"] = delivery_time
        if is_replacement_order is not UNSET:
            field_dict["is_replacement_order"] = is_replacement_order
        if is_subscription_order is not UNSET:
            field_dict["is_subscription_order"] = is_subscription_order
        if is_refundable_sample is not UNSET:
            field_dict["is_refundable_sample"] = is_refundable_sample
        if authentication_required is not UNSET:
            field_dict["authentication_required"] = authentication_required
        if collection_time is not UNSET:
            field_dict["collection_time"] = collection_time
        if replaced_order_id is not UNSET:
            field_dict["replaced_order_id"] = replaced_order_id
        if is_buyer_request_cancel is not UNSET:
            field_dict["is_buyer_request_cancel"] = is_buyer_request_cancel
        if pick_up_cut_off_time is not UNSET:
            field_dict["pick_up_cut_off_time"] = pick_up_cut_off_time
        if fast_dispatch_sla_time is not UNSET:
            field_dict["fast_dispatch_sla_time"] = fast_dispatch_sla_time
        if commerce_platform is not UNSET:
            field_dict["commerce_platform"] = commerce_platform
        if order_type is not UNSET:
            field_dict["order_type"] = order_type
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if handling_duration is not UNSET:
            field_dict["handling_duration"] = handling_duration
        if auto_combine_group_id is not UNSET:
            field_dict["auto_combine_group_id"] = auto_combine_group_id
        if cpf_name is not UNSET:
            field_dict["cpf_name"] = cpf_name
        if is_exchange_order is not UNSET:
            field_dict["is_exchange_order"] = is_exchange_order
        if exchange_source_order_id is not UNSET:
            field_dict["exchange_source_order_id"] = exchange_source_order_id
        if consultation_id is not UNSET:
            field_dict["consultation_id"] = consultation_id
        if fast_delivery_program is not UNSET:
            field_dict["fast_delivery_program"] = fast_delivery_program
        if fulfillment_priority_level is not UNSET:
            field_dict["fulfillment_priority_level"] = fulfillment_priority_level
        if recommended_shipping_time is not UNSET:
            field_dict["recommended_shipping_time"] = recommended_shipping_time
        if buyer_nickname is not UNSET:
            field_dict["buyer_nickname"] = buyer_nickname
        if buyer_avatar is not UNSET:
            field_dict["buyer_avatar"] = buyer_avatar
        if order_rights is not UNSET:
            field_dict["order_rights"] = order_rights
        if instore_pickup_sla_time is not UNSET:
            field_dict["instore_pickup_sla_time"] = instore_pickup_sla_time
        if fast_rts_sla_time is not UNSET:
            field_dict["fast_rts_sla_time"] = fast_rts_sla_time
        if fast_collection_sla_time is not UNSET:
            field_dict["fast_collection_sla_time"] = fast_collection_sla_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_list_response_data_order_line_item import (
            GetOrderListResponseDataOrderLineItem,  # noqa: PLC0415
        )
        from ..models.get_order_list_response_data_order_package import (
            GetOrderListResponseDataOrderPackage,  # noqa: PLC0415
        )
        from ..models.get_order_list_response_data_order_recipient_address import (
            GetOrderListResponseDataOrderRecipientAddress,  # noqa: PLC0415
        )
        from ..models.handling_duration import HandlingDuration  # noqa: PLC0415
        from ..models.payment import Payment  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        buyer_message = d.pop("buyer_message", UNSET)

        cancellation_initiator = d.pop("cancellation_initiator", UNSET)

        shipping_provider_id = d.pop("shipping_provider_id", UNSET)

        create_time = d.pop("create_time", UNSET)

        shipping_provider = d.pop("shipping_provider", UNSET)

        _packages = d.pop("packages", UNSET)
        packages: list[GetOrderListResponseDataOrderPackage] | Unset = UNSET
        if _packages is not UNSET:
            packages = []
            for packages_item_data in _packages:
                packages_item = GetOrderListResponseDataOrderPackage.from_dict(packages_item_data)

                packages.append(packages_item)

        _payment = d.pop("payment", UNSET)
        payment: Payment | Unset
        if isinstance(_payment, Unset):
            payment = UNSET
        else:
            payment = Payment.from_dict(_payment)

        _recipient_address = d.pop("recipient_address", UNSET)
        recipient_address: GetOrderListResponseDataOrderRecipientAddress | Unset
        if isinstance(_recipient_address, Unset):
            recipient_address = UNSET
        else:
            recipient_address = GetOrderListResponseDataOrderRecipientAddress.from_dict(_recipient_address)

        status = d.pop("status", UNSET)

        fulfillment_type = d.pop("fulfillment_type", UNSET)

        delivery_type = d.pop("delivery_type", UNSET)

        paid_time = d.pop("paid_time", UNSET)

        rts_sla_time = d.pop("rts_sla_time", UNSET)

        tts_sla_time = d.pop("tts_sla_time", UNSET)

        cancel_reason = d.pop("cancel_reason", UNSET)

        update_time = d.pop("update_time", UNSET)

        payment_method_name = d.pop("payment_method_name", UNSET)

        rts_time = d.pop("rts_time", UNSET)

        tracking_number = d.pop("tracking_number", UNSET)

        split_or_combine_tag = d.pop("split_or_combine_tag", UNSET)

        has_updated_recipient_address = d.pop("has_updated_recipient_address", UNSET)

        cancel_order_sla_time = d.pop("cancel_order_sla_time", UNSET)

        warehouse_id = d.pop("warehouse_id", UNSET)

        request_cancel_time = d.pop("request_cancel_time", UNSET)

        shipping_type = d.pop("shipping_type", UNSET)

        user_id = d.pop("user_id", UNSET)

        seller_note = d.pop("seller_note", UNSET)

        delivery_sla_time = d.pop("delivery_sla_time", UNSET)

        is_cod = d.pop("is_cod", UNSET)

        delivery_option_id = d.pop("delivery_option_id", UNSET)

        cancel_time = d.pop("cancel_time", UNSET)

        need_upload_invoice = d.pop("need_upload_invoice", UNSET)

        delivery_option_name = d.pop("delivery_option_name", UNSET)

        cpf = d.pop("cpf", UNSET)

        _line_items = d.pop("line_items", UNSET)
        line_items: list[GetOrderListResponseDataOrderLineItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = GetOrderListResponseDataOrderLineItem.from_dict(line_items_item_data)

                line_items.append(line_items_item)

        buyer_email = d.pop("buyer_email", UNSET)

        delivery_due_time = d.pop("delivery_due_time", UNSET)

        is_sample_order = d.pop("is_sample_order", UNSET)

        shipping_due_time = d.pop("shipping_due_time", UNSET)

        collection_due_time = d.pop("collection_due_time", UNSET)

        delivery_option_required_delivery_time = d.pop("delivery_option_required_delivery_time", UNSET)

        is_on_hold_order = d.pop("is_on_hold_order", UNSET)

        delivery_time = d.pop("delivery_time", UNSET)

        is_replacement_order = d.pop("is_replacement_order", UNSET)

        is_subscription_order = d.pop("is_subscription_order", UNSET)

        is_refundable_sample = d.pop("is_refundable_sample", UNSET)

        authentication_required = d.pop("authentication_required", UNSET)

        collection_time = d.pop("collection_time", UNSET)

        replaced_order_id = d.pop("replaced_order_id", UNSET)

        is_buyer_request_cancel = d.pop("is_buyer_request_cancel", UNSET)

        pick_up_cut_off_time = d.pop("pick_up_cut_off_time", UNSET)

        fast_dispatch_sla_time = d.pop("fast_dispatch_sla_time", UNSET)

        commerce_platform = d.pop("commerce_platform", UNSET)

        order_type = d.pop("order_type", UNSET)

        release_date = d.pop("release_date", UNSET)

        _handling_duration = d.pop("handling_duration", UNSET)
        handling_duration: HandlingDuration | Unset
        if isinstance(_handling_duration, Unset):
            handling_duration = UNSET
        else:
            handling_duration = HandlingDuration.from_dict(_handling_duration)

        auto_combine_group_id = d.pop("auto_combine_group_id", UNSET)

        cpf_name = d.pop("cpf_name", UNSET)

        is_exchange_order = d.pop("is_exchange_order", UNSET)

        exchange_source_order_id = d.pop("exchange_source_order_id", UNSET)

        consultation_id = d.pop("consultation_id", UNSET)

        fast_delivery_program = d.pop("fast_delivery_program", UNSET)

        fulfillment_priority_level = d.pop("fulfillment_priority_level", UNSET)

        recommended_shipping_time = d.pop("recommended_shipping_time", UNSET)

        buyer_nickname = d.pop("buyer_nickname", UNSET)

        buyer_avatar = d.pop("buyer_avatar", UNSET)

        order_rights = cast(list[int], d.pop("order_rights", UNSET))

        instore_pickup_sla_time = d.pop("instore_pickup_sla_time", UNSET)

        fast_rts_sla_time = d.pop("fast_rts_sla_time", UNSET)

        fast_collection_sla_time = d.pop("fast_collection_sla_time", UNSET)

        get_order_list_response_data_order = cls(
            id=id,
            buyer_message=buyer_message,
            cancellation_initiator=cancellation_initiator,
            shipping_provider_id=shipping_provider_id,
            create_time=create_time,
            shipping_provider=shipping_provider,
            packages=packages,
            payment=payment,
            recipient_address=recipient_address,
            status=status,
            fulfillment_type=fulfillment_type,
            delivery_type=delivery_type,
            paid_time=paid_time,
            rts_sla_time=rts_sla_time,
            tts_sla_time=tts_sla_time,
            cancel_reason=cancel_reason,
            update_time=update_time,
            payment_method_name=payment_method_name,
            rts_time=rts_time,
            tracking_number=tracking_number,
            split_or_combine_tag=split_or_combine_tag,
            has_updated_recipient_address=has_updated_recipient_address,
            cancel_order_sla_time=cancel_order_sla_time,
            warehouse_id=warehouse_id,
            request_cancel_time=request_cancel_time,
            shipping_type=shipping_type,
            user_id=user_id,
            seller_note=seller_note,
            delivery_sla_time=delivery_sla_time,
            is_cod=is_cod,
            delivery_option_id=delivery_option_id,
            cancel_time=cancel_time,
            need_upload_invoice=need_upload_invoice,
            delivery_option_name=delivery_option_name,
            cpf=cpf,
            line_items=line_items,
            buyer_email=buyer_email,
            delivery_due_time=delivery_due_time,
            is_sample_order=is_sample_order,
            shipping_due_time=shipping_due_time,
            collection_due_time=collection_due_time,
            delivery_option_required_delivery_time=delivery_option_required_delivery_time,
            is_on_hold_order=is_on_hold_order,
            delivery_time=delivery_time,
            is_replacement_order=is_replacement_order,
            is_subscription_order=is_subscription_order,
            is_refundable_sample=is_refundable_sample,
            authentication_required=authentication_required,
            collection_time=collection_time,
            replaced_order_id=replaced_order_id,
            is_buyer_request_cancel=is_buyer_request_cancel,
            pick_up_cut_off_time=pick_up_cut_off_time,
            fast_dispatch_sla_time=fast_dispatch_sla_time,
            commerce_platform=commerce_platform,
            order_type=order_type,
            release_date=release_date,
            handling_duration=handling_duration,
            auto_combine_group_id=auto_combine_group_id,
            cpf_name=cpf_name,
            is_exchange_order=is_exchange_order,
            exchange_source_order_id=exchange_source_order_id,
            consultation_id=consultation_id,
            fast_delivery_program=fast_delivery_program,
            fulfillment_priority_level=fulfillment_priority_level,
            recommended_shipping_time=recommended_shipping_time,
            buyer_nickname=buyer_nickname,
            buyer_avatar=buyer_avatar,
            order_rights=order_rights,
            instore_pickup_sla_time=instore_pickup_sla_time,
            fast_rts_sla_time=fast_rts_sla_time,
            fast_collection_sla_time=fast_collection_sla_time,
        )

        get_order_list_response_data_order.additional_properties = d
        return get_order_list_response_data_order

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
