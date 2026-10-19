from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_live_performance_list_response_data_live_stream_session import (
        GetShopLIVEPerformanceListResponseDataLiveStreamSession,
    )


T = TypeVar("T", bound="GetShopLIVEPerformanceListResponseData")


@_attrs_define
class GetShopLIVEPerformanceListResponseData:
    """
    Attributes:
        latest_available_date (datetime.date | Unset): Latest date in local timezone where data is ready (ISO 8601
            format).
        live_stream_sessions (list[GetShopLIVEPerformanceListResponseDataLiveStreamSession] | Unset): List of live
            performance metrics.
        next_page_token (str | Unset): Page token for the next page request.
        total_count (int | Unset): Total number of LIVE stream sessions.
        updated_at (str | Unset): Time when the data was last updated in shop registered timezone.
    """

    latest_available_date: datetime.date | Unset = UNSET
    live_stream_sessions: list[GetShopLIVEPerformanceListResponseDataLiveStreamSession] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        live_stream_sessions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.live_stream_sessions, Unset):
            live_stream_sessions = []
            for live_stream_sessions_item_data in self.live_stream_sessions:
                live_stream_sessions_item = live_stream_sessions_item_data.to_dict()
                live_stream_sessions.append(live_stream_sessions_item)

        next_page_token = self.next_page_token

        total_count = self.total_count

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if live_stream_sessions is not UNSET:
            field_dict["live_stream_sessions"] = live_stream_sessions
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_live_performance_list_response_data_live_stream_session import (
            GetShopLIVEPerformanceListResponseDataLiveStreamSession,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date, Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)

        _live_stream_sessions = d.pop("live_stream_sessions", UNSET)
        live_stream_sessions: list[GetShopLIVEPerformanceListResponseDataLiveStreamSession] | Unset = UNSET
        if _live_stream_sessions is not UNSET:
            live_stream_sessions = []
            for live_stream_sessions_item_data in _live_stream_sessions:
                live_stream_sessions_item = GetShopLIVEPerformanceListResponseDataLiveStreamSession.from_dict(
                    live_stream_sessions_item_data
                )

                live_stream_sessions.append(live_stream_sessions_item)

        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        get_shop_live_performance_list_response_data = cls(
            latest_available_date=latest_available_date,
            live_stream_sessions=live_stream_sessions,
            next_page_token=next_page_token,
            total_count=total_count,
            updated_at=updated_at,
        )

        get_shop_live_performance_list_response_data.additional_properties = d
        return get_shop_live_performance_list_response_data

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
