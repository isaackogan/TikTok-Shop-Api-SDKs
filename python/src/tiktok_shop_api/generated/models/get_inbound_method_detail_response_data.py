from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_inbound_method_detail_response_data_placement_task_status import (
    GetInboundMethodDetailResponseDataPlacementTaskStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_inbound_method_detail_response_data_info import GetInboundMethodDetailResponseDataInfo


T = TypeVar("T", bound="GetInboundMethodDetailResponseData")


@_attrs_define
class GetInboundMethodDetailResponseData:
    """
    Attributes:
        info (list[GetInboundMethodDetailResponseDataInfo] | Unset): Placement options for the current placement task.
            If `placement_task_status` is `Executing`, repeat this request with the same `plan_id`, `inbound_method`, and
            estimated arrival window to retrieve the latest status. When the status is `Succeed`, select an option from
            `info` and pass its `placement_option_id` to the Confirm Inbound Method API. Do not confirm an option when the
            status is `Failed`. After `expiration_timestamp`, call this API again with the same selection inputs to obtain a
            new placement option or task.
        placement_task_status (GetInboundMethodDetailResponseDataPlacementTaskStatus | Unset): **Possible values:**
            * `Executing`
            * `Succeed`
            * `Failed`
        expiration_timestamp (str | Unset): Unix timestamp in seconds when the placement result expires. For `ONE_HUB`,
            the expiration is set to 24 hours after this API processes the request. For other methods, it is 24 hours after
            the placement task's trigger time. After expiration, call this API again to generate a new placement task.
    """

    info: list[GetInboundMethodDetailResponseDataInfo] | Unset = UNSET
    placement_task_status: GetInboundMethodDetailResponseDataPlacementTaskStatus | Unset = UNSET
    expiration_timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.info, Unset):
            info = []
            for info_item_data in self.info:
                info_item = info_item_data.to_dict()
                info.append(info_item)

        placement_task_status: str | Unset = UNSET
        if not isinstance(self.placement_task_status, Unset):
            placement_task_status = self.placement_task_status.value

        expiration_timestamp = self.expiration_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if info is not UNSET:
            field_dict["info"] = info
        if placement_task_status is not UNSET:
            field_dict["placement_task_status"] = placement_task_status
        if expiration_timestamp is not UNSET:
            field_dict["expiration_timestamp"] = expiration_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_inbound_method_detail_response_data_info import (
            GetInboundMethodDetailResponseDataInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _info = d.pop("info", UNSET)
        info: list[GetInboundMethodDetailResponseDataInfo] | Unset = UNSET
        if _info is not UNSET:
            info = []
            for info_item_data in _info:
                info_item = GetInboundMethodDetailResponseDataInfo.from_dict(info_item_data)

                info.append(info_item)

        _placement_task_status = d.pop("placement_task_status", UNSET)
        placement_task_status: GetInboundMethodDetailResponseDataPlacementTaskStatus | Unset
        if isinstance(_placement_task_status, Unset):
            placement_task_status = UNSET
        else:
            placement_task_status = GetInboundMethodDetailResponseDataPlacementTaskStatus(_placement_task_status)

        expiration_timestamp = d.pop("expiration_timestamp", UNSET)

        get_inbound_method_detail_response_data = cls(
            info=info,
            placement_task_status=placement_task_status,
            expiration_timestamp=expiration_timestamp,
        )

        get_inbound_method_detail_response_data.additional_properties = d
        return get_inbound_method_detail_response_data

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
