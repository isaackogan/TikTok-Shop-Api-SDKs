from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpdateInboundOrderTrackingRequestParcelTrackingInfo")



@_attrs_define
class UpdateInboundOrderTrackingRequestParcelTrackingInfo:
    """ 
        Attributes:
            provider_name (str): The `provider_name` field must contain exactly one of the following strings.

                * `FEDEX` (Federal Express)
                * `UPS` (United Parcel Service)
                * `DHL` (DHL Express)
                * `USPS` (United States Postal Service)
                * `OTHER` (All other logistics providers)

                **Note:** Input must match the uppercase string exactly (e.g., `"provider_name": "FEDEX"`).
            tracking_number (str): The tracking number to associate with this carton. It must not be empty or contain only
                whitespace, and it may contain only ASCII letters, digits, spaces, and hyphens. After spaces and hyphens are
                removed, 8 to 40 letters or digits must remain.
            carton_number (str): The carton number of an existing carton in this inbound order. After leading and trailing
                whitespace is removed, this value is matched to the carton whose tracking information is created or replaced.
     """

    provider_name: str
    tracking_number: str
    carton_number: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        provider_name = self.provider_name

        tracking_number = self.tracking_number

        carton_number = self.carton_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "provider_name": provider_name,
            "tracking_number": tracking_number,
            "carton_number": carton_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_name = d.pop("provider_name")

        tracking_number = d.pop("tracking_number")

        carton_number = d.pop("carton_number")

        update_inbound_order_tracking_request_parcel_tracking_info = cls(
            provider_name=provider_name,
            tracking_number=tracking_number,
            carton_number=carton_number,
        )


        update_inbound_order_tracking_request_parcel_tracking_info.additional_properties = d
        return update_inbound_order_tracking_request_parcel_tracking_info

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
