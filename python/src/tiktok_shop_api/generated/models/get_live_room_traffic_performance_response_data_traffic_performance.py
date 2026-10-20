from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_live_room_traffic_performance_response_data_traffic_performance_source import GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSource
  from ..models.get_live_room_traffic_performance_response_data_traffic_performance_sub_source import GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSubSource





T = TypeVar("T", bound="GetLiveRoomTrafficPerformanceResponseDataTrafficPerformance")



@_attrs_define
class GetLiveRoomTrafficPerformanceResponseDataTrafficPerformance:
    """ 
        Attributes:
            source (GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSource | Unset):
            sub_sources (list[GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSubSource] | Unset): Traffic sub-
                sources associated with the primary traffic source, when available.
     """

    source: GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSource | Unset = UNSET
    sub_sources: list[GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSubSource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_live_room_traffic_performance_response_data_traffic_performance_source import GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSource # noqa: PLC0415
        from ..models.get_live_room_traffic_performance_response_data_traffic_performance_sub_source import GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSubSource # noqa: PLC0415
        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        sub_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sub_sources, Unset):
            sub_sources = []
            for sub_sources_item_data in self.sub_sources:
                sub_sources_item = sub_sources_item_data.to_dict()
                sub_sources.append(sub_sources_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if source is not UNSET:
            field_dict["source"] = source
        if sub_sources is not UNSET:
            field_dict["sub_sources"] = sub_sources

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_live_room_traffic_performance_response_data_traffic_performance_source import GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSource # noqa: PLC0415
        from ..models.get_live_room_traffic_performance_response_data_traffic_performance_sub_source import GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSubSource # noqa: PLC0415
        d = dict(src_dict)
        _source = d.pop("source", UNSET)
        source: GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSource | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSource.from_dict(_source)




        _sub_sources = d.pop("sub_sources", UNSET)
        sub_sources: list[GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSubSource] | Unset = UNSET
        if _sub_sources is not UNSET:
            sub_sources = []
            for sub_sources_item_data in _sub_sources:
                sub_sources_item = GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSubSource.from_dict(sub_sources_item_data)



                sub_sources.append(sub_sources_item)


        get_live_room_traffic_performance_response_data_traffic_performance = cls(
            source=source,
            sub_sources=sub_sources,
        )


        get_live_room_traffic_performance_response_data_traffic_performance.additional_properties = d
        return get_live_room_traffic_performance_response_data_traffic_performance

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
