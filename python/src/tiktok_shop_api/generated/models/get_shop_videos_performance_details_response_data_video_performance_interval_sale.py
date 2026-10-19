from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_videos_performance_details_response_data_video_performance_interval_sale_overall import (
        GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSaleOverall,
    )


T = TypeVar("T", bound="GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSale")


@_attrs_define
class GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSale:
    """
    Attributes:
        overall (GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSaleOverall | Unset):
    """

    overall: GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSaleOverall | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overall: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overall, Unset):
            overall = self.overall.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if overall is not UNSET:
            field_dict["overall"] = overall

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_videos_performance_details_response_data_video_performance_interval_sale_overall import (
            GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSaleOverall,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _overall = d.pop("overall", UNSET)
        overall: GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSaleOverall | Unset
        if isinstance(_overall, Unset):
            overall = UNSET
        else:
            overall = GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSaleOverall.from_dict(_overall)

        get_shop_videos_performance_details_response_data_video_performance_interval_sale = cls(
            overall=overall,
        )

        get_shop_videos_performance_details_response_data_video_performance_interval_sale.additional_properties = d
        return get_shop_videos_performance_details_response_data_video_performance_interval_sale

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
