from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_tax import ItemTax


T = TypeVar("T", bound="SubItemInfo")


@_attrs_define
class SubItemInfo:
    """
    Attributes:
        id (str | Unset): Line item id of the sub_item. This unique identifier can be used when performing split/line-
            level fulfillment events.
        sku_id (str | Unset): SKU ID.
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
        platform_discount (str | Unset): Platform discount amount. Please refer to the currency of `payment_info`.
        seller_discount (str | Unset): Seller discount amount. Please refer to the currency of `payment_info`.
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
        item_tax (list[ItemTax] | Unset): Item tax detail.
        tracking_number (str | Unset): Tracking number. Available after package has been shipped.
        package_id (str | Unset): An order can contain one or more packages based on how the seller chooses to ship.
            Each package has a unique `package_id` and `tracking_id`.
        retail_delivery_fee (str | Unset): Retail delivery fee (RDF).
            **Note**: Only available in the US market.
        is_dangerous_good (bool | Unset): Whether the SKU is a hazmat item. When creating the label for a hazmat item,
            you must follow the platform rules to put certain items into one package. Please refer to the relationship
            between `sku_id` and `package_id` to determine how to follow platform rules.
        warehouse_id (str | Unset): Seller warehouse ID.
    """

    id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    display_status: str | Unset = UNSET
    product_name: str | Unset = UNSET
    seller_sku: str | Unset = UNSET
    sku_image: str | Unset = UNSET
    sku_name: str | Unset = UNSET
    product_id: str | Unset = UNSET
    sale_price: str | Unset = UNSET
    platform_discount: str | Unset = UNSET
    seller_discount: str | Unset = UNSET
    cancel_reason: str | Unset = UNSET
    original_price: str | Unset = UNSET
    rts_time: int | Unset = UNSET
    package_status: str | Unset = UNSET
    currency: str | Unset = UNSET
    shipping_provider_name: str | Unset = UNSET
    cancel_user: str | Unset = UNSET
    shipping_provider_id: str | Unset = UNSET
    item_tax: list[ItemTax] | Unset = UNSET
    tracking_number: str | Unset = UNSET
    package_id: str | Unset = UNSET
    retail_delivery_fee: str | Unset = UNSET
    is_dangerous_good: bool | Unset = UNSET
    warehouse_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sku_id = self.sku_id

        display_status = self.display_status

        product_name = self.product_name

        seller_sku = self.seller_sku

        sku_image = self.sku_image

        sku_name = self.sku_name

        product_id = self.product_id

        sale_price = self.sale_price

        platform_discount = self.platform_discount

        seller_discount = self.seller_discount

        cancel_reason = self.cancel_reason

        original_price = self.original_price

        rts_time = self.rts_time

        package_status = self.package_status

        currency = self.currency

        shipping_provider_name = self.shipping_provider_name

        cancel_user = self.cancel_user

        shipping_provider_id = self.shipping_provider_id

        item_tax: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.item_tax, Unset):
            item_tax = []
            for item_tax_item_data in self.item_tax:
                item_tax_item = item_tax_item_data.to_dict()
                item_tax.append(item_tax_item)

        tracking_number = self.tracking_number

        package_id = self.package_id

        retail_delivery_fee = self.retail_delivery_fee

        is_dangerous_good = self.is_dangerous_good

        warehouse_id = self.warehouse_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
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
        if platform_discount is not UNSET:
            field_dict["platform_discount"] = platform_discount
        if seller_discount is not UNSET:
            field_dict["seller_discount"] = seller_discount
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
        if item_tax is not UNSET:
            field_dict["item_tax"] = item_tax
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if retail_delivery_fee is not UNSET:
            field_dict["retail_delivery_fee"] = retail_delivery_fee
        if is_dangerous_good is not UNSET:
            field_dict["is_dangerous_good"] = is_dangerous_good
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_tax import ItemTax  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        display_status = d.pop("display_status", UNSET)

        product_name = d.pop("product_name", UNSET)

        seller_sku = d.pop("seller_sku", UNSET)

        sku_image = d.pop("sku_image", UNSET)

        sku_name = d.pop("sku_name", UNSET)

        product_id = d.pop("product_id", UNSET)

        sale_price = d.pop("sale_price", UNSET)

        platform_discount = d.pop("platform_discount", UNSET)

        seller_discount = d.pop("seller_discount", UNSET)

        cancel_reason = d.pop("cancel_reason", UNSET)

        original_price = d.pop("original_price", UNSET)

        rts_time = d.pop("rts_time", UNSET)

        package_status = d.pop("package_status", UNSET)

        currency = d.pop("currency", UNSET)

        shipping_provider_name = d.pop("shipping_provider_name", UNSET)

        cancel_user = d.pop("cancel_user", UNSET)

        shipping_provider_id = d.pop("shipping_provider_id", UNSET)

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

        is_dangerous_good = d.pop("is_dangerous_good", UNSET)

        warehouse_id = d.pop("warehouse_id", UNSET)

        sub_item_info = cls(
            id=id,
            sku_id=sku_id,
            display_status=display_status,
            product_name=product_name,
            seller_sku=seller_sku,
            sku_image=sku_image,
            sku_name=sku_name,
            product_id=product_id,
            sale_price=sale_price,
            platform_discount=platform_discount,
            seller_discount=seller_discount,
            cancel_reason=cancel_reason,
            original_price=original_price,
            rts_time=rts_time,
            package_status=package_status,
            currency=currency,
            shipping_provider_name=shipping_provider_name,
            cancel_user=cancel_user,
            shipping_provider_id=shipping_provider_id,
            item_tax=item_tax,
            tracking_number=tracking_number,
            package_id=package_id,
            retail_delivery_fee=retail_delivery_fee,
            is_dangerous_good=is_dangerous_good,
            warehouse_id=warehouse_id,
        )

        sub_item_info.additional_properties = d
        return sub_item_info

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
