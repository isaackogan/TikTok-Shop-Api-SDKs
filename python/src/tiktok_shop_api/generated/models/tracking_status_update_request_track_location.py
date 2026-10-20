from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TrackingStatusUpdateRequestTrackLocation")



@_attrs_define
class TrackingStatusUpdateRequestTrackLocation:
    """ 
        Attributes:
            country (str | Unset): country.
            state (str | Unset): state.
            city (str | Unset): city.
            zip_code (str | Unset): zip code/post code.
     """

    country: str | Unset = UNSET
    state: str | Unset = UNSET
    city: str | Unset = UNSET
    zip_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        country = self.country

        state = self.state

        city = self.city

        zip_code = self.zip_code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if country is not UNSET:
            field_dict["country"] = country
        if state is not UNSET:
            field_dict["state"] = state
        if city is not UNSET:
            field_dict["city"] = city
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country = d.pop("country", UNSET)

        state = d.pop("state", UNSET)

        city = d.pop("city", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        tracking_status_update_request_track_location = cls(
            country=country,
            state=state,
            city=city,
            zip_code=zip_code,
        )


        tracking_status_update_request_track_location.additional_properties = d
        return tracking_status_update_request_track_location

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
