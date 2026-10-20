from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gmv import Gmv


T = TypeVar("T", bound="GetVideoPerformancesResponseDataVideoPerformanceMetric")


@_attrs_define
class GetVideoPerformancesResponseDataVideoPerformanceMetric:
    """
    Attributes:
        anchor_display_rate (str | Unset): Display rate for anchors, specified with two decimal numbers.
        click_through_rate (str | Unset): Click through rate, specified with two decimal numbers.
        order_count (int | Unset): Number of orders in this date.
        item_sold_count (int | Unset): Number of sold items in this date.
        gmv (Gmv | Unset):
    """

    anchor_display_rate: str | Unset = UNSET
    click_through_rate: str | Unset = UNSET
    order_count: int | Unset = UNSET
    item_sold_count: int | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anchor_display_rate = self.anchor_display_rate

        click_through_rate = self.click_through_rate

        order_count = self.order_count

        item_sold_count = self.item_sold_count

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anchor_display_rate is not UNSET:
            field_dict["anchor_display_rate"] = anchor_display_rate
        if click_through_rate is not UNSET:
            field_dict["click_through_rate"] = click_through_rate
        if order_count is not UNSET:
            field_dict["order_count"] = order_count
        if item_sold_count is not UNSET:
            field_dict["item_sold_count"] = item_sold_count
        if gmv is not UNSET:
            field_dict["gmv"] = gmv

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv  # noqa: PLC0415

        d = dict(src_dict)
        anchor_display_rate = d.pop("anchor_display_rate", UNSET)

        click_through_rate = d.pop("click_through_rate", UNSET)

        order_count = d.pop("order_count", UNSET)

        item_sold_count = d.pop("item_sold_count", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv, Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)

        get_video_performances_response_data_video_performance_metric = cls(
            anchor_display_rate=anchor_display_rate,
            click_through_rate=click_through_rate,
            order_count=order_count,
            item_sold_count=item_sold_count,
            gmv=gmv,
        )

        get_video_performances_response_data_video_performance_metric.additional_properties = d
        return get_video_performances_response_data_video_performance_metric

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
