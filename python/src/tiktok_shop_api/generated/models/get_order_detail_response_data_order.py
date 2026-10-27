from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_order_detail_response_data_order_line_item import GetOrderDetailResponseDataOrderLineItem
  from ..models.get_order_detail_response_data_order_package import GetOrderDetailResponseDataOrderPackage
  from ..models.get_order_detail_response_data_order_recipient_address import GetOrderDetailResponseDataOrderRecipientAddress
  from ..models.handling_duration import HandlingDuration
  from ..models.payment import Payment





T = TypeVar("T", bound="GetOrderDetailResponseDataOrder")



@_attrs_define
class GetOrderDetailResponseDataOrder:
    """ 
        Attributes:
            id (str | Unset): A unique identifier for a TikTok Shop order.
            cancellation_initiator (str | Unset): The initiator of a cancellation request.
                Possible values:
                - `SELLER`
                - `BUYER`
                - `SYSTEM`
            shipping_provider (str | Unset): The name of the current shipping provider.
            shipping_provider_id (str | Unset): The ID of the current shipping provider.
            user_id (str | Unset): The buyer's user ID.
            status (str | Unset): The order status.
                Possible values:
                - `UNPAID`: The order is placed, but payment is not yet completed.
                - `ON_HOLD`: The order is accepted and is waiting for fulfillment so the buyer may still cancel without the
                seller’s approval. If `order_type=PRE_ORDER`, it also means the product is still awaiting release so payment
                will only be authorized 1 day before the release, but the seller should start preparing for the release.
                - `AWAITING_SHIPMENT`: The order is ready for shipment, but no items are shipped yet.
                - `PARTIALLY_SHIPPING`: Some items in the order are shipped, but not all.
                - `AWAITING_COLLECTION`: The shipment is arranged, but the package is waiting to be collected by the carrier.
                - `IN_TRANSIT`: The package is collected by the carrier and delivery is in progress.
                - `DELIVERED`: The package is delivered to buyer.
                - `COMPLETED`: The order is completed, and no further returns or refunds are allowed.
                - `CANCELLED`: The order is cancelled.
            rts_time (int | Unset): The time seller shipped the order (call Ship Order endpoint successfully).
                Unix timestamp.
            payment (Payment | Unset):
            recipient_address (GetOrderDetailResponseDataOrderRecipientAddress | Unset):
            buyer_message (str | Unset): The note from buyer.
            create_time (int | Unset): The date and time that the order was created. Unix timestamp.
            tracking_number (str | Unset): Tracking number. Available after ship package.
            cancel_reason (str | Unset): The order level cancellation reason.
                **Note**: A multi-line order may have different `cancel_reason` across the multiple items.
                If this occurs, the order-level `cancel_reason` will surface the `cancel_reason` from the first line item.
                [See here](https://partner.tiktokshop.com/docv2/page/cancel-reasons) for more details on cancellation reasons.
            rts_sla_time (int | Unset): The latest shipping time specified by the platform. Unix timestamp.
            paid_time (int | Unset): The date and time that the order was paid. Unix timestamp.
            fulfillment_type (str | Unset): Fulfillment type.
                Only orders with fulfillment type can be shipped by sellers.
                Possible values:
                - `FULFILLMENT_BY_SELLER`: a method where sellers fulfill orders directly from their own inventory, without
                using TikTok's fulfillment centers. In this model, the seller is responsible for storing, packaging, and
                shipping the product to customers.
                - `FULFILLMENT_BY_TIKTOK`: a service offered by TikTok that enables sellers to send their products to TikTok's
                fulfillment centers. TikTok then takes care of storing, picking, packing, and shipping the products to
                customers.
                - `FULFILLMENT_BY_DILAYANI_TOKOPEDIA`: a method where Tokopedia GoTo Logistics provides warehousing and
                logistics services to sellers and charges a fee for the service.
            seller_note (str | Unset): This field return the note, which seller notes in TikTok Seller Center.
            tts_sla_time (int | Unset): The latest collection time specified by the platform.
                Unix timestamp.
            cancel_order_sla_time (int | Unset): The automatic cancellation time for orders specified by the platform.
                Unix timestamp.
            update_time (int | Unset): Time of order status changes.
                Unix timestamp.
            packages (list[GetOrderDetailResponseDataOrderPackage] | Unset): List of packages included in this order
            delivery_type (str | Unset): Indicates whether it is a PickUp DropOff (PUDO) location. The PUDO location is
                selected by the buyer when placing orders.
                - `HOME_DELIVERY`: not a PUDO location
                - `COLLECTION_POINT`: a PUDO location
            is_sample_order (bool | Unset): Use this field to determine whether the order is a sample order.
            warehouse_id (str | Unset): seller warehouse ID.
            split_or_combine_tag (str | Unset): Indicate whether the order is combined or split.
                - `COMBINED`
                - `SPLIT`
                This field will be used in future fulfillment apis.
            has_updated_recipient_address (bool | Unset): Whether the recipient address has been updated.
                - `false`: no update
                - `true`: updated
            cpf (str | Unset): CPF (invoice number), used to issue an invoice. Exclusive for the Brazil market.
            delivery_option_id (str | Unset): Order delivery option ID.
            delivery_sla_time (int | Unset): Order should arrive by this date to be considered on-time and to avoid late
                delivery penalties.
            payment_method_name (str | Unset): Payment method name, only for display
            payment_card_type (str | Unset): Code to distinguish different payment method. Only assigned when the payment
                method is using bank card. Possible values are: Debit, Credit, Prepaid
            channel_entity_national_registry_id (str | Unset): The national channel entity registration ID  of payment
                institution/creditor. In Brazil, it is the CNPJ of payment instituion.
            payment_method_code (str | Unset): Payment method code identifying current transaction. It will contains payment
                method and card brand if it is card transaction.
            payment_auth_code (str | Unset): Authorization code of current transaction (only for the Brazilian market).
                For card transactions (credit/debit card), this field will be transaction authorization code. For PIX
                transactions, this field will be E2E ID.
            shipping_due_time (int | Unset): If the order hasn't updated its status to `AWAITING_COLLECTION` before this
                time, the order will be automatically canceled by TikTok Shop.
            line_items (list[GetOrderDetailResponseDataOrderLineItem] | Unset): Line item info list.
            shipping_type (str | Unset): The method of delivery.
                - `TIKTOK`: shipping service provided by TikTok. The seller should obtain shipping label from TikTok.
                - `SELLER`: seller provides shipping, including through 3rd party fulfillment providers on behalf of the seller.
                - `TIKTOK_DIGITAL`: Tiktok delivers virtual goods directly to buyers. There is no action needed.
            buyer_email (str | Unset): The anonymized email address of the buyer. It is not recommended to send messages
                directly to this email address. If you need to contact the buyer, please go to Seller Center - Buyer Messages
                page.
            delivery_time (int | Unset): The timestamp of the order's status update to `DELIVERED`.
            need_upload_invoice (str | Unset): Whether an invoice needs to be uploaded and uploaded status (only for Brazil
                market).
                - UNKNOWN: Currently unable to confirm whether an invoice is needed
                - NEED_INVOICE: This order requires an invoice and the invoice has not been uploaded yet
                - NO_NEED：This order does not require an invoice
                - INVOICE_UPLOADED: The invoice for this order has been uploaded and verified. If the order is split, it will be
                marked as "uploaded" once any sub-order's invoice is uploaded.
                - INVOICE_PROCESSING: The invoice for this order is currently being uploaded/cancelled. Please wait for the
                final result and do not repeat the operation
            is_cod (bool | Unset): This option is for sellers that accept cash payment on delivery which is rare. Buyers
                will pay in cash upon receipt of package. Default value is `FALSE`. Only applicable to countries where Cash on
                Delivery (COD) is supported.
            request_cancel_time (int | Unset): Buyer request cancel time.
            delivery_option_required_delivery_time (int | Unset): Order should be delivered before this time.
            delivery_option_name (str | Unset): Delivery option name. For display purposes only.
            is_buyer_request_cancel (bool | Unset): True when the buyer has a pending cancellation request
            delivery_due_time (int | Unset): If the order hasn't updated its status to `DELIVERED` before this time, the
                order will be automatically canceled by TikTok Shop.
            collection_time (int | Unset): The timestamp of the order's status update to `IN_TRANSIT`.
            is_on_hold_order (bool | Unset): Indicates whether the order experienced or will be experienced `ON_HOLD`
                status.
            cancel_time (int | Unset): The timestamp of the order's status update to `CANCELLED`.
            is_replacement_order (bool | Unset): When true, this is a replacement order.
            replaced_order_id (str | Unset): The order ID for the order that is being replaced. Returned only if
                `is_replacement_order` = `true`
            collection_due_time (int | Unset): If the order hasn't updated its status to `IN_TRANSIT` before this time, the
                order will be automatically canceled by TikTok Shop
            pick_up_cut_off_time (int | Unset): To avoid LDR, you must ensure the package is picked up by this time. Only
                applicable in Southeast Asia regions.
            fast_dispatch_sla_time (int | Unset): The latest collection time to gain incentives of NDD (Next Day Delivery)
                project. Unix timestamp
                Only available in Thailand and Philippines.
            commerce_platform (str | Unset): The platform where the order was placed.
                Possible values:
                - `TIKTOK_SHOP`
                - `TOKOPEDIA`
                - `TIKTOK_SHOP_APP`
                **Note**: `Tokopedia` and `Tiktok Shop App` available only in the SEA market.
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
            is_subscription_order (bool | Unset): Subscription orders are recurring orders set up by customers. If TRUE,
                this order is generated from a subscription order
            is_refundable_sample (bool | Unset): This indicates if an order is a refundable sample. Refundable samples lets
                sellers collaborate with creators by refunding product costs only when creators meet sales thresholds.
            authentication_required (bool | Unset): If true, order requires authentication. Use an approved in-house
                authentication service after an order has been placed for verification. This must be completed before shipment.
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
            instore_pickup_sla_time (int | Unset): The latest buyer pickup time for instore pickup method specified by the
                platform. Currently applicable for SEA market. Unix timestamp.
            fast_rts_sla_time (int | Unset): Indicate fast fulfillment SLA for shipping action. Applicable for SEA market
                only. Unix timestamp
            fast_collection_sla_time (int | Unset): Indicate fast fulfillment SLA for collection action. Applicable for SEA
                market only. Unix timestamp
     """

    id: str | Unset = UNSET
    cancellation_initiator: str | Unset = UNSET
    shipping_provider: str | Unset = UNSET
    shipping_provider_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    status: str | Unset = UNSET
    rts_time: int | Unset = UNSET
    payment: Payment | Unset = UNSET
    recipient_address: GetOrderDetailResponseDataOrderRecipientAddress | Unset = UNSET
    buyer_message: str | Unset = UNSET
    create_time: int | Unset = UNSET
    tracking_number: str | Unset = UNSET
    cancel_reason: str | Unset = UNSET
    rts_sla_time: int | Unset = UNSET
    paid_time: int | Unset = UNSET
    fulfillment_type: str | Unset = UNSET
    seller_note: str | Unset = UNSET
    tts_sla_time: int | Unset = UNSET
    cancel_order_sla_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    packages: list[GetOrderDetailResponseDataOrderPackage] | Unset = UNSET
    delivery_type: str | Unset = UNSET
    is_sample_order: bool | Unset = UNSET
    warehouse_id: str | Unset = UNSET
    split_or_combine_tag: str | Unset = UNSET
    has_updated_recipient_address: bool | Unset = UNSET
    cpf: str | Unset = UNSET
    delivery_option_id: str | Unset = UNSET
    delivery_sla_time: int | Unset = UNSET
    payment_method_name: str | Unset = UNSET
    payment_card_type: str | Unset = UNSET
    channel_entity_national_registry_id: str | Unset = UNSET
    payment_method_code: str | Unset = UNSET
    payment_auth_code: str | Unset = UNSET
    shipping_due_time: int | Unset = UNSET
    line_items: list[GetOrderDetailResponseDataOrderLineItem] | Unset = UNSET
    shipping_type: str | Unset = UNSET
    buyer_email: str | Unset = UNSET
    delivery_time: int | Unset = UNSET
    need_upload_invoice: str | Unset = UNSET
    is_cod: bool | Unset = UNSET
    request_cancel_time: int | Unset = UNSET
    delivery_option_required_delivery_time: int | Unset = UNSET
    delivery_option_name: str | Unset = UNSET
    is_buyer_request_cancel: bool | Unset = UNSET
    delivery_due_time: int | Unset = UNSET
    collection_time: int | Unset = UNSET
    is_on_hold_order: bool | Unset = UNSET
    cancel_time: int | Unset = UNSET
    is_replacement_order: bool | Unset = UNSET
    replaced_order_id: str | Unset = UNSET
    collection_due_time: int | Unset = UNSET
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
    is_subscription_order: bool | Unset = UNSET
    is_refundable_sample: bool | Unset = UNSET
    authentication_required: bool | Unset = UNSET
    consultation_id: str | Unset = UNSET
    fast_delivery_program: str | Unset = UNSET
    buyer_nickname: str | Unset = UNSET
    buyer_avatar: str | Unset = UNSET
    order_rights: list[int] | Unset = UNSET
    fulfillment_priority_level: int | Unset = UNSET
    recommended_shipping_time: int | Unset = UNSET
    instore_pickup_sla_time: int | Unset = UNSET
    fast_rts_sla_time: int | Unset = UNSET
    fast_collection_sla_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_order_detail_response_data_order_line_item import GetOrderDetailResponseDataOrderLineItem # noqa: PLC0415
        from ..models.get_order_detail_response_data_order_package import GetOrderDetailResponseDataOrderPackage # noqa: PLC0415
        from ..models.get_order_detail_response_data_order_recipient_address import GetOrderDetailResponseDataOrderRecipientAddress # noqa: PLC0415
        from ..models.handling_duration import HandlingDuration # noqa: PLC0415
        from ..models.payment import Payment # noqa: PLC0415
        id = self.id

        cancellation_initiator = self.cancellation_initiator

        shipping_provider = self.shipping_provider

        shipping_provider_id = self.shipping_provider_id

        user_id = self.user_id

        status = self.status

        rts_time = self.rts_time

        payment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payment, Unset):
            payment = self.payment.to_dict()

        recipient_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipient_address, Unset):
            recipient_address = self.recipient_address.to_dict()

        buyer_message = self.buyer_message

        create_time = self.create_time

        tracking_number = self.tracking_number

        cancel_reason = self.cancel_reason

        rts_sla_time = self.rts_sla_time

        paid_time = self.paid_time

        fulfillment_type = self.fulfillment_type

        seller_note = self.seller_note

        tts_sla_time = self.tts_sla_time

        cancel_order_sla_time = self.cancel_order_sla_time

        update_time = self.update_time

        packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)



        delivery_type = self.delivery_type

        is_sample_order = self.is_sample_order

        warehouse_id = self.warehouse_id

        split_or_combine_tag = self.split_or_combine_tag

        has_updated_recipient_address = self.has_updated_recipient_address

        cpf = self.cpf

        delivery_option_id = self.delivery_option_id

        delivery_sla_time = self.delivery_sla_time

        payment_method_name = self.payment_method_name

        payment_card_type = self.payment_card_type

        channel_entity_national_registry_id = self.channel_entity_national_registry_id

        payment_method_code = self.payment_method_code

        payment_auth_code = self.payment_auth_code

        shipping_due_time = self.shipping_due_time

        line_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_items, Unset):
            line_items = []
            for line_items_item_data in self.line_items:
                line_items_item = line_items_item_data.to_dict()
                line_items.append(line_items_item)



        shipping_type = self.shipping_type

        buyer_email = self.buyer_email

        delivery_time = self.delivery_time

        need_upload_invoice = self.need_upload_invoice

        is_cod = self.is_cod

        request_cancel_time = self.request_cancel_time

        delivery_option_required_delivery_time = self.delivery_option_required_delivery_time

        delivery_option_name = self.delivery_option_name

        is_buyer_request_cancel = self.is_buyer_request_cancel

        delivery_due_time = self.delivery_due_time

        collection_time = self.collection_time

        is_on_hold_order = self.is_on_hold_order

        cancel_time = self.cancel_time

        is_replacement_order = self.is_replacement_order

        replaced_order_id = self.replaced_order_id

        collection_due_time = self.collection_due_time

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

        is_subscription_order = self.is_subscription_order

        is_refundable_sample = self.is_refundable_sample

        authentication_required = self.authentication_required

        consultation_id = self.consultation_id

        fast_delivery_program = self.fast_delivery_program

        buyer_nickname = self.buyer_nickname

        buyer_avatar = self.buyer_avatar

        order_rights: list[int] | Unset = UNSET
        if not isinstance(self.order_rights, Unset):
            order_rights = self.order_rights



        fulfillment_priority_level = self.fulfillment_priority_level

        recommended_shipping_time = self.recommended_shipping_time

        instore_pickup_sla_time = self.instore_pickup_sla_time

        fast_rts_sla_time = self.fast_rts_sla_time

        fast_collection_sla_time = self.fast_collection_sla_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if cancellation_initiator is not UNSET:
            field_dict["cancellation_initiator"] = cancellation_initiator
        if shipping_provider is not UNSET:
            field_dict["shipping_provider"] = shipping_provider
        if shipping_provider_id is not UNSET:
            field_dict["shipping_provider_id"] = shipping_provider_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if status is not UNSET:
            field_dict["status"] = status
        if rts_time is not UNSET:
            field_dict["rts_time"] = rts_time
        if payment is not UNSET:
            field_dict["payment"] = payment
        if recipient_address is not UNSET:
            field_dict["recipient_address"] = recipient_address
        if buyer_message is not UNSET:
            field_dict["buyer_message"] = buyer_message
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if cancel_reason is not UNSET:
            field_dict["cancel_reason"] = cancel_reason
        if rts_sla_time is not UNSET:
            field_dict["rts_sla_time"] = rts_sla_time
        if paid_time is not UNSET:
            field_dict["paid_time"] = paid_time
        if fulfillment_type is not UNSET:
            field_dict["fulfillment_type"] = fulfillment_type
        if seller_note is not UNSET:
            field_dict["seller_note"] = seller_note
        if tts_sla_time is not UNSET:
            field_dict["tts_sla_time"] = tts_sla_time
        if cancel_order_sla_time is not UNSET:
            field_dict["cancel_order_sla_time"] = cancel_order_sla_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if packages is not UNSET:
            field_dict["packages"] = packages
        if delivery_type is not UNSET:
            field_dict["delivery_type"] = delivery_type
        if is_sample_order is not UNSET:
            field_dict["is_sample_order"] = is_sample_order
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id
        if split_or_combine_tag is not UNSET:
            field_dict["split_or_combine_tag"] = split_or_combine_tag
        if has_updated_recipient_address is not UNSET:
            field_dict["has_updated_recipient_address"] = has_updated_recipient_address
        if cpf is not UNSET:
            field_dict["cpf"] = cpf
        if delivery_option_id is not UNSET:
            field_dict["delivery_option_id"] = delivery_option_id
        if delivery_sla_time is not UNSET:
            field_dict["delivery_sla_time"] = delivery_sla_time
        if payment_method_name is not UNSET:
            field_dict["payment_method_name"] = payment_method_name
        if payment_card_type is not UNSET:
            field_dict["payment_card_type"] = payment_card_type
        if channel_entity_national_registry_id is not UNSET:
            field_dict["channel_entity_national_registry_id"] = channel_entity_national_registry_id
        if payment_method_code is not UNSET:
            field_dict["payment_method_code"] = payment_method_code
        if payment_auth_code is not UNSET:
            field_dict["payment_auth_code"] = payment_auth_code
        if shipping_due_time is not UNSET:
            field_dict["shipping_due_time"] = shipping_due_time
        if line_items is not UNSET:
            field_dict["line_items"] = line_items
        if shipping_type is not UNSET:
            field_dict["shipping_type"] = shipping_type
        if buyer_email is not UNSET:
            field_dict["buyer_email"] = buyer_email
        if delivery_time is not UNSET:
            field_dict["delivery_time"] = delivery_time
        if need_upload_invoice is not UNSET:
            field_dict["need_upload_invoice"] = need_upload_invoice
        if is_cod is not UNSET:
            field_dict["is_cod"] = is_cod
        if request_cancel_time is not UNSET:
            field_dict["request_cancel_time"] = request_cancel_time
        if delivery_option_required_delivery_time is not UNSET:
            field_dict["delivery_option_required_delivery_time"] = delivery_option_required_delivery_time
        if delivery_option_name is not UNSET:
            field_dict["delivery_option_name"] = delivery_option_name
        if is_buyer_request_cancel is not UNSET:
            field_dict["is_buyer_request_cancel"] = is_buyer_request_cancel
        if delivery_due_time is not UNSET:
            field_dict["delivery_due_time"] = delivery_due_time
        if collection_time is not UNSET:
            field_dict["collection_time"] = collection_time
        if is_on_hold_order is not UNSET:
            field_dict["is_on_hold_order"] = is_on_hold_order
        if cancel_time is not UNSET:
            field_dict["cancel_time"] = cancel_time
        if is_replacement_order is not UNSET:
            field_dict["is_replacement_order"] = is_replacement_order
        if replaced_order_id is not UNSET:
            field_dict["replaced_order_id"] = replaced_order_id
        if collection_due_time is not UNSET:
            field_dict["collection_due_time"] = collection_due_time
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
        if is_subscription_order is not UNSET:
            field_dict["is_subscription_order"] = is_subscription_order
        if is_refundable_sample is not UNSET:
            field_dict["is_refundable_sample"] = is_refundable_sample
        if authentication_required is not UNSET:
            field_dict["authentication_required"] = authentication_required
        if consultation_id is not UNSET:
            field_dict["consultation_id"] = consultation_id
        if fast_delivery_program is not UNSET:
            field_dict["fast_delivery_program"] = fast_delivery_program
        if buyer_nickname is not UNSET:
            field_dict["buyer_nickname"] = buyer_nickname
        if buyer_avatar is not UNSET:
            field_dict["buyer_avatar"] = buyer_avatar
        if order_rights is not UNSET:
            field_dict["order_rights"] = order_rights
        if fulfillment_priority_level is not UNSET:
            field_dict["fulfillment_priority_level"] = fulfillment_priority_level
        if recommended_shipping_time is not UNSET:
            field_dict["recommended_shipping_time"] = recommended_shipping_time
        if instore_pickup_sla_time is not UNSET:
            field_dict["instore_pickup_sla_time"] = instore_pickup_sla_time
        if fast_rts_sla_time is not UNSET:
            field_dict["fast_rts_sla_time"] = fast_rts_sla_time
        if fast_collection_sla_time is not UNSET:
            field_dict["fast_collection_sla_time"] = fast_collection_sla_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_detail_response_data_order_line_item import GetOrderDetailResponseDataOrderLineItem # noqa: PLC0415
        from ..models.get_order_detail_response_data_order_package import GetOrderDetailResponseDataOrderPackage # noqa: PLC0415
        from ..models.get_order_detail_response_data_order_recipient_address import GetOrderDetailResponseDataOrderRecipientAddress # noqa: PLC0415
        from ..models.handling_duration import HandlingDuration # noqa: PLC0415
        from ..models.payment import Payment # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        cancellation_initiator = d.pop("cancellation_initiator", UNSET)

        shipping_provider = d.pop("shipping_provider", UNSET)

        shipping_provider_id = d.pop("shipping_provider_id", UNSET)

        user_id = d.pop("user_id", UNSET)

        status = d.pop("status", UNSET)

        rts_time = d.pop("rts_time", UNSET)

        _payment = d.pop("payment", UNSET)
        payment: Payment | Unset
        if isinstance(_payment,  Unset):
            payment = UNSET
        else:
            payment = Payment.from_dict(_payment)




        _recipient_address = d.pop("recipient_address", UNSET)
        recipient_address: GetOrderDetailResponseDataOrderRecipientAddress | Unset
        if isinstance(_recipient_address,  Unset):
            recipient_address = UNSET
        else:
            recipient_address = GetOrderDetailResponseDataOrderRecipientAddress.from_dict(_recipient_address)




        buyer_message = d.pop("buyer_message", UNSET)

        create_time = d.pop("create_time", UNSET)

        tracking_number = d.pop("tracking_number", UNSET)

        cancel_reason = d.pop("cancel_reason", UNSET)

        rts_sla_time = d.pop("rts_sla_time", UNSET)

        paid_time = d.pop("paid_time", UNSET)

        fulfillment_type = d.pop("fulfillment_type", UNSET)

        seller_note = d.pop("seller_note", UNSET)

        tts_sla_time = d.pop("tts_sla_time", UNSET)

        cancel_order_sla_time = d.pop("cancel_order_sla_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        _packages = d.pop("packages", UNSET)
        packages: list[GetOrderDetailResponseDataOrderPackage] | Unset = UNSET
        if _packages is not UNSET:
            packages = []
            for packages_item_data in _packages:
                packages_item = GetOrderDetailResponseDataOrderPackage.from_dict(packages_item_data)



                packages.append(packages_item)


        delivery_type = d.pop("delivery_type", UNSET)

        is_sample_order = d.pop("is_sample_order", UNSET)

        warehouse_id = d.pop("warehouse_id", UNSET)

        split_or_combine_tag = d.pop("split_or_combine_tag", UNSET)

        has_updated_recipient_address = d.pop("has_updated_recipient_address", UNSET)

        cpf = d.pop("cpf", UNSET)

        delivery_option_id = d.pop("delivery_option_id", UNSET)

        delivery_sla_time = d.pop("delivery_sla_time", UNSET)

        payment_method_name = d.pop("payment_method_name", UNSET)

        payment_card_type = d.pop("payment_card_type", UNSET)

        channel_entity_national_registry_id = d.pop("channel_entity_national_registry_id", UNSET)

        payment_method_code = d.pop("payment_method_code", UNSET)

        payment_auth_code = d.pop("payment_auth_code", UNSET)

        shipping_due_time = d.pop("shipping_due_time", UNSET)

        _line_items = d.pop("line_items", UNSET)
        line_items: list[GetOrderDetailResponseDataOrderLineItem] | Unset = UNSET
        if _line_items is not UNSET:
            line_items = []
            for line_items_item_data in _line_items:
                line_items_item = GetOrderDetailResponseDataOrderLineItem.from_dict(line_items_item_data)



                line_items.append(line_items_item)


        shipping_type = d.pop("shipping_type", UNSET)

        buyer_email = d.pop("buyer_email", UNSET)

        delivery_time = d.pop("delivery_time", UNSET)

        need_upload_invoice = d.pop("need_upload_invoice", UNSET)

        is_cod = d.pop("is_cod", UNSET)

        request_cancel_time = d.pop("request_cancel_time", UNSET)

        delivery_option_required_delivery_time = d.pop("delivery_option_required_delivery_time", UNSET)

        delivery_option_name = d.pop("delivery_option_name", UNSET)

        is_buyer_request_cancel = d.pop("is_buyer_request_cancel", UNSET)

        delivery_due_time = d.pop("delivery_due_time", UNSET)

        collection_time = d.pop("collection_time", UNSET)

        is_on_hold_order = d.pop("is_on_hold_order", UNSET)

        cancel_time = d.pop("cancel_time", UNSET)

        is_replacement_order = d.pop("is_replacement_order", UNSET)

        replaced_order_id = d.pop("replaced_order_id", UNSET)

        collection_due_time = d.pop("collection_due_time", UNSET)

        pick_up_cut_off_time = d.pop("pick_up_cut_off_time", UNSET)

        fast_dispatch_sla_time = d.pop("fast_dispatch_sla_time", UNSET)

        commerce_platform = d.pop("commerce_platform", UNSET)

        order_type = d.pop("order_type", UNSET)

        release_date = d.pop("release_date", UNSET)

        _handling_duration = d.pop("handling_duration", UNSET)
        handling_duration: HandlingDuration | Unset
        if isinstance(_handling_duration,  Unset):
            handling_duration = UNSET
        else:
            handling_duration = HandlingDuration.from_dict(_handling_duration)




        auto_combine_group_id = d.pop("auto_combine_group_id", UNSET)

        cpf_name = d.pop("cpf_name", UNSET)

        is_exchange_order = d.pop("is_exchange_order", UNSET)

        exchange_source_order_id = d.pop("exchange_source_order_id", UNSET)

        is_subscription_order = d.pop("is_subscription_order", UNSET)

        is_refundable_sample = d.pop("is_refundable_sample", UNSET)

        authentication_required = d.pop("authentication_required", UNSET)

        consultation_id = d.pop("consultation_id", UNSET)

        fast_delivery_program = d.pop("fast_delivery_program", UNSET)

        buyer_nickname = d.pop("buyer_nickname", UNSET)

        buyer_avatar = d.pop("buyer_avatar", UNSET)

        order_rights = cast(list[int], d.pop("order_rights", UNSET))


        fulfillment_priority_level = d.pop("fulfillment_priority_level", UNSET)

        recommended_shipping_time = d.pop("recommended_shipping_time", UNSET)

        instore_pickup_sla_time = d.pop("instore_pickup_sla_time", UNSET)

        fast_rts_sla_time = d.pop("fast_rts_sla_time", UNSET)

        fast_collection_sla_time = d.pop("fast_collection_sla_time", UNSET)

        get_order_detail_response_data_order = cls(
            id=id,
            cancellation_initiator=cancellation_initiator,
            shipping_provider=shipping_provider,
            shipping_provider_id=shipping_provider_id,
            user_id=user_id,
            status=status,
            rts_time=rts_time,
            payment=payment,
            recipient_address=recipient_address,
            buyer_message=buyer_message,
            create_time=create_time,
            tracking_number=tracking_number,
            cancel_reason=cancel_reason,
            rts_sla_time=rts_sla_time,
            paid_time=paid_time,
            fulfillment_type=fulfillment_type,
            seller_note=seller_note,
            tts_sla_time=tts_sla_time,
            cancel_order_sla_time=cancel_order_sla_time,
            update_time=update_time,
            packages=packages,
            delivery_type=delivery_type,
            is_sample_order=is_sample_order,
            warehouse_id=warehouse_id,
            split_or_combine_tag=split_or_combine_tag,
            has_updated_recipient_address=has_updated_recipient_address,
            cpf=cpf,
            delivery_option_id=delivery_option_id,
            delivery_sla_time=delivery_sla_time,
            payment_method_name=payment_method_name,
            payment_card_type=payment_card_type,
            channel_entity_national_registry_id=channel_entity_national_registry_id,
            payment_method_code=payment_method_code,
            payment_auth_code=payment_auth_code,
            shipping_due_time=shipping_due_time,
            line_items=line_items,
            shipping_type=shipping_type,
            buyer_email=buyer_email,
            delivery_time=delivery_time,
            need_upload_invoice=need_upload_invoice,
            is_cod=is_cod,
            request_cancel_time=request_cancel_time,
            delivery_option_required_delivery_time=delivery_option_required_delivery_time,
            delivery_option_name=delivery_option_name,
            is_buyer_request_cancel=is_buyer_request_cancel,
            delivery_due_time=delivery_due_time,
            collection_time=collection_time,
            is_on_hold_order=is_on_hold_order,
            cancel_time=cancel_time,
            is_replacement_order=is_replacement_order,
            replaced_order_id=replaced_order_id,
            collection_due_time=collection_due_time,
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
            is_subscription_order=is_subscription_order,
            is_refundable_sample=is_refundable_sample,
            authentication_required=authentication_required,
            consultation_id=consultation_id,
            fast_delivery_program=fast_delivery_program,
            buyer_nickname=buyer_nickname,
            buyer_avatar=buyer_avatar,
            order_rights=order_rights,
            fulfillment_priority_level=fulfillment_priority_level,
            recommended_shipping_time=recommended_shipping_time,
            instore_pickup_sla_time=instore_pickup_sla_time,
            fast_rts_sla_time=fast_rts_sla_time,
            fast_collection_sla_time=fast_collection_sla_time,
        )


        get_order_detail_response_data_order.additional_properties = d
        return get_order_detail_response_data_order

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
