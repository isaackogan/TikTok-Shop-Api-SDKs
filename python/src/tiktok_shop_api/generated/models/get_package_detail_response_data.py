from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_package_detail_response_data_handover_method import GetPackageDetailResponseDataHandoverMethod
from ..models.get_package_detail_response_data_note_tag import GetPackageDetailResponseDataNoteTag
from ..models.get_package_detail_response_data_package_status import GetPackageDetailResponseDataPackageStatus
from ..models.get_package_detail_response_data_package_sub_status import GetPackageDetailResponseDataPackageSubStatus
from ..models.get_package_detail_response_data_shipping_type import GetPackageDetailResponseDataShippingType
from ..models.get_package_detail_response_data_split_and_combine_tag import (
    GetPackageDetailResponseDataSplitAndCombineTag,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dimension import Dimension
    from ..models.get_package_detail_response_data_insurance import GetPackageDetailResponseDataInsurance
    from ..models.get_package_detail_response_data_recipient_address import GetPackageDetailResponseDataRecipientAddress
    from ..models.get_package_detail_response_data_sender_address import GetPackageDetailResponseDataSenderAddress
    from ..models.order import Order
    from ..models.pickup_slot import PickupSlot
    from ..models.weight import Weight


T = TypeVar("T", bound="GetPackageDetailResponseData")


@_attrs_define
class GetPackageDetailResponseData:
    """
    Attributes:
        package_id (str | Unset): TikTok Shop package ID.
        orders (list[Order] | Unset): The response list of TikTok Shop orders.
        package_status (GetPackageDetailResponseDataPackageStatus | Unset): Possible values:
            - `TO_FULFILL`：Waiting for the merchant or warehouse to ship the package.
            - `PROCESSING`: Package has been arranged by seller. Waiting for carrier to collect the parcel.
            - `FULFILLING`: Package has been collected by carrier and in transit.
            - `COMPLETED`: Package has been delivered.
            - `CANCELLED`: Package has been canceled. Normally, the package is canceled due to the package being lost or
            damaged.
        package_sub_status (GetPackageDetailResponseDataPackageSubStatus | Unset): Package sub-status.
            Possible values:
            - `CREATED`: The package has been created.
            - `ISSUE`: Package allocation failed; contact platform support.
            - `STOCKING`: Platform verification is complete and the package is waiting for the seller to ship it.
            - `RTSING`: The shipping label is being purchased and the carrier result is pending.
            - `HBW`: For FBT orders only; the package has been created in the warehouse.
            - `HBWING`: For FBT orders only; the package is being created in the warehouse.
            - `TSP_PENDING`: Authorization for third-party service-provider fulfillment is pending.
            - `RTS`: The shipping label has been purchased and the seller can print it.
            - `TTS`: The carrier has picked up the package.
            - `DELIVERED`: The package has been delivered to the buyer.
            - `SHIP_EXCEPTION`: The package cannot be delivered, for example because it is damaged or lost. See
            `ship_exception_reason` for the detailed reason.
            - `PART_DELIVERED_AND_EXCEPTION`: Part of the package delivery completed and another part encountered a shipping
            exception.
            - `CANCELLED`: The package has been canceled.
        ship_exception_reason (str | Unset): -PACKAGE_DAMAGAED
            -PACKAGE_LOST
            -RETURNED_TO_SHIPPER
            -PACKAGE_SCRAP
        split_and_combine_tag (GetPackageDetailResponseDataSplitAndCombineTag | Unset): Possible values:
            - `DEFAULT`: The package has not undergone any combine or split operation.
            - `COMBINE`: The package has been consolidated with another order.
            - `SPLIT`: The order has been split into multiple orders.
        has_multi_skus (bool | Unset): Whether there are multiple SKU IDs in a package.
        note_tag (GetPackageDetailResponseDataNoteTag | Unset): Possible values:
            - `BUYER_UNNOTED`: The order has not been noted by buyer.
            - `BUYER_NOTED`: The order has been noted by buyer.
        shipping_provider_name (str | Unset): Package shipping provider name.
        shipping_provider_id (str | Unset): Package shipping provider ID.
        shipping_type (GetPackageDetailResponseDataShippingType | Unset): Indicates who provides the shipping service.
            Possible values:
            - `TIKTOK`: Shipping service provided by TikTok. The seller should obtain a shipping label from TikTok.
            - `SELLER`: Seller provides shipping, including through a third-party fulfillment provider acting on the
            seller's behalf.
        delivery_option_name (str | Unset): Delivery option name. For display purposes only.
        delivery_option_id (str | Unset): Order delivery option ID. Delivery option ID is mapped to seller configured
            logistics templates ID.
        tracking_number (str | Unset): Package tracking number.
        last_mile_tracking_number (str | Unset): For cross-border order only. Cross-border order last mile tracking
            number.
        pickup_slot (PickupSlot | Unset):
        create_time (int | Unset): Package creation time. Unix timestamp, in seconds.
        handover_method (GetPackageDetailResponseDataHandoverMethod | Unset): Whether the package is delivered by pick
            up or drop off. Possible values:
            - `PICKUP`: A Logistics carrier will pickup the package(s) from the seller's pickup address.
            - `DROP_OFF`: Seller will need to drop off the package(s) to a designated location.
        order_line_item_ids (list[str] | Unset): The order line item ID contained in the package.
        recipient_address (GetPackageDetailResponseDataRecipientAddress | Unset):
        sender_address (GetPackageDetailResponseDataSenderAddress | Unset):
        weight (Weight | Unset):
        dimension (Dimension | Unset):
        update_time (int | Unset): The time when the package was last updated, as a Unix timestamp in seconds.
        insurance (GetPackageDetailResponseDataInsurance | Unset):
        biz_extension_tags (list[str] | Unset): Special tags for current package if any.
            - `NON_MCF`: whether this package was shipped as a MCF order while in fact it is not.
        warehouse_id (str | Unset): Seller Warehouse id for this package
    """

    package_id: str | Unset = UNSET
    orders: list[Order] | Unset = UNSET
    package_status: GetPackageDetailResponseDataPackageStatus | Unset = UNSET
    package_sub_status: GetPackageDetailResponseDataPackageSubStatus | Unset = UNSET
    ship_exception_reason: str | Unset = UNSET
    split_and_combine_tag: GetPackageDetailResponseDataSplitAndCombineTag | Unset = UNSET
    has_multi_skus: bool | Unset = UNSET
    note_tag: GetPackageDetailResponseDataNoteTag | Unset = UNSET
    shipping_provider_name: str | Unset = UNSET
    shipping_provider_id: str | Unset = UNSET
    shipping_type: GetPackageDetailResponseDataShippingType | Unset = UNSET
    delivery_option_name: str | Unset = UNSET
    delivery_option_id: str | Unset = UNSET
    tracking_number: str | Unset = UNSET
    last_mile_tracking_number: str | Unset = UNSET
    pickup_slot: PickupSlot | Unset = UNSET
    create_time: int | Unset = UNSET
    handover_method: GetPackageDetailResponseDataHandoverMethod | Unset = UNSET
    order_line_item_ids: list[str] | Unset = UNSET
    recipient_address: GetPackageDetailResponseDataRecipientAddress | Unset = UNSET
    sender_address: GetPackageDetailResponseDataSenderAddress | Unset = UNSET
    weight: Weight | Unset = UNSET
    dimension: Dimension | Unset = UNSET
    update_time: int | Unset = UNSET
    insurance: GetPackageDetailResponseDataInsurance | Unset = UNSET
    biz_extension_tags: list[str] | Unset = UNSET
    warehouse_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_id = self.package_id

        orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        package_status: str | Unset = UNSET
        if not isinstance(self.package_status, Unset):
            package_status = self.package_status.value

        package_sub_status: str | Unset = UNSET
        if not isinstance(self.package_sub_status, Unset):
            package_sub_status = self.package_sub_status.value

        ship_exception_reason = self.ship_exception_reason

        split_and_combine_tag: str | Unset = UNSET
        if not isinstance(self.split_and_combine_tag, Unset):
            split_and_combine_tag = self.split_and_combine_tag.value

        has_multi_skus = self.has_multi_skus

        note_tag: str | Unset = UNSET
        if not isinstance(self.note_tag, Unset):
            note_tag = self.note_tag.value

        shipping_provider_name = self.shipping_provider_name

        shipping_provider_id = self.shipping_provider_id

        shipping_type: str | Unset = UNSET
        if not isinstance(self.shipping_type, Unset):
            shipping_type = self.shipping_type.value

        delivery_option_name = self.delivery_option_name

        delivery_option_id = self.delivery_option_id

        tracking_number = self.tracking_number

        last_mile_tracking_number = self.last_mile_tracking_number

        pickup_slot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pickup_slot, Unset):
            pickup_slot = self.pickup_slot.to_dict()

        create_time = self.create_time

        handover_method: str | Unset = UNSET
        if not isinstance(self.handover_method, Unset):
            handover_method = self.handover_method.value

        order_line_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_line_item_ids, Unset):
            order_line_item_ids = self.order_line_item_ids

        recipient_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recipient_address, Unset):
            recipient_address = self.recipient_address.to_dict()

        sender_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sender_address, Unset):
            sender_address = self.sender_address.to_dict()

        weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimension, Unset):
            dimension = self.dimension.to_dict()

        update_time = self.update_time

        insurance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insurance, Unset):
            insurance = self.insurance.to_dict()

        biz_extension_tags: list[str] | Unset = UNSET
        if not isinstance(self.biz_extension_tags, Unset):
            biz_extension_tags = self.biz_extension_tags

        warehouse_id = self.warehouse_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if orders is not UNSET:
            field_dict["orders"] = orders
        if package_status is not UNSET:
            field_dict["package_status"] = package_status
        if package_sub_status is not UNSET:
            field_dict["package_sub_status"] = package_sub_status
        if ship_exception_reason is not UNSET:
            field_dict["ship_exception_reason"] = ship_exception_reason
        if split_and_combine_tag is not UNSET:
            field_dict["split_and_combine_tag"] = split_and_combine_tag
        if has_multi_skus is not UNSET:
            field_dict["has_multi_skus"] = has_multi_skus
        if note_tag is not UNSET:
            field_dict["note_tag"] = note_tag
        if shipping_provider_name is not UNSET:
            field_dict["shipping_provider_name"] = shipping_provider_name
        if shipping_provider_id is not UNSET:
            field_dict["shipping_provider_id"] = shipping_provider_id
        if shipping_type is not UNSET:
            field_dict["shipping_type"] = shipping_type
        if delivery_option_name is not UNSET:
            field_dict["delivery_option_name"] = delivery_option_name
        if delivery_option_id is not UNSET:
            field_dict["delivery_option_id"] = delivery_option_id
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if last_mile_tracking_number is not UNSET:
            field_dict["last_mile_tracking_number"] = last_mile_tracking_number
        if pickup_slot is not UNSET:
            field_dict["pickup_slot"] = pickup_slot
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if handover_method is not UNSET:
            field_dict["handover_method"] = handover_method
        if order_line_item_ids is not UNSET:
            field_dict["order_line_item_ids"] = order_line_item_ids
        if recipient_address is not UNSET:
            field_dict["recipient_address"] = recipient_address
        if sender_address is not UNSET:
            field_dict["sender_address"] = sender_address
        if weight is not UNSET:
            field_dict["weight"] = weight
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if insurance is not UNSET:
            field_dict["insurance"] = insurance
        if biz_extension_tags is not UNSET:
            field_dict["biz_extension_tags"] = biz_extension_tags
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension  # noqa: PLC0415
        from ..models.get_package_detail_response_data_insurance import (
            GetPackageDetailResponseDataInsurance,  # noqa: PLC0415
        )
        from ..models.get_package_detail_response_data_recipient_address import (
            GetPackageDetailResponseDataRecipientAddress,  # noqa: PLC0415
        )
        from ..models.get_package_detail_response_data_sender_address import (
            GetPackageDetailResponseDataSenderAddress,  # noqa: PLC0415
        )
        from ..models.order import Order  # noqa: PLC0415
        from ..models.pickup_slot import PickupSlot  # noqa: PLC0415
        from ..models.weight import Weight  # noqa: PLC0415

        d = dict(src_dict)
        package_id = d.pop("package_id", UNSET)

        _orders = d.pop("orders", UNSET)
        orders: list[Order] | Unset = UNSET
        if _orders is not UNSET:
            orders = []
            for orders_item_data in _orders:
                orders_item = Order.from_dict(orders_item_data)

                orders.append(orders_item)

        _package_status = d.pop("package_status", UNSET)
        package_status: GetPackageDetailResponseDataPackageStatus | Unset
        if isinstance(_package_status, Unset):
            package_status = UNSET
        else:
            package_status = GetPackageDetailResponseDataPackageStatus(_package_status)

        _package_sub_status = d.pop("package_sub_status", UNSET)
        package_sub_status: GetPackageDetailResponseDataPackageSubStatus | Unset
        if isinstance(_package_sub_status, Unset):
            package_sub_status = UNSET
        else:
            package_sub_status = GetPackageDetailResponseDataPackageSubStatus(_package_sub_status)

        ship_exception_reason = d.pop("ship_exception_reason", UNSET)

        _split_and_combine_tag = d.pop("split_and_combine_tag", UNSET)
        split_and_combine_tag: GetPackageDetailResponseDataSplitAndCombineTag | Unset
        if isinstance(_split_and_combine_tag, Unset):
            split_and_combine_tag = UNSET
        else:
            split_and_combine_tag = GetPackageDetailResponseDataSplitAndCombineTag(_split_and_combine_tag)

        has_multi_skus = d.pop("has_multi_skus", UNSET)

        _note_tag = d.pop("note_tag", UNSET)
        note_tag: GetPackageDetailResponseDataNoteTag | Unset
        if isinstance(_note_tag, Unset):
            note_tag = UNSET
        else:
            note_tag = GetPackageDetailResponseDataNoteTag(_note_tag)

        shipping_provider_name = d.pop("shipping_provider_name", UNSET)

        shipping_provider_id = d.pop("shipping_provider_id", UNSET)

        _shipping_type = d.pop("shipping_type", UNSET)
        shipping_type: GetPackageDetailResponseDataShippingType | Unset
        if isinstance(_shipping_type, Unset):
            shipping_type = UNSET
        else:
            shipping_type = GetPackageDetailResponseDataShippingType(_shipping_type)

        delivery_option_name = d.pop("delivery_option_name", UNSET)

        delivery_option_id = d.pop("delivery_option_id", UNSET)

        tracking_number = d.pop("tracking_number", UNSET)

        last_mile_tracking_number = d.pop("last_mile_tracking_number", UNSET)

        _pickup_slot = d.pop("pickup_slot", UNSET)
        pickup_slot: PickupSlot | Unset
        if isinstance(_pickup_slot, Unset):
            pickup_slot = UNSET
        else:
            pickup_slot = PickupSlot.from_dict(_pickup_slot)

        create_time = d.pop("create_time", UNSET)

        _handover_method = d.pop("handover_method", UNSET)
        handover_method: GetPackageDetailResponseDataHandoverMethod | Unset
        if isinstance(_handover_method, Unset):
            handover_method = UNSET
        else:
            handover_method = GetPackageDetailResponseDataHandoverMethod(_handover_method)

        order_line_item_ids = cast(list[str], d.pop("order_line_item_ids", UNSET))

        _recipient_address = d.pop("recipient_address", UNSET)
        recipient_address: GetPackageDetailResponseDataRecipientAddress | Unset
        if isinstance(_recipient_address, Unset):
            recipient_address = UNSET
        else:
            recipient_address = GetPackageDetailResponseDataRecipientAddress.from_dict(_recipient_address)

        _sender_address = d.pop("sender_address", UNSET)
        sender_address: GetPackageDetailResponseDataSenderAddress | Unset
        if isinstance(_sender_address, Unset):
            sender_address = UNSET
        else:
            sender_address = GetPackageDetailResponseDataSenderAddress.from_dict(_sender_address)

        _weight = d.pop("weight", UNSET)
        weight: Weight | Unset
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = Weight.from_dict(_weight)

        _dimension = d.pop("dimension", UNSET)
        dimension: Dimension | Unset
        if isinstance(_dimension, Unset):
            dimension = UNSET
        else:
            dimension = Dimension.from_dict(_dimension)

        update_time = d.pop("update_time", UNSET)

        _insurance = d.pop("insurance", UNSET)
        insurance: GetPackageDetailResponseDataInsurance | Unset
        if isinstance(_insurance, Unset):
            insurance = UNSET
        else:
            insurance = GetPackageDetailResponseDataInsurance.from_dict(_insurance)

        biz_extension_tags = cast(list[str], d.pop("biz_extension_tags", UNSET))

        warehouse_id = d.pop("warehouse_id", UNSET)

        get_package_detail_response_data = cls(
            package_id=package_id,
            orders=orders,
            package_status=package_status,
            package_sub_status=package_sub_status,
            ship_exception_reason=ship_exception_reason,
            split_and_combine_tag=split_and_combine_tag,
            has_multi_skus=has_multi_skus,
            note_tag=note_tag,
            shipping_provider_name=shipping_provider_name,
            shipping_provider_id=shipping_provider_id,
            shipping_type=shipping_type,
            delivery_option_name=delivery_option_name,
            delivery_option_id=delivery_option_id,
            tracking_number=tracking_number,
            last_mile_tracking_number=last_mile_tracking_number,
            pickup_slot=pickup_slot,
            create_time=create_time,
            handover_method=handover_method,
            order_line_item_ids=order_line_item_ids,
            recipient_address=recipient_address,
            sender_address=sender_address,
            weight=weight,
            dimension=dimension,
            update_time=update_time,
            insurance=insurance,
            biz_extension_tags=biz_extension_tags,
            warehouse_id=warehouse_id,
        )

        get_package_detail_response_data.additional_properties = d
        return get_package_detail_response_data

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
