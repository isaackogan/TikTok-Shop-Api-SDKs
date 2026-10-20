from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.local_gmv import LocalGmv
    from ..models.local_unit_price import LocalUnitPrice


T = TypeVar("T", bound="GetLiveRoomCoreStatsResponseDataStat")


@_attrs_define
class GetLiveRoomCoreStatsResponseDataStat:
    """
    Attributes:
        sales (int | Unset): The number of product units sold from the livestream
        local_gmv (LocalGmv | Unset):
        created_order_count (int | Unset): The number of SKU orders created by users from the livestream
        current_visitor_count (int | Unset): The number of viewers currently watching the livestream.
        paid_order_count (int | Unset): The number of SKU orders created and paid by users from the livestream
        local_unit_price (LocalUnitPrice | Unset):
        product_reach_count (int | Unset): The number of product clicks from the livestream, including product list and
            product card clicks
        watch_pv (int | Unset): The number of views of the livestream
        click_through_rate (str | Unset): Click through rate，product clicks / views
        accumulated_new_follower_count (int | Unset): The number of times users clicked to follow the creator
        buyer_count (int | Unset): The number of unique users who paid for orders made from livestream, including
            returned/refunded orders
        accumulated_comment_count (int | Unset): The cumulative number of times users left comments on the livestream
        product_view_count (int | Unset): The number of impressions of all livestream products, including product list
            and product card impressions
        click_order_rate (str | Unset): Click to order，paid sku orders/ product clicks
        avg_watching_duration (int | Unset): The average length of time each unique viewer watches the livestream.
        accumulated_sharing_count (int | Unset): The cumulative number of times users shared the livestream
        peak_concurrent_user_count (int | Unset): The peak number of concurrent viewers of the livestream
    """

    sales: int | Unset = UNSET
    local_gmv: LocalGmv | Unset = UNSET
    created_order_count: int | Unset = UNSET
    current_visitor_count: int | Unset = UNSET
    paid_order_count: int | Unset = UNSET
    local_unit_price: LocalUnitPrice | Unset = UNSET
    product_reach_count: int | Unset = UNSET
    watch_pv: int | Unset = UNSET
    click_through_rate: str | Unset = UNSET
    accumulated_new_follower_count: int | Unset = UNSET
    buyer_count: int | Unset = UNSET
    accumulated_comment_count: int | Unset = UNSET
    product_view_count: int | Unset = UNSET
    click_order_rate: str | Unset = UNSET
    avg_watching_duration: int | Unset = UNSET
    accumulated_sharing_count: int | Unset = UNSET
    peak_concurrent_user_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sales = self.sales

        local_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_gmv, Unset):
            local_gmv = self.local_gmv.to_dict()

        created_order_count = self.created_order_count

        current_visitor_count = self.current_visitor_count

        paid_order_count = self.paid_order_count

        local_unit_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_unit_price, Unset):
            local_unit_price = self.local_unit_price.to_dict()

        product_reach_count = self.product_reach_count

        watch_pv = self.watch_pv

        click_through_rate = self.click_through_rate

        accumulated_new_follower_count = self.accumulated_new_follower_count

        buyer_count = self.buyer_count

        accumulated_comment_count = self.accumulated_comment_count

        product_view_count = self.product_view_count

        click_order_rate = self.click_order_rate

        avg_watching_duration = self.avg_watching_duration

        accumulated_sharing_count = self.accumulated_sharing_count

        peak_concurrent_user_count = self.peak_concurrent_user_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sales is not UNSET:
            field_dict["sales"] = sales
        if local_gmv is not UNSET:
            field_dict["local_gmv"] = local_gmv
        if created_order_count is not UNSET:
            field_dict["created_order_count"] = created_order_count
        if current_visitor_count is not UNSET:
            field_dict["current_visitor_count"] = current_visitor_count
        if paid_order_count is not UNSET:
            field_dict["paid_order_count"] = paid_order_count
        if local_unit_price is not UNSET:
            field_dict["local_unit_price"] = local_unit_price
        if product_reach_count is not UNSET:
            field_dict["product_reach_count"] = product_reach_count
        if watch_pv is not UNSET:
            field_dict["watch_pv"] = watch_pv
        if click_through_rate is not UNSET:
            field_dict["click_through_rate"] = click_through_rate
        if accumulated_new_follower_count is not UNSET:
            field_dict["accumulated_new_follower_count"] = accumulated_new_follower_count
        if buyer_count is not UNSET:
            field_dict["buyer_count"] = buyer_count
        if accumulated_comment_count is not UNSET:
            field_dict["accumulated_comment_count"] = accumulated_comment_count
        if product_view_count is not UNSET:
            field_dict["product_view_count"] = product_view_count
        if click_order_rate is not UNSET:
            field_dict["click_order_rate"] = click_order_rate
        if avg_watching_duration is not UNSET:
            field_dict["avg_watching_duration"] = avg_watching_duration
        if accumulated_sharing_count is not UNSET:
            field_dict["accumulated_sharing_count"] = accumulated_sharing_count
        if peak_concurrent_user_count is not UNSET:
            field_dict["peak_concurrent_user_count"] = peak_concurrent_user_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.local_gmv import LocalGmv  # noqa: PLC0415
        from ..models.local_unit_price import LocalUnitPrice  # noqa: PLC0415

        d = dict(src_dict)
        sales = d.pop("sales", UNSET)

        _local_gmv = d.pop("local_gmv", UNSET)
        local_gmv: LocalGmv | Unset
        if isinstance(_local_gmv, Unset):
            local_gmv = UNSET
        else:
            local_gmv = LocalGmv.from_dict(_local_gmv)

        created_order_count = d.pop("created_order_count", UNSET)

        current_visitor_count = d.pop("current_visitor_count", UNSET)

        paid_order_count = d.pop("paid_order_count", UNSET)

        _local_unit_price = d.pop("local_unit_price", UNSET)
        local_unit_price: LocalUnitPrice | Unset
        if isinstance(_local_unit_price, Unset):
            local_unit_price = UNSET
        else:
            local_unit_price = LocalUnitPrice.from_dict(_local_unit_price)

        product_reach_count = d.pop("product_reach_count", UNSET)

        watch_pv = d.pop("watch_pv", UNSET)

        click_through_rate = d.pop("click_through_rate", UNSET)

        accumulated_new_follower_count = d.pop("accumulated_new_follower_count", UNSET)

        buyer_count = d.pop("buyer_count", UNSET)

        accumulated_comment_count = d.pop("accumulated_comment_count", UNSET)

        product_view_count = d.pop("product_view_count", UNSET)

        click_order_rate = d.pop("click_order_rate", UNSET)

        avg_watching_duration = d.pop("avg_watching_duration", UNSET)

        accumulated_sharing_count = d.pop("accumulated_sharing_count", UNSET)

        peak_concurrent_user_count = d.pop("peak_concurrent_user_count", UNSET)

        get_live_room_core_stats_response_data_stat = cls(
            sales=sales,
            local_gmv=local_gmv,
            created_order_count=created_order_count,
            current_visitor_count=current_visitor_count,
            paid_order_count=paid_order_count,
            local_unit_price=local_unit_price,
            product_reach_count=product_reach_count,
            watch_pv=watch_pv,
            click_through_rate=click_through_rate,
            accumulated_new_follower_count=accumulated_new_follower_count,
            buyer_count=buyer_count,
            accumulated_comment_count=accumulated_comment_count,
            product_view_count=product_view_count,
            click_order_rate=click_order_rate,
            avg_watching_duration=avg_watching_duration,
            accumulated_sharing_count=accumulated_sharing_count,
            peak_concurrent_user_count=peak_concurrent_user_count,
        )

        get_live_room_core_stats_response_data_stat.additional_properties = d
        return get_live_room_core_stats_response_data_stat

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
