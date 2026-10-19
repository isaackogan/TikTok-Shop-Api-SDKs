from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePackagesResponseDataShippingServiceInfo")


@_attrs_define
class CreatePackagesResponseDataShippingServiceInfo:
    """
    Attributes:
        id (str | Unset): Shipping service ID.
        name (str | Unset): Shipping service name.
        price (str | Unset): Estimated price for this service.
        currency (str | Unset): Currency of the price.
        earliest_delivery_days (int | Unset): The minimum estimated duration required for package delivery.US only.
        latest_delivery_days (int | Unset): The maximum estimated duration required for package delivery.US only.
        shipping_provider_id (str | Unset): Shipping provider ID.US only.
        shipping_provider_name (str | Unset): Shipping provider name.US only.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    price: str | Unset = UNSET
    currency: str | Unset = UNSET
    earliest_delivery_days: int | Unset = UNSET
    latest_delivery_days: int | Unset = UNSET
    shipping_provider_id: str | Unset = UNSET
    shipping_provider_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        price = self.price

        currency = self.currency

        earliest_delivery_days = self.earliest_delivery_days

        latest_delivery_days = self.latest_delivery_days

        shipping_provider_id = self.shipping_provider_id

        shipping_provider_name = self.shipping_provider_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if earliest_delivery_days is not UNSET:
            field_dict["earliest_delivery_days"] = earliest_delivery_days
        if latest_delivery_days is not UNSET:
            field_dict["latest_delivery_days"] = latest_delivery_days
        if shipping_provider_id is not UNSET:
            field_dict["shipping_provider_id"] = shipping_provider_id
        if shipping_provider_name is not UNSET:
            field_dict["shipping_provider_name"] = shipping_provider_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        price = d.pop("price", UNSET)

        currency = d.pop("currency", UNSET)

        earliest_delivery_days = d.pop("earliest_delivery_days", UNSET)

        latest_delivery_days = d.pop("latest_delivery_days", UNSET)

        shipping_provider_id = d.pop("shipping_provider_id", UNSET)

        shipping_provider_name = d.pop("shipping_provider_name", UNSET)

        create_packages_response_data_shipping_service_info = cls(
            id=id,
            name=name,
            price=price,
            currency=currency,
            earliest_delivery_days=earliest_delivery_days,
            latest_delivery_days=latest_delivery_days,
            shipping_provider_id=shipping_provider_id,
            shipping_provider_name=shipping_provider_name,
        )

        create_packages_response_data_shipping_service_info.additional_properties = d
        return create_packages_response_data_shipping_service_info

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
