from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_compass_offline_export_task_response_data_task import CreateCompassOfflineExportTaskResponseDataTask





T = TypeVar("T", bound="CreateCompassOfflineExportTaskResponseData")



@_attrs_define
class CreateCompassOfflineExportTaskResponseData:
    """ 
        Attributes:
            task (CreateCompassOfflineExportTaskResponseDataTask | Unset):
     """

    task: CreateCompassOfflineExportTaskResponseDataTask | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_compass_offline_export_task_response_data_task import CreateCompassOfflineExportTaskResponseDataTask # noqa: PLC0415
        task: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task, Unset):
            task = self.task.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if task is not UNSET:
            field_dict["task"] = task

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_compass_offline_export_task_response_data_task import CreateCompassOfflineExportTaskResponseDataTask # noqa: PLC0415
        d = dict(src_dict)
        _task = d.pop("task", UNSET)
        task: CreateCompassOfflineExportTaskResponseDataTask | Unset
        if isinstance(_task,  Unset):
            task = UNSET
        else:
            task = CreateCompassOfflineExportTaskResponseDataTask.from_dict(_task)




        create_compass_offline_export_task_response_data = cls(
            task=task,
        )


        create_compass_offline_export_task_response_data.additional_properties = d
        return create_compass_offline_export_task_response_data

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
