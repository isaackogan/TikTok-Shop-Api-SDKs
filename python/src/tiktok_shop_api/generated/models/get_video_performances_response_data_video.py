from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_video_performances_response_data_video_performance import GetVideoPerformancesResponseDataVideoPerformance





T = TypeVar("T", bound="GetVideoPerformancesResponseDataVideo")



@_attrs_define
class GetVideoPerformancesResponseDataVideo:
    """ 
        Attributes:
            id (str | Unset): The video ID. The performances array contains the daily metrics for this video.
            performances (list[GetVideoPerformancesResponseDataVideoPerformance] | Unset): The list of objects within will
                be arranged in ascending order based on the start_time field.
     """

    id: str | Unset = UNSET
    performances: list[GetVideoPerformancesResponseDataVideoPerformance] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_video_performances_response_data_video_performance import GetVideoPerformancesResponseDataVideoPerformance # noqa: PLC0415
        id = self.id

        performances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.performances, Unset):
            performances = []
            for performances_item_data in self.performances:
                performances_item = performances_item_data.to_dict()
                performances.append(performances_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if performances is not UNSET:
            field_dict["performances"] = performances

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_video_performances_response_data_video_performance import GetVideoPerformancesResponseDataVideoPerformance # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _performances = d.pop("performances", UNSET)
        performances: list[GetVideoPerformancesResponseDataVideoPerformance] | Unset = UNSET
        if _performances is not UNSET:
            performances = []
            for performances_item_data in _performances:
                performances_item = GetVideoPerformancesResponseDataVideoPerformance.from_dict(performances_item_data)



                performances.append(performances_item)


        get_video_performances_response_data_video = cls(
            id=id,
            performances=performances,
        )


        get_video_performances_response_data_video.additional_properties = d
        return get_video_performances_response_data_video

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
