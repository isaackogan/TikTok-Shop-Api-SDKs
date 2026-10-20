from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FulfillmentType")


@_attrs_define
class FulfillmentType:
    """
    Attributes:
        handling_duration_days (int | Unset): The desired duration for handling a pre-sale order and handing it over to
            a shipping carrier.

            Applicable only for the following regions and pre-sale type:
            **US**
            - `MADE_TO_ORDER`: Business days, from 3 to 14 days.
            - `CUSTOM`: Business days, from 3 to 30 days.

            **UK, EU, SEA, JP, and LATAM**
            - `PRE_ORDER`: Calendar days, from 3 to 30 days.
        release_date (int | Unset): The date on which the product gets converted into a regular product and becomes
            available for general purchase. On this date, order handling will also start, changing the status of the order
            to [`AWAITING_SHIPMENT`](https://partner.tiktokshop.com/docv2/page/650b1b4bbace3e02b76d1011).

            Applicable only for `PRE_ORDER` in the US.
            **Note**:
            - Valid range: The date must fall within 3 - 60 days from the current date.
            - This date is a unix timestamp (seconds) based on the seller-selected timezone in Seller Center.
            - This date cannot be modified once the product goes live.
    """

    handling_duration_days: int | Unset = UNSET
    release_date: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        handling_duration_days = self.handling_duration_days

        release_date = self.release_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if handling_duration_days is not UNSET:
            field_dict["handling_duration_days"] = handling_duration_days
        if release_date is not UNSET:
            field_dict["release_date"] = release_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handling_duration_days = d.pop("handling_duration_days", UNSET)

        release_date = d.pop("release_date", UNSET)

        fulfillment_type = cls(
            handling_duration_days=handling_duration_days,
            release_date=release_date,
        )

        fulfillment_type.additional_properties = d
        return fulfillment_type

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
