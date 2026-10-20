from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_live_performance_list_response_data_live_stream_session_creator import (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionCreator,
    )
    from ..models.get_shop_live_performance_list_response_data_live_stream_session_interaction_performance import (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionInteractionPerformance,
    )
    from ..models.get_shop_live_performance_list_response_data_live_stream_session_sales_performance import (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformance,
    )
    from ..models.get_shop_live_performance_list_response_data_live_stream_session_traffic import (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionTraffic,
    )


T = TypeVar("T", bound="GetShopLIVEPerformanceListResponseDataLiveStreamSession")


@_attrs_define
class GetShopLIVEPerformanceListResponseDataLiveStreamSession:
    """
    Attributes:
        creator (GetShopLIVEPerformanceListResponseDataLiveStreamSessionCreator | Unset):
        end_time (str | Unset): End time of the LIVE, unix timestamp GMT (UTC+00:00).
        id (str | Unset): ID of the LIVE
        interaction_performance (GetShopLIVEPerformanceListResponseDataLiveStreamSessionInteractionPerformance | Unset):
        sales_performance (GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformance | Unset):
        start_time (str | Unset): Start time of the LIVE, unix timestamp GMT (UTC+00:00).
        title (str | Unset): Title of the LIVE
        traffic (GetShopLIVEPerformanceListResponseDataLiveStreamSessionTraffic | Unset):
    """

    creator: GetShopLIVEPerformanceListResponseDataLiveStreamSessionCreator | Unset = UNSET
    end_time: str | Unset = UNSET
    id: str | Unset = UNSET
    interaction_performance: GetShopLIVEPerformanceListResponseDataLiveStreamSessionInteractionPerformance | Unset = (
        UNSET
    )
    sales_performance: GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformance | Unset = UNSET
    start_time: str | Unset = UNSET
    title: str | Unset = UNSET
    traffic: GetShopLIVEPerformanceListResponseDataLiveStreamSessionTraffic | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        end_time = self.end_time

        id = self.id

        interaction_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interaction_performance, Unset):
            interaction_performance = self.interaction_performance.to_dict()

        sales_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sales_performance, Unset):
            sales_performance = self.sales_performance.to_dict()

        start_time = self.start_time

        title = self.title

        traffic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.traffic, Unset):
            traffic = self.traffic.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator is not UNSET:
            field_dict["creator"] = creator
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if id is not UNSET:
            field_dict["id"] = id
        if interaction_performance is not UNSET:
            field_dict["interaction_performance"] = interaction_performance
        if sales_performance is not UNSET:
            field_dict["sales_performance"] = sales_performance
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if title is not UNSET:
            field_dict["title"] = title
        if traffic is not UNSET:
            field_dict["traffic"] = traffic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_live_performance_list_response_data_live_stream_session_creator import (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionCreator,  # noqa: PLC0415
        )
        from ..models.get_shop_live_performance_list_response_data_live_stream_session_interaction_performance import (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionInteractionPerformance,  # noqa: PLC0415
        )
        from ..models.get_shop_live_performance_list_response_data_live_stream_session_sales_performance import (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformance,  # noqa: PLC0415
        )
        from ..models.get_shop_live_performance_list_response_data_live_stream_session_traffic import (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionTraffic,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _creator = d.pop("creator", UNSET)
        creator: GetShopLIVEPerformanceListResponseDataLiveStreamSessionCreator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = GetShopLIVEPerformanceListResponseDataLiveStreamSessionCreator.from_dict(_creator)

        end_time = d.pop("end_time", UNSET)

        id = d.pop("id", UNSET)

        _interaction_performance = d.pop("interaction_performance", UNSET)
        interaction_performance: GetShopLIVEPerformanceListResponseDataLiveStreamSessionInteractionPerformance | Unset
        if isinstance(_interaction_performance, Unset):
            interaction_performance = UNSET
        else:
            interaction_performance = (
                GetShopLIVEPerformanceListResponseDataLiveStreamSessionInteractionPerformance.from_dict(
                    _interaction_performance
                )
            )

        _sales_performance = d.pop("sales_performance", UNSET)
        sales_performance: GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformance | Unset
        if isinstance(_sales_performance, Unset):
            sales_performance = UNSET
        else:
            sales_performance = GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformance.from_dict(
                _sales_performance
            )

        start_time = d.pop("start_time", UNSET)

        title = d.pop("title", UNSET)

        _traffic = d.pop("traffic", UNSET)
        traffic: GetShopLIVEPerformanceListResponseDataLiveStreamSessionTraffic | Unset
        if isinstance(_traffic, Unset):
            traffic = UNSET
        else:
            traffic = GetShopLIVEPerformanceListResponseDataLiveStreamSessionTraffic.from_dict(_traffic)

        get_shop_live_performance_list_response_data_live_stream_session = cls(
            creator=creator,
            end_time=end_time,
            id=id,
            interaction_performance=interaction_performance,
            sales_performance=sales_performance,
            start_time=start_time,
            title=title,
            traffic=traffic,
        )

        get_shop_live_performance_list_response_data_live_stream_session.additional_properties = d
        return get_shop_live_performance_list_response_data_live_stream_session

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
