from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combined_listing_sku import CombinedListingSku
    from ..models.item_tax import ItemTax
    from ..models.sub_item_info import SubItemInfo
    from ..models.unboxing_case_list import UnboxingCaseList


T = TypeVar("T", bound="GetOrderListResponseDataOrderLineItem")


@_attrs_define
class GetOrderListResponseDataOrderLineItem:
    """
    Attributes:
        id (str | Unset): Line item ID.
        sku_id (str | Unset): SKU ID.
        combined_listing_skus (list[CombinedListingSku] | Unset): For a virtual bundle SKU, returns an array of related
            product SKUs that compose the virtual bundle.
        display_status (str | Unset): Available values:
            - `UNPAID`: The order has been placed, but payment has not yet completed.
            - `AWAITING_SHIPMENT`: The order is ready for shipment, but no items have been shipped yet.
            - `AWAITING_COLLECTION`: Shipping has been arranged, but the package is waiting to be collected by the carrier.
            - `IN_TRANSIT`: The package has been collected by the carrier and delivery is in progress.
            - `DELIVERED`: The package has been delivered to the buyer.
            - `COMPLETED`: The order has been completed, and no further returns or refunds are allowed.
            - `CANCELLED`: The order has been cancelled.
        product_name (str | Unset): Product name.
        seller_sku (str | Unset): The seller stock keeping unit (SKU) of the item.
        sku_image (str | Unset): SKU image.
        sku_name (str | Unset): The name of the SKU, combined by product SKU attribute like size or color. e.g. "Black,
            26"
        product_id (str | Unset): Product ID.
        sale_price (str | Unset): Item sale price. Please refer to the currency of `payment_info`.
        pfand_fee (str | Unset): Deposit fee that is applied to certain products, typically beverage containers such as
            bottles or cans.
            **Note** Only available in Germany market
        platform_discount (str | Unset): Platform discount amount. Please refer to the currency of `payment_info`.
        seller_discount (str | Unset): Seller discount amount. Please refer to the currency of `payment_info`.
        sku_type (str | Unset): [**Deprecated**: This field is deprecated and will be removed in a future API version.
            Use `order_type` instead.]

            The order line type.
            Possible values based on region:

            **All regions**
            - `NORMAL`: An item that is in stock and available for immediate purchase and fulfillment.
            - `ZERO_LOTTERY`: An item purchased during a lottery event in TikTok LIVE.
            - `SHOP_PARTNER`: An item purchased from a TikTok Shop partner store.

            **US**
            - `PRE_ORDER`: An item that is not yet available or released. Fulfillment starts on a specific date in the
            future.
            - `MADE_TO_ORDER`: An item that is produced only after the order is received. Fulfillment starts after the
            product is produced.
        cancel_reason (str | Unset): The cancellation reason. Please visit [our list of cancel
            reasons](https://partner.tiktokshop.com/docv2/page/67e61eee427345048595487d) for more information.
        original_price (str | Unset): Item original price. Please refer to the currency of `payment_info`.
        rts_time (int | Unset): The time sellers shipped the order (called [Ship Package
            API](https://partner.tiktokshop.com/docv2/page/650aa4f1defece02be6e7cb1) successfully). Unix timestamp.
        package_status (str | Unset): The package status of the item.
            Available values:
            - `TO_FULFILL`: Package awaiting seller to arrange shipment.
            - `PROCESSING`: Shipping has been arranged by the seller. Awaiting carrier collection.
            - `FULFILLING`: Package has been collected by carrier and is in transit.
            - `COMPLETED`: Package has been delivered.
            - `CANCELLED`: Package has been canceled. Normally, the package is canceled due to the package being lost or
            damaged.
        currency (str | Unset): Currency for payment.
        shipping_provider_name (str | Unset): The shipping provider name.
        cancel_user (str | Unset): Cancellation request initiator.
            Available values:
            - `BUYER`
            - `SELLER`
            - `OPERATOR`
            - `SYSTEM`
        shipping_provider_id (str | Unset): The shipping provider ID of the item.
        is_gift (bool | Unset): Indicates whether the current order line item is a gift.
        item_tax (list[ItemTax] | Unset): Item tax detail.
        tracking_number (str | Unset): Tracking number. Available after package has been shipped.
        package_id (str | Unset): An order can contain one or more packages based on how the seller chooses to ship.
            Each package has a unique `package_id` and `tracking_id`.
        retail_delivery_fee (str | Unset): Retail delivery fee (RDF).

            **Note**: Only available in the US market.
        buyer_service_fee (str | Unset): A service fee is charged on every transaction made. The charge is applied from
            the fifth order onwards and collected directly from customers during checkout.

            **Note**: Only available in the Indonesia market.
        small_order_fee (str | Unset): Small order fee for Thailand (TH).
        handling_duration_days (str | Unset): [**Deprecated**: This field is deprecated and will be removed in a future
            API version. Use `handling_duration` instead.]

            The number of business days required for the seller to process the order and hand it over to a shipping carrier
            after the order is placed.
            Applicable only if the value for `sku_type` is `MADE_TO_ORDER`.
        is_dangerous_good (bool | Unset): Whether the SKU is a hazmat item. When creating the label for a hazmat item,
            you must follow the platform rules to put certain items into one package. Please refer to the relationship
            between `sku_id` and `package_id` to determine how to follow platform rules.
        needs_prescription (bool | Unset): A flag to indicate whether the included product requires a prescription.
        gift_retail_price (str | Unset): Retail price of the free item in orders Live giveaway, free sample and gift
            with purchase. For other orders, this field always returns 0.
            This amount can be used for free samples and live giveaway order invoice in Brazil
        is_unboxing_item (bool | Unset): If `true`, indicates the sku is a blind box item that will need be unboxed to
            reveal the actual product to the buyer. The actual product sku name and picture can also be updated to TikTok
            after the unboxing is completed.

            Note: This is currently only available in the US market.
        unboxing_sku_code (str | Unset): A seller's third party sku code for the actual unboxed item, which warehouse
            fulfillment operations can reference to identify the accurate product they are shipping.

            Note: This is currently only available in the US market.
        unboxing_case_list (list[UnboxingCaseList] | Unset): A seller's third party sku code for the case unboxed item,
            which warehouse fulfillment operations can reference to identify the accurate product they are shipping.

            Note: This is currently only available in the US market.
        room_id (str | Unset): The unique ID of the LIVE session where the order line item was created. If the order
            line item was not created from a LIVE session, this field returns an empty string.
        sub_item_info (list[SubItemInfo] | Unset): Sub items represent skus that belong to a "virtual bundle" that has
            been defined by a seller. The sub_item_info will include all relevant information about each item that is
            required to be fulfilled as part of the virtual bundle.
            Note: Each quantity of any sku has a unique sub_item_info "id", which allows the seller to perform line-level
            fulfillments, in the event the items are split across different warehouse locations.
        distance_shipping_fee (str | Unset): Distance shipping fee is fee that charged charged by our logistics partner
            and covers the separate distance-based cost for deliveries outside Java island as a part of Horizon+ Program.
            Only applicable in ID Market.
        distance_fee (str | Unset): Total distance fee for Horizon+ Program. Only applicable for ID market
        shipping_vat_amount (str | Unset): Shipping vat amount
            Available in EU market
        shipping_vat_rate (str | Unset): Shipping vat rate
            Available in EU market
        is_pod_customized (bool | Unset): Identifies if this SKU contains print on demand customization
        pod_info_id (str | Unset): ID of the print on demand customization details. This ID can be used to query for the
            exact details of the customization
        product_listing_type (str | Unset): This describes the product listing type of the SKU.
            Possible values:
            - `TEMPORARY LISTING`
    """

    id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    combined_listing_skus: list[CombinedListingSku] | Unset = UNSET
    display_status: str | Unset = UNSET
    product_name: str | Unset = UNSET
    seller_sku: str | Unset = UNSET
    sku_image: str | Unset = UNSET
    sku_name: str | Unset = UNSET
    product_id: str | Unset = UNSET
    sale_price: str | Unset = UNSET
    pfand_fee: str | Unset = UNSET
    platform_discount: str | Unset = UNSET
    seller_discount: str | Unset = UNSET
    sku_type: str | Unset = UNSET
    cancel_reason: str | Unset = UNSET
    original_price: str | Unset = UNSET
    rts_time: int | Unset = UNSET
    package_status: str | Unset = UNSET
    currency: str | Unset = UNSET
    shipping_provider_name: str | Unset = UNSET
    cancel_user: str | Unset = UNSET
    shipping_provider_id: str | Unset = UNSET
    is_gift: bool | Unset = UNSET
    item_tax: list[ItemTax] | Unset = UNSET
    tracking_number: str | Unset = UNSET
    package_id: str | Unset = UNSET
    retail_delivery_fee: str | Unset = UNSET
    buyer_service_fee: str | Unset = UNSET
    small_order_fee: str | Unset = UNSET
    handling_duration_days: str | Unset = UNSET
    is_dangerous_good: bool | Unset = UNSET
    needs_prescription: bool | Unset = UNSET
    gift_retail_price: str | Unset = UNSET
    is_unboxing_item: bool | Unset = UNSET
    unboxing_sku_code: str | Unset = UNSET
    unboxing_case_list: list[UnboxingCaseList] | Unset = UNSET
    room_id: str | Unset = UNSET
    sub_item_info: list[SubItemInfo] | Unset = UNSET
    distance_shipping_fee: str | Unset = UNSET
    distance_fee: str | Unset = UNSET
    shipping_vat_amount: str | Unset = UNSET
    shipping_vat_rate: str | Unset = UNSET
    is_pod_customized: bool | Unset = UNSET
    pod_info_id: str | Unset = UNSET
    product_listing_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sku_id = self.sku_id

        combined_listing_skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.combined_listing_skus, Unset):
            combined_listing_skus = []
            for combined_listing_skus_item_data in self.combined_listing_skus:
                combined_listing_skus_item = combined_listing_skus_item_data.to_dict()
                combined_listing_skus.append(combined_listing_skus_item)

        display_status = self.display_status

        product_name = self.product_name

        seller_sku = self.seller_sku

        sku_image = self.sku_image

        sku_name = self.sku_name

        product_id = self.product_id

        sale_price = self.sale_price

        pfand_fee = self.pfand_fee

        platform_discount = self.platform_discount

        seller_discount = self.seller_discount

        sku_type = self.sku_type

        cancel_reason = self.cancel_reason

        original_price = self.original_price

        rts_time = self.rts_time

        package_status = self.package_status

        currency = self.currency

        shipping_provider_name = self.shipping_provider_name

        cancel_user = self.cancel_user

        shipping_provider_id = self.shipping_provider_id

        is_gift = self.is_gift

        item_tax: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.item_tax, Unset):
            item_tax = []
            for item_tax_item_data in self.item_tax:
                item_tax_item = item_tax_item_data.to_dict()
                item_tax.append(item_tax_item)

        tracking_number = self.tracking_number

        package_id = self.package_id

        retail_delivery_fee = self.retail_delivery_fee

        buyer_service_fee = self.buyer_service_fee

        small_order_fee = self.small_order_fee

        handling_duration_days = self.handling_duration_days

        is_dangerous_good = self.is_dangerous_good

        needs_prescription = self.needs_prescription

        gift_retail_price = self.gift_retail_price

        is_unboxing_item = self.is_unboxing_item

        unboxing_sku_code = self.unboxing_sku_code

        unboxing_case_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unboxing_case_list, Unset):
            unboxing_case_list = []
            for unboxing_case_list_item_data in self.unboxing_case_list:
                unboxing_case_list_item = unboxing_case_list_item_data.to_dict()
                unboxing_case_list.append(unboxing_case_list_item)

        room_id = self.room_id

        sub_item_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sub_item_info, Unset):
            sub_item_info = []
            for sub_item_info_item_data in self.sub_item_info:
                sub_item_info_item = sub_item_info_item_data.to_dict()
                sub_item_info.append(sub_item_info_item)

        distance_shipping_fee = self.distance_shipping_fee

        distance_fee = self.distance_fee

        shipping_vat_amount = self.shipping_vat_amount

        shipping_vat_rate = self.shipping_vat_rate

        is_pod_customized = self.is_pod_customized

        pod_info_id = self.pod_info_id

        product_listing_type = self.product_listing_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if combined_listing_skus is not UNSET:
            field_dict["combined_listing_skus"] = combined_listing_skus
        if display_status is not UNSET:
            field_dict["display_status"] = display_status
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if seller_sku is not UNSET:
            field_dict["seller_sku"] = seller_sku
        if sku_image is not UNSET:
            field_dict["sku_image"] = sku_image
        if sku_name is not UNSET:
            field_dict["sku_name"] = sku_name
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if sale_price is not UNSET:
            field_dict["sale_price"] = sale_price
        if pfand_fee is not UNSET:
            field_dict["pfand_fee"] = pfand_fee
        if platform_discount is not UNSET:
            field_dict["platform_discount"] = platform_discount
        if seller_discount is not UNSET:
            field_dict["seller_discount"] = seller_discount
        if sku_type is not UNSET:
            field_dict["sku_type"] = sku_type
        if cancel_reason is not UNSET:
            field_dict["cancel_reason"] = cancel_reason
        if original_price is not UNSET:
            field_dict["original_price"] = original_price
        if rts_time is not UNSET:
            field_dict["rts_time"] = rts_time
        if package_status is not UNSET:
            field_dict["package_status"] = package_status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if shipping_provider_name is not UNSET:
            field_dict["shipping_provider_name"] = shipping_provider_name
        if cancel_user is not UNSET:
            field_dict["cancel_user"] = cancel_user
        if shipping_provider_id is not UNSET:
            field_dict["shipping_provider_id"] = shipping_provider_id
        if is_gift is not UNSET:
            field_dict["is_gift"] = is_gift
        if item_tax is not UNSET:
            field_dict["item_tax"] = item_tax
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if retail_delivery_fee is not UNSET:
            field_dict["retail_delivery_fee"] = retail_delivery_fee
        if buyer_service_fee is not UNSET:
            field_dict["buyer_service_fee"] = buyer_service_fee
        if small_order_fee is not UNSET:
            field_dict["small_order_fee"] = small_order_fee
        if handling_duration_days is not UNSET:
            field_dict["handling_duration_days"] = handling_duration_days
        if is_dangerous_good is not UNSET:
            field_dict["is_dangerous_good"] = is_dangerous_good
        if needs_prescription is not UNSET:
            field_dict["needs_prescription"] = needs_prescription
        if gift_retail_price is not UNSET:
            field_dict["gift_retail_price"] = gift_retail_price
        if is_unboxing_item is not UNSET:
            field_dict["is_unboxing_item"] = is_unboxing_item
        if unboxing_sku_code is not UNSET:
            field_dict["unboxing_sku_code"] = unboxing_sku_code
        if unboxing_case_list is not UNSET:
            field_dict["unboxing_case_list"] = unboxing_case_list
        if room_id is not UNSET:
            field_dict["room_id"] = room_id
        if sub_item_info is not UNSET:
            field_dict["sub_item_info"] = sub_item_info
        if distance_shipping_fee is not UNSET:
            field_dict["distance_shipping_fee"] = distance_shipping_fee
        if distance_fee is not UNSET:
            field_dict["distance_fee"] = distance_fee
        if shipping_vat_amount is not UNSET:
            field_dict["shipping_vat_amount"] = shipping_vat_amount
        if shipping_vat_rate is not UNSET:
            field_dict["shipping_vat_rate"] = shipping_vat_rate
        if is_pod_customized is not UNSET:
            field_dict["is_pod_customized"] = is_pod_customized
        if pod_info_id is not UNSET:
            field_dict["pod_info_id"] = pod_info_id
        if product_listing_type is not UNSET:
            field_dict["product_listing_type"] = product_listing_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_listing_sku import CombinedListingSku  # noqa: PLC0415
        from ..models.item_tax import ItemTax  # noqa: PLC0415
        from ..models.sub_item_info import SubItemInfo  # noqa: PLC0415
        from ..models.unboxing_case_list import UnboxingCaseList  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        _combined_listing_skus = d.pop("combined_listing_skus", UNSET)
        combined_listing_skus: list[CombinedListingSku] | Unset = UNSET
        if _combined_listing_skus is not UNSET:
            combined_listing_skus = []
            for combined_listing_skus_item_data in _combined_listing_skus:
                combined_listing_skus_item = CombinedListingSku.from_dict(combined_listing_skus_item_data)

                combined_listing_skus.append(combined_listing_skus_item)

        display_status = d.pop("display_status", UNSET)

        product_name = d.pop("product_name", UNSET)

        seller_sku = d.pop("seller_sku", UNSET)

        sku_image = d.pop("sku_image", UNSET)

        sku_name = d.pop("sku_name", UNSET)

        product_id = d.pop("product_id", UNSET)

        sale_price = d.pop("sale_price", UNSET)

        pfand_fee = d.pop("pfand_fee", UNSET)

        platform_discount = d.pop("platform_discount", UNSET)

        seller_discount = d.pop("seller_discount", UNSET)

        sku_type = d.pop("sku_type", UNSET)

        cancel_reason = d.pop("cancel_reason", UNSET)

        original_price = d.pop("original_price", UNSET)

        rts_time = d.pop("rts_time", UNSET)

        package_status = d.pop("package_status", UNSET)

        currency = d.pop("currency", UNSET)

        shipping_provider_name = d.pop("shipping_provider_name", UNSET)

        cancel_user = d.pop("cancel_user", UNSET)

        shipping_provider_id = d.pop("shipping_provider_id", UNSET)

        is_gift = d.pop("is_gift", UNSET)

        _item_tax = d.pop("item_tax", UNSET)
        item_tax: list[ItemTax] | Unset = UNSET
        if _item_tax is not UNSET:
            item_tax = []
            for item_tax_item_data in _item_tax:
                item_tax_item = ItemTax.from_dict(item_tax_item_data)

                item_tax.append(item_tax_item)

        tracking_number = d.pop("tracking_number", UNSET)

        package_id = d.pop("package_id", UNSET)

        retail_delivery_fee = d.pop("retail_delivery_fee", UNSET)

        buyer_service_fee = d.pop("buyer_service_fee", UNSET)

        small_order_fee = d.pop("small_order_fee", UNSET)

        handling_duration_days = d.pop("handling_duration_days", UNSET)

        is_dangerous_good = d.pop("is_dangerous_good", UNSET)

        needs_prescription = d.pop("needs_prescription", UNSET)

        gift_retail_price = d.pop("gift_retail_price", UNSET)

        is_unboxing_item = d.pop("is_unboxing_item", UNSET)

        unboxing_sku_code = d.pop("unboxing_sku_code", UNSET)

        _unboxing_case_list = d.pop("unboxing_case_list", UNSET)
        unboxing_case_list: list[UnboxingCaseList] | Unset = UNSET
        if _unboxing_case_list is not UNSET:
            unboxing_case_list = []
            for unboxing_case_list_item_data in _unboxing_case_list:
                unboxing_case_list_item = UnboxingCaseList.from_dict(unboxing_case_list_item_data)

                unboxing_case_list.append(unboxing_case_list_item)

        room_id = d.pop("room_id", UNSET)

        _sub_item_info = d.pop("sub_item_info", UNSET)
        sub_item_info: list[SubItemInfo] | Unset = UNSET
        if _sub_item_info is not UNSET:
            sub_item_info = []
            for sub_item_info_item_data in _sub_item_info:
                sub_item_info_item = SubItemInfo.from_dict(sub_item_info_item_data)

                sub_item_info.append(sub_item_info_item)

        distance_shipping_fee = d.pop("distance_shipping_fee", UNSET)

        distance_fee = d.pop("distance_fee", UNSET)

        shipping_vat_amount = d.pop("shipping_vat_amount", UNSET)

        shipping_vat_rate = d.pop("shipping_vat_rate", UNSET)

        is_pod_customized = d.pop("is_pod_customized", UNSET)

        pod_info_id = d.pop("pod_info_id", UNSET)

        product_listing_type = d.pop("product_listing_type", UNSET)

        get_order_list_response_data_order_line_item = cls(
            id=id,
            sku_id=sku_id,
            combined_listing_skus=combined_listing_skus,
            display_status=display_status,
            product_name=product_name,
            seller_sku=seller_sku,
            sku_image=sku_image,
            sku_name=sku_name,
            product_id=product_id,
            sale_price=sale_price,
            pfand_fee=pfand_fee,
            platform_discount=platform_discount,
            seller_discount=seller_discount,
            sku_type=sku_type,
            cancel_reason=cancel_reason,
            original_price=original_price,
            rts_time=rts_time,
            package_status=package_status,
            currency=currency,
            shipping_provider_name=shipping_provider_name,
            cancel_user=cancel_user,
            shipping_provider_id=shipping_provider_id,
            is_gift=is_gift,
            item_tax=item_tax,
            tracking_number=tracking_number,
            package_id=package_id,
            retail_delivery_fee=retail_delivery_fee,
            buyer_service_fee=buyer_service_fee,
            small_order_fee=small_order_fee,
            handling_duration_days=handling_duration_days,
            is_dangerous_good=is_dangerous_good,
            needs_prescription=needs_prescription,
            gift_retail_price=gift_retail_price,
            is_unboxing_item=is_unboxing_item,
            unboxing_sku_code=unboxing_sku_code,
            unboxing_case_list=unboxing_case_list,
            room_id=room_id,
            sub_item_info=sub_item_info,
            distance_shipping_fee=distance_shipping_fee,
            distance_fee=distance_fee,
            shipping_vat_amount=shipping_vat_amount,
            shipping_vat_rate=shipping_vat_rate,
            is_pod_customized=is_pod_customized,
            pod_info_id=pod_info_id,
            product_listing_type=product_listing_type,
        )

        get_order_list_response_data_order_line_item.additional_properties = d
        return get_order_list_response_data_order_line_item

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
