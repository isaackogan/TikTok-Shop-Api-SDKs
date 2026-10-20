from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_logistics_tracking_response_data_logistics_detail_track_list import GetLogisticsTrackingResponseDataLogisticsDetailTrackList





T = TypeVar("T", bound="GetLogisticsTrackingResponseDataLogisticsDetail")



@_attrs_define
class GetLogisticsTrackingResponseDataLogisticsDetail:
    """ 
        Attributes:
            newest_tracking_no (str | Unset): The latest logistics tracking number for this parcel.
            carrier_name (str | Unset): The carrier name.
            track_list (list[GetLogisticsTrackingResponseDataLogisticsDetailTrackList] | Unset): A list of logistics
                tracking events for this parcel.
     """

    newest_tracking_no: str | Unset = UNSET
    carrier_name: str | Unset = UNSET
    track_list: list[GetLogisticsTrackingResponseDataLogisticsDetailTrackList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_logistics_tracking_response_data_logistics_detail_track_list import GetLogisticsTrackingResponseDataLogisticsDetailTrackList # noqa: PLC0415
        newest_tracking_no = self.newest_tracking_no

        carrier_name = self.carrier_name

        track_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.track_list, Unset):
            track_list = []
            for track_list_item_data in self.track_list:
                track_list_item = track_list_item_data.to_dict()
                track_list.append(track_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if newest_tracking_no is not UNSET:
            field_dict["newest_tracking_no"] = newest_tracking_no
        if carrier_name is not UNSET:
            field_dict["carrier_name"] = carrier_name
        if track_list is not UNSET:
            field_dict["track_list"] = track_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_logistics_tracking_response_data_logistics_detail_track_list import GetLogisticsTrackingResponseDataLogisticsDetailTrackList # noqa: PLC0415
        d = dict(src_dict)
        newest_tracking_no = d.pop("newest_tracking_no", UNSET)

        carrier_name = d.pop("carrier_name", UNSET)

        _track_list = d.pop("track_list", UNSET)
        track_list: list[GetLogisticsTrackingResponseDataLogisticsDetailTrackList] | Unset = UNSET
        if _track_list is not UNSET:
            track_list = []
            for track_list_item_data in _track_list:
                track_list_item = GetLogisticsTrackingResponseDataLogisticsDetailTrackList.from_dict(track_list_item_data)



                track_list.append(track_list_item)


        get_logistics_tracking_response_data_logistics_detail = cls(
            newest_tracking_no=newest_tracking_no,
            carrier_name=carrier_name,
            track_list=track_list,
        )


        get_logistics_tracking_response_data_logistics_detail.additional_properties = d
        return get_logistics_tracking_response_data_logistics_detail

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
