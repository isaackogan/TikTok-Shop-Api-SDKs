from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_package_handover_time_slots_response_data_pickup_slot import GetPackageHandoverTimeSlotsResponseDataPickupSlot





T = TypeVar("T", bound="GetPackageHandoverTimeSlotsResponseData")



@_attrs_define
class GetPackageHandoverTimeSlotsResponseData:
    """ 
        Attributes:
            can_pickup (bool | Unset): Whether this package supports door-to-door collection.
            can_drop_off (bool | Unset): Whether this package be dropped off at a drop-off location
            can_van_collection (bool | Unset): Specific to UK. Use this field to determine whether van collection is
                available.
            drop_off_point_url (str | Unset): View package drop-off locations  via provided URL.
            pickup_slots (list[GetPackageHandoverTimeSlotsResponseDataPickupSlot] | Unset): Door-to-door collection time
                slots. Check `avaliable` to determine whether each time slot can be scheduled.
     """

    can_pickup: bool | Unset = UNSET
    can_drop_off: bool | Unset = UNSET
    can_van_collection: bool | Unset = UNSET
    drop_off_point_url: str | Unset = UNSET
    pickup_slots: list[GetPackageHandoverTimeSlotsResponseDataPickupSlot] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_package_handover_time_slots_response_data_pickup_slot import GetPackageHandoverTimeSlotsResponseDataPickupSlot # noqa: PLC0415
        can_pickup = self.can_pickup

        can_drop_off = self.can_drop_off

        can_van_collection = self.can_van_collection

        drop_off_point_url = self.drop_off_point_url

        pickup_slots: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pickup_slots, Unset):
            pickup_slots = []
            for pickup_slots_item_data in self.pickup_slots:
                pickup_slots_item = pickup_slots_item_data.to_dict()
                pickup_slots.append(pickup_slots_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if can_pickup is not UNSET:
            field_dict["can_pickup"] = can_pickup
        if can_drop_off is not UNSET:
            field_dict["can_drop_off"] = can_drop_off
        if can_van_collection is not UNSET:
            field_dict["can_van_collection"] = can_van_collection
        if drop_off_point_url is not UNSET:
            field_dict["drop_off_point_url"] = drop_off_point_url
        if pickup_slots is not UNSET:
            field_dict["pickup_slots"] = pickup_slots

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_package_handover_time_slots_response_data_pickup_slot import GetPackageHandoverTimeSlotsResponseDataPickupSlot # noqa: PLC0415
        d = dict(src_dict)
        can_pickup = d.pop("can_pickup", UNSET)

        can_drop_off = d.pop("can_drop_off", UNSET)

        can_van_collection = d.pop("can_van_collection", UNSET)

        drop_off_point_url = d.pop("drop_off_point_url", UNSET)

        _pickup_slots = d.pop("pickup_slots", UNSET)
        pickup_slots: list[GetPackageHandoverTimeSlotsResponseDataPickupSlot] | Unset = UNSET
        if _pickup_slots is not UNSET:
            pickup_slots = []
            for pickup_slots_item_data in _pickup_slots:
                pickup_slots_item = GetPackageHandoverTimeSlotsResponseDataPickupSlot.from_dict(pickup_slots_item_data)



                pickup_slots.append(pickup_slots_item)


        get_package_handover_time_slots_response_data = cls(
            can_pickup=can_pickup,
            can_drop_off=can_drop_off,
            can_van_collection=can_van_collection,
            drop_off_point_url=drop_off_point_url,
            pickup_slots=pickup_slots,
        )


        get_package_handover_time_slots_response_data.additional_properties = d
        return get_package_handover_time_slots_response_data

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
