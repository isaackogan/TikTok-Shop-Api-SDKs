from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_inbound_method_detail_response_data_info_allocation_shipment import (
        GetInboundMethodDetailResponseDataInfoAllocationShipment,
    )
    from ..models.get_inbound_method_detail_response_data_info_placement_fee_estimate import (
        GetInboundMethodDetailResponseDataInfoPlacementFeeEstimate,
    )


T = TypeVar("T", bound="GetInboundMethodDetailResponseDataInfo")


@_attrs_define
class GetInboundMethodDetailResponseDataInfo:
    """
    Attributes:
        allocation_shipments (list[GetInboundMethodDetailResponseDataInfoAllocationShipment] | Unset): List of shipments
            for this placement option.
        placement_option_id (str | Unset): Placement option id. A placement option represents the shipment splits and
            destinations.
        placement_fee_estimate (GetInboundMethodDetailResponseDataInfoPlacementFeeEstimate | Unset):
    """

    allocation_shipments: list[GetInboundMethodDetailResponseDataInfoAllocationShipment] | Unset = UNSET
    placement_option_id: str | Unset = UNSET
    placement_fee_estimate: GetInboundMethodDetailResponseDataInfoPlacementFeeEstimate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocation_shipments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.allocation_shipments, Unset):
            allocation_shipments = []
            for allocation_shipments_item_data in self.allocation_shipments:
                allocation_shipments_item = allocation_shipments_item_data.to_dict()
                allocation_shipments.append(allocation_shipments_item)

        placement_option_id = self.placement_option_id

        placement_fee_estimate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.placement_fee_estimate, Unset):
            placement_fee_estimate = self.placement_fee_estimate.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocation_shipments is not UNSET:
            field_dict["allocation_shipments"] = allocation_shipments
        if placement_option_id is not UNSET:
            field_dict["placement_option_id"] = placement_option_id
        if placement_fee_estimate is not UNSET:
            field_dict["placement_fee_estimate"] = placement_fee_estimate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_inbound_method_detail_response_data_info_allocation_shipment import (
            GetInboundMethodDetailResponseDataInfoAllocationShipment,  # noqa: PLC0415
        )
        from ..models.get_inbound_method_detail_response_data_info_placement_fee_estimate import (
            GetInboundMethodDetailResponseDataInfoPlacementFeeEstimate,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _allocation_shipments = d.pop("allocation_shipments", UNSET)
        allocation_shipments: list[GetInboundMethodDetailResponseDataInfoAllocationShipment] | Unset = UNSET
        if _allocation_shipments is not UNSET:
            allocation_shipments = []
            for allocation_shipments_item_data in _allocation_shipments:
                allocation_shipments_item = GetInboundMethodDetailResponseDataInfoAllocationShipment.from_dict(
                    allocation_shipments_item_data
                )

                allocation_shipments.append(allocation_shipments_item)

        placement_option_id = d.pop("placement_option_id", UNSET)

        _placement_fee_estimate = d.pop("placement_fee_estimate", UNSET)
        placement_fee_estimate: GetInboundMethodDetailResponseDataInfoPlacementFeeEstimate | Unset
        if isinstance(_placement_fee_estimate, Unset):
            placement_fee_estimate = UNSET
        else:
            placement_fee_estimate = GetInboundMethodDetailResponseDataInfoPlacementFeeEstimate.from_dict(
                _placement_fee_estimate
            )

        get_inbound_method_detail_response_data_info = cls(
            allocation_shipments=allocation_shipments,
            placement_option_id=placement_option_id,
            placement_fee_estimate=placement_fee_estimate,
        )

        get_inbound_method_detail_response_data_info.additional_properties = d
        return get_inbound_method_detail_response_data_info

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
