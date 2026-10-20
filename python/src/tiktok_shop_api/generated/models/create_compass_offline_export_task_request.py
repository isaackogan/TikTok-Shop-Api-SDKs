from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_compass_offline_export_task_request_module_type import (
    CreateCompassOfflineExportTaskRequestModuleType,
)
from ..models.create_compass_offline_export_task_request_plan_type import CreateCompassOfflineExportTaskRequestPlanType
from ..models.create_compass_offline_export_task_request_window_type import (
    CreateCompassOfflineExportTaskRequestWindowType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCompassOfflineExportTaskRequest")


@_attrs_define
class CreateCompassOfflineExportTaskRequest:
    """
    Attributes:
        module_type (CreateCompassOfflineExportTaskRequestModuleType | Unset): Type of Compass data to export. Allowed
            values:
            - CREATOR: Creator list data.
            - BASE: Core performance data.
        window_type (CreateCompassOfflineExportTaskRequestWindowType | Unset): Time window included in the export,
            ending on end_day. Allowed values: PAST_24H, PAST_7_DAYS, PAST_30_DAYS.
        end_day (int | Unset): End date in the local timezone of the specified region, formatted as YYYYMMDD.
              - id：UTC+7
              - my：UTC+8
              - sg：UTC+8
              - vn：UTC+7
              - th：UTC+7
              - ph：UTC+8
              - sa：UTC+3
              - us：UTC-8
              - mx：UTC-6
              - br：UTC-3
              - jp：UTC+9
              - gb：UTC+0
              - ie：UTC+0
              - es：UTC+1
              - de：UTC+1
              - fr：UTC+1
              - it：UTC+1
              - pl：UTC+1
              - nl：UTC+1
              - be：UTC+1
              - cz：UTC+1
              - at：UTC+1
              - gr：UTC+2
              - pt：UTC+0
              - hu：UTC+1
        plan_type (CreateCompassOfflineExportTaskRequestPlanType | Unset): Plan type. Allowed values: ALL, TARGET, OPEN,
            PARTNER.
    """

    module_type: CreateCompassOfflineExportTaskRequestModuleType | Unset = UNSET
    window_type: CreateCompassOfflineExportTaskRequestWindowType | Unset = UNSET
    end_day: int | Unset = UNSET
    plan_type: CreateCompassOfflineExportTaskRequestPlanType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        module_type: str | Unset = UNSET
        if not isinstance(self.module_type, Unset):
            module_type = self.module_type.value

        window_type: str | Unset = UNSET
        if not isinstance(self.window_type, Unset):
            window_type = self.window_type.value

        end_day = self.end_day

        plan_type: str | Unset = UNSET
        if not isinstance(self.plan_type, Unset):
            plan_type = self.plan_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if module_type is not UNSET:
            field_dict["module_type"] = module_type
        if window_type is not UNSET:
            field_dict["window_type"] = window_type
        if end_day is not UNSET:
            field_dict["end_day"] = end_day
        if plan_type is not UNSET:
            field_dict["plan_type"] = plan_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _module_type = d.pop("module_type", UNSET)
        module_type: CreateCompassOfflineExportTaskRequestModuleType | Unset
        if isinstance(_module_type, Unset):
            module_type = UNSET
        else:
            module_type = CreateCompassOfflineExportTaskRequestModuleType(_module_type)

        _window_type = d.pop("window_type", UNSET)
        window_type: CreateCompassOfflineExportTaskRequestWindowType | Unset
        if isinstance(_window_type, Unset):
            window_type = UNSET
        else:
            window_type = CreateCompassOfflineExportTaskRequestWindowType(_window_type)

        end_day = d.pop("end_day", UNSET)

        _plan_type = d.pop("plan_type", UNSET)
        plan_type: CreateCompassOfflineExportTaskRequestPlanType | Unset
        if isinstance(_plan_type, Unset):
            plan_type = UNSET
        else:
            plan_type = CreateCompassOfflineExportTaskRequestPlanType(_plan_type)

        create_compass_offline_export_task_request = cls(
            module_type=module_type,
            window_type=window_type,
            end_day=end_day,
            plan_type=plan_type,
        )

        create_compass_offline_export_task_request.additional_properties = d
        return create_compass_offline_export_task_request

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
