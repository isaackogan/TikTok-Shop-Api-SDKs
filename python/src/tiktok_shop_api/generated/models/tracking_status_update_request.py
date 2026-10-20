from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tracking_status_update_request_track import TrackingStatusUpdateRequestTrack





T = TypeVar("T", bound="TrackingStatusUpdateRequest")



@_attrs_define
class TrackingStatusUpdateRequest:
    """ 
        Attributes:
            country (str): Order Country.
            order_id (str): TikTok Shop order ID.
            tracks (list[TrackingStatusUpdateRequestTrack]): Trajectory node array; maximum number of entries per single
                request [50], processing results are returned one by one within the array. That is, in the interface, a maximum
                of 50 tracks can be postbacked per order at a time.
            provider_id (str): The logistics provider ID, which is the one filled in when placing an order or uploading a
                tracking number, must be consistent with it.
            external_tracking_url (str | Unset): Service provider's track URL / official website link.
     """

    country: str
    order_id: str
    tracks: list[TrackingStatusUpdateRequestTrack]
    provider_id: str
    external_tracking_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tracking_status_update_request_track import TrackingStatusUpdateRequestTrack # noqa: PLC0415
        country = self.country

        order_id = self.order_id

        tracks = []
        for tracks_item_data in self.tracks:
            tracks_item = tracks_item_data.to_dict()
            tracks.append(tracks_item)



        provider_id = self.provider_id

        external_tracking_url = self.external_tracking_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "country": country,
            "order_id": order_id,
            "tracks": tracks,
            "provider_id": provider_id,
        })
        if external_tracking_url is not UNSET:
            field_dict["external_tracking_url"] = external_tracking_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracking_status_update_request_track import TrackingStatusUpdateRequestTrack # noqa: PLC0415
        d = dict(src_dict)
        country = d.pop("country")

        order_id = d.pop("order_id")

        tracks = []
        _tracks = d.pop("tracks")
        for tracks_item_data in (_tracks):
            tracks_item = TrackingStatusUpdateRequestTrack.from_dict(tracks_item_data)



            tracks.append(tracks_item)


        provider_id = d.pop("provider_id")

        external_tracking_url = d.pop("external_tracking_url", UNSET)

        tracking_status_update_request = cls(
            country=country,
            order_id=order_id,
            tracks=tracks,
            provider_id=provider_id,
            external_tracking_url=external_tracking_url,
        )


        tracking_status_update_request.additional_properties = d
        return tracking_status_update_request

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
