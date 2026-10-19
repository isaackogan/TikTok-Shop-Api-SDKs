from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SelfShipment")


@_attrs_define
class SelfShipment:
    """
    Attributes:
        tracking_number (str): For packages with the `SEND_BY_SELLER` delivery option type (seller shipping), you must
            provide the package's tracking number.
        shipping_provider_id (str): For packages with the `SEND_BY_SELLER` delivery option type (seller shipping), you
            must provide the shipping provider information. Please use the [Get Shipping Providers](https://partner.tiktoksh
            op.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c06d85cd#Back%20To%20Top) API to obtain
            the `shipping_provider_id`.
    """

    tracking_number: str
    shipping_provider_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tracking_number = self.tracking_number

        shipping_provider_id = self.shipping_provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tracking_number": tracking_number,
                "shipping_provider_id": shipping_provider_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tracking_number = d.pop("tracking_number")

        shipping_provider_id = d.pop("shipping_provider_id")

        self_shipment = cls(
            tracking_number=tracking_number,
            shipping_provider_id=shipping_provider_id,
        )

        self_shipment.additional_properties = d
        return self_shipment

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
