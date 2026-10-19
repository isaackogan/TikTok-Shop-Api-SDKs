from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ship_package_request_handover_method import ShipPackageRequestHandoverMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pickup_slot import PickupSlot
    from ..models.self_shipment import SelfShipment


T = TypeVar("T", bound="ShipPackageRequest")


@_attrs_define
class ShipPackageRequest:
    """
    Attributes:
        handover_method (ShipPackageRequestHandoverMethod | Unset): Possible values:
            - `PICKUP`: A logistics carrier will pick up the package(s) from the seller's pickup address.
            - `DROP_OFF`: The seller will need to drop off the package(s) to a designated location.
        pickup_slot (PickupSlot | Unset):
        self_shipment (SelfShipment | Unset):
    """

    handover_method: ShipPackageRequestHandoverMethod | Unset = UNSET
    pickup_slot: PickupSlot | Unset = UNSET
    self_shipment: SelfShipment | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        handover_method: str | Unset = UNSET
        if not isinstance(self.handover_method, Unset):
            handover_method = self.handover_method.value

        pickup_slot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pickup_slot, Unset):
            pickup_slot = self.pickup_slot.to_dict()

        self_shipment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.self_shipment, Unset):
            self_shipment = self.self_shipment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if handover_method is not UNSET:
            field_dict["handover_method"] = handover_method
        if pickup_slot is not UNSET:
            field_dict["pickup_slot"] = pickup_slot
        if self_shipment is not UNSET:
            field_dict["self_shipment"] = self_shipment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pickup_slot import PickupSlot  # noqa: PLC0415
        from ..models.self_shipment import SelfShipment  # noqa: PLC0415

        d = dict(src_dict)
        _handover_method = d.pop("handover_method", UNSET)
        handover_method: ShipPackageRequestHandoverMethod | Unset
        if isinstance(_handover_method, Unset):
            handover_method = UNSET
        else:
            handover_method = ShipPackageRequestHandoverMethod(_handover_method)

        _pickup_slot = d.pop("pickup_slot", UNSET)
        pickup_slot: PickupSlot | Unset
        if isinstance(_pickup_slot, Unset):
            pickup_slot = UNSET
        else:
            pickup_slot = PickupSlot.from_dict(_pickup_slot)

        _self_shipment = d.pop("self_shipment", UNSET)
        self_shipment: SelfShipment | Unset
        if isinstance(_self_shipment, Unset):
            self_shipment = UNSET
        else:
            self_shipment = SelfShipment.from_dict(_self_shipment)

        ship_package_request = cls(
            handover_method=handover_method,
            pickup_slot=pickup_slot,
            self_shipment=self_shipment,
        )

        ship_package_request.additional_properties = d
        return ship_package_request

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
