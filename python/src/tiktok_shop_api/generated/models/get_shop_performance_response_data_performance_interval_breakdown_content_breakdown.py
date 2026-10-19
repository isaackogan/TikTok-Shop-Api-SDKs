from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_shop_performance_response_data_performance_interval_breakdown_content_breakdown_channel import (
    GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownChannel,
)
from ..models.get_shop_performance_response_data_performance_interval_breakdown_content_breakdown_content_type import (
    GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownContentType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gmv import Gmv
    from ..models.indirect_gmv import IndirectGmv


T = TypeVar("T", bound="GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdown")


@_attrs_define
class GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdown:
    """
    Attributes:
        channel (GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownChannel | Unset): Channel
            type.
            Possible values: CREATOR, SELLER
        content_type (GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownContentType | Unset):
            Content type.
            Possible values: LIVE, VIDEO
        gmv (Gmv | Unset):
        indirect_gmv (IndirectGmv | Unset):
    """

    channel: GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownChannel | Unset = UNSET
    content_type: GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownContentType | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    indirect_gmv: IndirectGmv | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value

        content_type: str | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.indirect_gmv, Unset):
            indirect_gmv = self.indirect_gmv.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if indirect_gmv is not UNSET:
            field_dict["indirect_gmv"] = indirect_gmv

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv  # noqa: PLC0415
        from ..models.indirect_gmv import IndirectGmv  # noqa: PLC0415

        d = dict(src_dict)
        _channel = d.pop("channel", UNSET)
        channel: GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownChannel | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownChannel(_channel)

        _content_type = d.pop("content_type", UNSET)
        content_type: GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdownContentType(
                _content_type
            )

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv, Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)

        _indirect_gmv = d.pop("indirect_gmv", UNSET)
        indirect_gmv: IndirectGmv | Unset
        if isinstance(_indirect_gmv, Unset):
            indirect_gmv = UNSET
        else:
            indirect_gmv = IndirectGmv.from_dict(_indirect_gmv)

        get_shop_performance_response_data_performance_interval_breakdown_content_breakdown = cls(
            channel=channel,
            content_type=content_type,
            gmv=gmv,
            indirect_gmv=indirect_gmv,
        )

        get_shop_performance_response_data_performance_interval_breakdown_content_breakdown.additional_properties = d
        return get_shop_performance_response_data_performance_interval_breakdown_content_breakdown

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
