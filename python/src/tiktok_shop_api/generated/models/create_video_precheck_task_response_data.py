from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_video_precheck_task_response_data_precheck import CreateVideoPrecheckTaskResponseDataPrecheck


T = TypeVar("T", bound="CreateVideoPrecheckTaskResponseData")


@_attrs_define
class CreateVideoPrecheckTaskResponseData:
    """
    Attributes:
        precheck (CreateVideoPrecheckTaskResponseDataPrecheck | Unset):
    """

    precheck: CreateVideoPrecheckTaskResponseDataPrecheck | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        precheck: dict[str, Any] | Unset = UNSET
        if not isinstance(self.precheck, Unset):
            precheck = self.precheck.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if precheck is not UNSET:
            field_dict["precheck"] = precheck

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_video_precheck_task_response_data_precheck import (
            CreateVideoPrecheckTaskResponseDataPrecheck,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _precheck = d.pop("precheck", UNSET)
        precheck: CreateVideoPrecheckTaskResponseDataPrecheck | Unset
        if isinstance(_precheck, Unset):
            precheck = UNSET
        else:
            precheck = CreateVideoPrecheckTaskResponseDataPrecheck.from_dict(_precheck)

        create_video_precheck_task_response_data = cls(
            precheck=precheck,
        )

        create_video_precheck_task_response_data.additional_properties = d
        return create_video_precheck_task_response_data

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
