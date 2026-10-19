from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cancel_fbtmcf_order_response_data_mcf_order_consign_order_status import (
    CancelFBTMCFOrderResponseDataMcfOrderConsignOrderStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelFBTMCFOrderResponseDataMcfOrderConsignOrder")


@_attrs_define
class CancelFBTMCFOrderResponseDataMcfOrderConsignOrder:
    """
    Attributes:
        id (str | Unset): The consign order ID, returned as a numeric string without the `OBF` prefix.
        status (CancelFBTMCFOrderResponseDataMcfOrderConsignOrderStatus | Unset): The current status of this consign
            order. In a cancellation response, `CLOSED` means that the consign order has been canceled.

            Possible Status Enumerations
            1. **PENDING** - Order is pending warehouse processing
            2. **HANDLE_BY_WAREHOUSE** - Order is being processed by the warehouse
            3. **SHIPPED** - Order has been shipped out from the warehouse
            4. **HANDOVER** - Order has been received by the logistics carrier and is in transit
            5. **CLOSED** - Order has been canceled
            6. **LOST** - Order is lost
            7. **DAMAGE** - Order is damaged
            8. **COMPLETED** - Order has been completed
            9. **ABNORMAL** - There is an issue related to this order and cannot be fulfilled
            10. **RETURNED** - Order has been returned
            11. **SCRAP** - Order has been scrapped
            12. **UNKNOWN** - Order status is unknown
    """

    id: str | Unset = UNSET
    status: CancelFBTMCFOrderResponseDataMcfOrderConsignOrderStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: CancelFBTMCFOrderResponseDataMcfOrderConsignOrderStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CancelFBTMCFOrderResponseDataMcfOrderConsignOrderStatus(_status)

        cancel_fbtmcf_order_response_data_mcf_order_consign_order = cls(
            id=id,
            status=status,
        )

        cancel_fbtmcf_order_response_data_mcf_order_consign_order.additional_properties = d
        return cancel_fbtmcf_order_response_data_mcf_order_consign_order

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
