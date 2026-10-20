from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFBTInboundOrderDetailsResponseDataInboundOrderStatusLog")


@_attrs_define
class GetFBTInboundOrderDetailsResponseDataInboundOrderStatusLog:
    """
    Attributes:
        operate_time (int | Unset): The time when the inbound order is processed by the merchant or warehouses,
            represented as a Unix timestamp in seconds.
        new_status (str | Unset): The order status in **Fulfilled by TikTok (FBT)** warehouse after this operation.

            **Possible values:**
            * `WORKING`
            * `READY_TO_SHIP`
            * `TO_BE_RECEIVED`
            * `ARRIVED_HUB`
            * `INTERNAL_TRANSFER`
            * `RECEIVING`
            * `PARTIALLY_RECEIVED`
            * `RECEIVED`
            * `CANCELLED`
            * `DELIVERED`
        previous_status (str | Unset): The order status in **Fulfilled by TikTok (FBT)** warehouse before this
            operation.

            **Possible values:**
            * `WORKING`
            * `READY_TO_SHIP`
            * `TO_BE_RECEIVED`
            * `ARRIVED_HUB`
            * `INTERNAL_TRANSFER`
            * `RECEIVING`
            * `PARTIALLY_RECEIVED`
            * `RECEIVED`
            * `CANCELLED`
            * `DELIVERED`
        operator (str | Unset): The unique identifier or name of the user or system entity that performed the status
            change.
    """

    operate_time: int | Unset = UNSET
    new_status: str | Unset = UNSET
    previous_status: str | Unset = UNSET
    operator: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operate_time = self.operate_time

        new_status = self.new_status

        previous_status = self.previous_status

        operator = self.operator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operate_time is not UNSET:
            field_dict["operate_time"] = operate_time
        if new_status is not UNSET:
            field_dict["new_status"] = new_status
        if previous_status is not UNSET:
            field_dict["previous_status"] = previous_status
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operate_time = d.pop("operate_time", UNSET)

        new_status = d.pop("new_status", UNSET)

        previous_status = d.pop("previous_status", UNSET)

        operator = d.pop("operator", UNSET)

        get_fbt_inbound_order_details_response_data_inbound_order_status_log = cls(
            operate_time=operate_time,
            new_status=new_status,
            previous_status=previous_status,
            operator=operator,
        )

        get_fbt_inbound_order_details_response_data_inbound_order_status_log.additional_properties = d
        return get_fbt_inbound_order_details_response_data_inbound_order_status_log

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
