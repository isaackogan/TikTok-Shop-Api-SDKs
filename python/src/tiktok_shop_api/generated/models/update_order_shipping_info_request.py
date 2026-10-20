from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpdateOrderShippingInfoRequest")



@_attrs_define
class UpdateOrderShippingInfoRequest:
    """ 
        Attributes:
            tracking_number (str): The shipment tracking number provided by the carrier. It must contain 4 to 50 characters
                consisting only of letters, numbers, hyphens (`-`), underscores (`_`), periods (`.`), or slashes (`/`).
            shipping_provider_id (str): Identifies the carrier that will deliver the package. Please call [Get Shipping
                Providers API](https://partner.tiktokshop.com/docv2/page/650aa48d4a0bb702c06d85cd?external_id=650aa48d4a0bb702c0
                6d85cd#Back%20To%20Top) to retrieve the available shipping provider(s).
     """

    tracking_number: str
    shipping_provider_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tracking_number = self.tracking_number

        shipping_provider_id = self.shipping_provider_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tracking_number": tracking_number,
            "shipping_provider_id": shipping_provider_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tracking_number = d.pop("tracking_number")

        shipping_provider_id = d.pop("shipping_provider_id")

        update_order_shipping_info_request = cls(
            tracking_number=tracking_number,
            shipping_provider_id=shipping_provider_id,
        )


        update_order_shipping_info_request.additional_properties = d
        return update_order_shipping_info_request

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
