from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLogisticsTrackingResponseDataLogisticsDetailTrackList")


@_attrs_define
class GetLogisticsTrackingResponseDataLogisticsDetailTrackList:
    """
    Attributes:
        description (str | Unset): Description of this tracking event.
        tracking_no (str | Unset): The logistics tracking number associated with this tracking event.
        update_time_millis (int | Unset): Unix timestamp in milliseconds (GMT/UTC+00:00) when this tracking event was
            updated.
        action_code (int | Unset): Action code of this tracking event. It is an enumerated status value; the full
            enumeration list is maintained by the business side.
            Refer: action_code/action_code_name mapping details https://partner.tiktokshop.com/docv2/page/37tihrdq
        action_code_name (str | Unset): Machine-readable status name corresponding to `action_code`. For action code and
            name mapping details, see https://partner.tiktokshop.com/docv2/page/37tihrdq.
    """

    description: str | Unset = UNSET
    tracking_no: str | Unset = UNSET
    update_time_millis: int | Unset = UNSET
    action_code: int | Unset = UNSET
    action_code_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        tracking_no = self.tracking_no

        update_time_millis = self.update_time_millis

        action_code = self.action_code

        action_code_name = self.action_code_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if tracking_no is not UNSET:
            field_dict["tracking_no"] = tracking_no
        if update_time_millis is not UNSET:
            field_dict["update_time_millis"] = update_time_millis
        if action_code is not UNSET:
            field_dict["action_code"] = action_code
        if action_code_name is not UNSET:
            field_dict["action_code_name"] = action_code_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        tracking_no = d.pop("tracking_no", UNSET)

        update_time_millis = d.pop("update_time_millis", UNSET)

        action_code = d.pop("action_code", UNSET)

        action_code_name = d.pop("action_code_name", UNSET)

        get_logistics_tracking_response_data_logistics_detail_track_list = cls(
            description=description,
            tracking_no=tracking_no,
            update_time_millis=update_time_millis,
            action_code=action_code,
            action_code_name=action_code_name,
        )

        get_logistics_tracking_response_data_logistics_detail_track_list.additional_properties = d
        return get_logistics_tracking_response_data_logistics_detail_track_list

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
