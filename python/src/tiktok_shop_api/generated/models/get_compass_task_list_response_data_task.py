from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetCompassTaskListResponseDataTask")



@_attrs_define
class GetCompassTaskListResponseDataTask:
    """ 
        Attributes:
            module_type (str | Unset): Allowed values: CREATOR, BASE.
            id (str | Unset): The ID of the offline report task. When the task status is `SUCCEEDED`, use this value as the
                `task_id` path parameter in `GET /affiliate_seller/202603/compass/offline_tasks/{task_id}/file` to download the
                completed export task's result file.
            file_name (str | Unset): the name of the final download file.
            status (str | Unset): The status of the task.
                - RUNNING
                - SUCCEEDED
                - FAILED
     """

    module_type: str | Unset = UNSET
    id: str | Unset = UNSET
    file_name: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        module_type = self.module_type

        id = self.id

        file_name = self.file_name

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if id is not UNSET:
            field_dict["id"] = id
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        module_type = d.pop("module_type", UNSET)

        id = d.pop("id", UNSET)

        file_name = d.pop("file_name", UNSET)

        status = d.pop("status", UNSET)

        get_compass_task_list_response_data_task = cls(
            module_type=module_type,
            id=id,
            file_name=file_name,
            status=status,
        )


        get_compass_task_list_response_data_task.additional_properties = d
        return get_compass_task_list_response_data_task

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
