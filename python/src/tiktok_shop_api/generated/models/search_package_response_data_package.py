from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_package_response_data_package_status import SearchPackageResponseDataPackageStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.order import Order


T = TypeVar("T", bound="SearchPackageResponseDataPackage")


@_attrs_define
class SearchPackageResponseDataPackage:
    """
    Attributes:
        id (str | Unset): Package ID.
        orders (list[Order] | Unset): The response list of TikTok Shop orders.
        create_time (int | Unset): Package creation time. Unix timestamp, in seconds.
        update_time (int | Unset): The time when the package was last updated. Unix timestamp, in seconds.
        status (SearchPackageResponseDataPackageStatus | Unset): Possible values:
            - `TO_FULFILL`
            - `PROCESSING`: Package has been arranged by seller. Waiting for carrier to collect the parcel.
            - `FULFILLING`: Package has been collected by carrier and in transit.
            - `COMPLETED`: Package has been delivered.
            - `CANCELLED`: Package has been canceled. Normally, the package is canceled due to the package being lost or
            damaged.
        tracking_number (str | Unset): Package tracking number.
        shipping_provider_name (str | Unset): Package shipping provider.
        shipping_provider_id (str | Unset): Package shipping provider ID.
        order_line_item_ids (list[str] | Unset): The order line item ID contained in the package.
    """

    id: str | Unset = UNSET
    orders: list[Order] | Unset = UNSET
    create_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    status: SearchPackageResponseDataPackageStatus | Unset = UNSET
    tracking_number: str | Unset = UNSET
    shipping_provider_name: str | Unset = UNSET
    shipping_provider_id: str | Unset = UNSET
    order_line_item_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        create_time = self.create_time

        update_time = self.update_time

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        tracking_number = self.tracking_number

        shipping_provider_name = self.shipping_provider_name

        shipping_provider_id = self.shipping_provider_id

        order_line_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_line_item_ids, Unset):
            order_line_item_ids = self.order_line_item_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if orders is not UNSET:
            field_dict["orders"] = orders
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if status is not UNSET:
            field_dict["status"] = status
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if shipping_provider_name is not UNSET:
            field_dict["shipping_provider_name"] = shipping_provider_name
        if shipping_provider_id is not UNSET:
            field_dict["shipping_provider_id"] = shipping_provider_id
        if order_line_item_ids is not UNSET:
            field_dict["order_line_item_ids"] = order_line_item_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order import Order  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _orders = d.pop("orders", UNSET)
        orders: list[Order] | Unset = UNSET
        if _orders is not UNSET:
            orders = []
            for orders_item_data in _orders:
                orders_item = Order.from_dict(orders_item_data)

                orders.append(orders_item)

        create_time = d.pop("create_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        _status = d.pop("status", UNSET)
        status: SearchPackageResponseDataPackageStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SearchPackageResponseDataPackageStatus(_status)

        tracking_number = d.pop("tracking_number", UNSET)

        shipping_provider_name = d.pop("shipping_provider_name", UNSET)

        shipping_provider_id = d.pop("shipping_provider_id", UNSET)

        order_line_item_ids = cast(list[str], d.pop("order_line_item_ids", UNSET))

        search_package_response_data_package = cls(
            id=id,
            orders=orders,
            create_time=create_time,
            update_time=update_time,
            status=status,
            tracking_number=tracking_number,
            shipping_provider_name=shipping_provider_name,
            shipping_provider_id=shipping_provider_id,
            order_line_item_ids=order_line_item_ids,
        )

        search_package_response_data_package.additional_properties = d
        return search_package_response_data_package

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
