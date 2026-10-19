from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_live_performance_list_response_data_live_stream_session_traffic_gmv_per_hour import (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficGmvPerHour,
    )
    from ..models.get_shop_live_performance_list_response_data_live_stream_session_traffic_watch_gpm import (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficWatchGpm,
    )
    from ..models.show_gpm import ShowGpm


T = TypeVar("T", bound="GetShopLIVEPerformanceListResponseDataLiveStreamSessionTraffic")


@_attrs_define
class GetShopLIVEPerformanceListResponseDataLiveStreamSessionTraffic:
    """
    Attributes:
        acu (int | Unset): Average concurrent users.
        avg_viewing_duration (int | Unset): Average viewing duration in seconds.
        avg_viewing_duration_per_viewer (int | Unset): Average viewing duration per viewer in seconds.
        ctor (str | Unset): Click-to-order rate. Expressed as a raw decimal string.
        ctor_sku_order (str | Unset): Ratio of attributed SKU orders to product clicks. Expressed as a raw decimal
            string.
        ctr (str | Unset): Click-through rate. Expressed as a raw decimal string.
        gmv_per_hour (GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficGmvPerHour | Unset):
        impressions (int | Unset): Number of LIVE impressions.
        impressions_per_hour (int | Unset): Average number of impressions per hour.
        live_ctr (str | Unset): Ratio of product clicks to product impressions. Expressed as a raw decimal string.
        order_rate_sku_orders (str | Unset): Ratio of attributed SKU orders to views. Expressed as a raw decimal string.
        over_1m_live_viewing_rate (str | Unset): Ratio of views lasting longer than one minute. Expressed as a raw
            decimal string.
        over_1m_views (int | Unset): Number of views lasting longer than one minute.
        pcu (int | Unset): Peak concurrent users.
        product_clicks (int | Unset): Number of product clicks.
        product_impressions (int | Unset): Number of product impressions.
        products_added (int | Unset): Number of products added to the LIVE session.
        show_gpm (ShowGpm | Unset):
        tap_through_rate (str | Unset): Ratio of LIVE views to LIVE impressions. Expressed as a raw decimal string.
        viewers (int | Unset): Number of unique viewers.
        views (int | Unset): Number of LIVE views.
        watch_gpm (GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficWatchGpm | Unset):
    """

    acu: int | Unset = UNSET
    avg_viewing_duration: int | Unset = UNSET
    avg_viewing_duration_per_viewer: int | Unset = UNSET
    ctor: str | Unset = UNSET
    ctor_sku_order: str | Unset = UNSET
    ctr: str | Unset = UNSET
    gmv_per_hour: GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficGmvPerHour | Unset = UNSET
    impressions: int | Unset = UNSET
    impressions_per_hour: int | Unset = UNSET
    live_ctr: str | Unset = UNSET
    order_rate_sku_orders: str | Unset = UNSET
    over_1m_live_viewing_rate: str | Unset = UNSET
    over_1m_views: int | Unset = UNSET
    pcu: int | Unset = UNSET
    product_clicks: int | Unset = UNSET
    product_impressions: int | Unset = UNSET
    products_added: int | Unset = UNSET
    show_gpm: ShowGpm | Unset = UNSET
    tap_through_rate: str | Unset = UNSET
    viewers: int | Unset = UNSET
    views: int | Unset = UNSET
    watch_gpm: GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficWatchGpm | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acu = self.acu

        avg_viewing_duration = self.avg_viewing_duration

        avg_viewing_duration_per_viewer = self.avg_viewing_duration_per_viewer

        ctor = self.ctor

        ctor_sku_order = self.ctor_sku_order

        ctr = self.ctr

        gmv_per_hour: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv_per_hour, Unset):
            gmv_per_hour = self.gmv_per_hour.to_dict()

        impressions = self.impressions

        impressions_per_hour = self.impressions_per_hour

        live_ctr = self.live_ctr

        order_rate_sku_orders = self.order_rate_sku_orders

        over_1m_live_viewing_rate = self.over_1m_live_viewing_rate

        over_1m_views = self.over_1m_views

        pcu = self.pcu

        product_clicks = self.product_clicks

        product_impressions = self.product_impressions

        products_added = self.products_added

        show_gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.show_gpm, Unset):
            show_gpm = self.show_gpm.to_dict()

        tap_through_rate = self.tap_through_rate

        viewers = self.viewers

        views = self.views

        watch_gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.watch_gpm, Unset):
            watch_gpm = self.watch_gpm.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acu is not UNSET:
            field_dict["acu"] = acu
        if avg_viewing_duration is not UNSET:
            field_dict["avg_viewing_duration"] = avg_viewing_duration
        if avg_viewing_duration_per_viewer is not UNSET:
            field_dict["avg_viewing_duration_per_viewer"] = avg_viewing_duration_per_viewer
        if ctor is not UNSET:
            field_dict["ctor"] = ctor
        if ctor_sku_order is not UNSET:
            field_dict["ctor_sku_order"] = ctor_sku_order
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if gmv_per_hour is not UNSET:
            field_dict["gmv_per_hour"] = gmv_per_hour
        if impressions is not UNSET:
            field_dict["impressions"] = impressions
        if impressions_per_hour is not UNSET:
            field_dict["impressions_per_hour"] = impressions_per_hour
        if live_ctr is not UNSET:
            field_dict["live_ctr"] = live_ctr
        if order_rate_sku_orders is not UNSET:
            field_dict["order_rate_sku_orders"] = order_rate_sku_orders
        if over_1m_live_viewing_rate is not UNSET:
            field_dict["over_1m_live_viewing_rate"] = over_1m_live_viewing_rate
        if over_1m_views is not UNSET:
            field_dict["over_1m_views"] = over_1m_views
        if pcu is not UNSET:
            field_dict["pcu"] = pcu
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if products_added is not UNSET:
            field_dict["products_added"] = products_added
        if show_gpm is not UNSET:
            field_dict["show_gpm"] = show_gpm
        if tap_through_rate is not UNSET:
            field_dict["tap_through_rate"] = tap_through_rate
        if viewers is not UNSET:
            field_dict["viewers"] = viewers
        if views is not UNSET:
            field_dict["views"] = views
        if watch_gpm is not UNSET:
            field_dict["watch_gpm"] = watch_gpm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_live_performance_list_response_data_live_stream_session_traffic_gmv_per_hour import (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficGmvPerHour,  # noqa: PLC0415
        )
        from ..models.get_shop_live_performance_list_response_data_live_stream_session_traffic_watch_gpm import (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficWatchGpm,  # noqa: PLC0415
        )
        from ..models.show_gpm import ShowGpm  # noqa: PLC0415

        d = dict(src_dict)
        acu = d.pop("acu", UNSET)

        avg_viewing_duration = d.pop("avg_viewing_duration", UNSET)

        avg_viewing_duration_per_viewer = d.pop("avg_viewing_duration_per_viewer", UNSET)

        ctor = d.pop("ctor", UNSET)

        ctor_sku_order = d.pop("ctor_sku_order", UNSET)

        ctr = d.pop("ctr", UNSET)

        _gmv_per_hour = d.pop("gmv_per_hour", UNSET)
        gmv_per_hour: GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficGmvPerHour | Unset
        if isinstance(_gmv_per_hour, Unset):
            gmv_per_hour = UNSET
        else:
            gmv_per_hour = GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficGmvPerHour.from_dict(
                _gmv_per_hour
            )

        impressions = d.pop("impressions", UNSET)

        impressions_per_hour = d.pop("impressions_per_hour", UNSET)

        live_ctr = d.pop("live_ctr", UNSET)

        order_rate_sku_orders = d.pop("order_rate_sku_orders", UNSET)

        over_1m_live_viewing_rate = d.pop("over_1m_live_viewing_rate", UNSET)

        over_1m_views = d.pop("over_1m_views", UNSET)

        pcu = d.pop("pcu", UNSET)

        product_clicks = d.pop("product_clicks", UNSET)

        product_impressions = d.pop("product_impressions", UNSET)

        products_added = d.pop("products_added", UNSET)

        _show_gpm = d.pop("show_gpm", UNSET)
        show_gpm: ShowGpm | Unset
        if isinstance(_show_gpm, Unset):
            show_gpm = UNSET
        else:
            show_gpm = ShowGpm.from_dict(_show_gpm)

        tap_through_rate = d.pop("tap_through_rate", UNSET)

        viewers = d.pop("viewers", UNSET)

        views = d.pop("views", UNSET)

        _watch_gpm = d.pop("watch_gpm", UNSET)
        watch_gpm: GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficWatchGpm | Unset
        if isinstance(_watch_gpm, Unset):
            watch_gpm = UNSET
        else:
            watch_gpm = GetShopLIVEPerformanceListResponseDataLiveStreamSessionTrafficWatchGpm.from_dict(_watch_gpm)

        get_shop_live_performance_list_response_data_live_stream_session_traffic = cls(
            acu=acu,
            avg_viewing_duration=avg_viewing_duration,
            avg_viewing_duration_per_viewer=avg_viewing_duration_per_viewer,
            ctor=ctor,
            ctor_sku_order=ctor_sku_order,
            ctr=ctr,
            gmv_per_hour=gmv_per_hour,
            impressions=impressions,
            impressions_per_hour=impressions_per_hour,
            live_ctr=live_ctr,
            order_rate_sku_orders=order_rate_sku_orders,
            over_1m_live_viewing_rate=over_1m_live_viewing_rate,
            over_1m_views=over_1m_views,
            pcu=pcu,
            product_clicks=product_clicks,
            product_impressions=product_impressions,
            products_added=products_added,
            show_gpm=show_gpm,
            tap_through_rate=tap_through_rate,
            viewers=viewers,
            views=views,
            watch_gpm=watch_gpm,
        )

        get_shop_live_performance_list_response_data_live_stream_session_traffic.additional_properties = d
        return get_shop_live_performance_list_response_data_live_stream_session_traffic

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
