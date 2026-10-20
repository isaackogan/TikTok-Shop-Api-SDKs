from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shoppable_video_precheck_result_response_data_precheck_task import GetShoppableVideoPrecheckResultResponseDataPrecheckTask





T = TypeVar("T", bound="GetShoppableVideoPrecheckResultResponseData")



@_attrs_define
class GetShoppableVideoPrecheckResultResponseData:
    """ 
        Attributes:
            precheck_task (GetShoppableVideoPrecheckResultResponseDataPrecheckTask | Unset):
     """

    precheck_task: GetShoppableVideoPrecheckResultResponseDataPrecheckTask | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shoppable_video_precheck_result_response_data_precheck_task import GetShoppableVideoPrecheckResultResponseDataPrecheckTask # noqa: PLC0415
        precheck_task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.precheck_task, Unset):
            precheck_task = self.precheck_task.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if precheck_task is not UNSET:
            field_dict["precheck_task"] = precheck_task

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shoppable_video_precheck_result_response_data_precheck_task import GetShoppableVideoPrecheckResultResponseDataPrecheckTask # noqa: PLC0415
        d = dict(src_dict)
        _precheck_task = d.pop("precheck_task", UNSET)
        precheck_task: GetShoppableVideoPrecheckResultResponseDataPrecheckTask | Unset
        if isinstance(_precheck_task,  Unset):
            precheck_task = UNSET
        else:
            precheck_task = GetShoppableVideoPrecheckResultResponseDataPrecheckTask.from_dict(_precheck_task)




        get_shoppable_video_precheck_result_response_data = cls(
            precheck_task=precheck_task,
        )


        get_shoppable_video_precheck_result_response_data.additional_properties = d
        return get_shoppable_video_precheck_result_response_data

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
