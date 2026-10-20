from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avg_live_auction_price import AvgLiveAuctionPrice
    from ..models.live_attributed_gmv import LiveAttributedGmv
    from ..models.live_auction_attributed_gmv import LiveAuctionAttributedGmv
    from ..models.live_gmv import LiveGmv
    from ..models.live_indirect_gmv import LiveIndirectGmv
    from ..models.show_gpm import ShowGpm


T = TypeVar("T", bound="GetShopLIVEPerformanceOverviewResponseDataPerformanceInterval")


@_attrs_define
class GetShopLIVEPerformanceOverviewResponseDataPerformanceInterval:
    """
    Attributes:
        avg_live_auction_price (AvgLiveAuctionPrice | Unset):
        avg_viewing_duration (int | Unset): Average viewing duration in seconds.
        ctor_sku_order (str | Unset): Ratio of LIVE-attributed SKU orders to product clicks in raw decimal format.
        end_date (datetime.date | Unset): End date of the interval (ISO 8601 YYYY-MM-DD format) in shop registered
            timezone, exclusive.
        live_attributed_gmv (LiveAttributedGmv | Unset):
        live_attributed_items_sold (int | Unset): Number of items sold attributed to LIVE streams.
        live_attributed_sku_orders (int | Unset): Number of paid SKU orders attributed to LIVE streams.
        live_auction_attributed_gmv (LiveAuctionAttributedGmv | Unset):
        live_auction_attributed_items_sold (int | Unset): Number of items sold attributed to LIVE auction products.
        live_auction_attributed_sku_orders (int | Unset): Number of paid SKU orders attributed to LIVE auction products.
        live_ctr (str | Unset): Ratio of product clicks to product impressions from LIVE streams in raw decimal format.
        live_gmv (LiveGmv | Unset):
        live_indirect_gmv (LiveIndirectGmv | Unset):
        show_gpm (ShowGpm | Unset):
        start_date (datetime.date | Unset): Start date of the interval (ISO 8601 YYYY-MM-DD format) in shop registered
            timezone, inclusive.
        views (int | Unset): Number of LIVE views.
    """

    avg_live_auction_price: AvgLiveAuctionPrice | Unset = UNSET
    avg_viewing_duration: int | Unset = UNSET
    ctor_sku_order: str | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    live_attributed_gmv: LiveAttributedGmv | Unset = UNSET
    live_attributed_items_sold: int | Unset = UNSET
    live_attributed_sku_orders: int | Unset = UNSET
    live_auction_attributed_gmv: LiveAuctionAttributedGmv | Unset = UNSET
    live_auction_attributed_items_sold: int | Unset = UNSET
    live_auction_attributed_sku_orders: int | Unset = UNSET
    live_ctr: str | Unset = UNSET
    live_gmv: LiveGmv | Unset = UNSET
    live_indirect_gmv: LiveIndirectGmv | Unset = UNSET
    show_gpm: ShowGpm | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    views: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_live_auction_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_live_auction_price, Unset):
            avg_live_auction_price = self.avg_live_auction_price.to_dict()

        avg_viewing_duration = self.avg_viewing_duration

        ctor_sku_order = self.ctor_sku_order

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        live_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_attributed_gmv, Unset):
            live_attributed_gmv = self.live_attributed_gmv.to_dict()

        live_attributed_items_sold = self.live_attributed_items_sold

        live_attributed_sku_orders = self.live_attributed_sku_orders

        live_auction_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_auction_attributed_gmv, Unset):
            live_auction_attributed_gmv = self.live_auction_attributed_gmv.to_dict()

        live_auction_attributed_items_sold = self.live_auction_attributed_items_sold

        live_auction_attributed_sku_orders = self.live_auction_attributed_sku_orders

        live_ctr = self.live_ctr

        live_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_gmv, Unset):
            live_gmv = self.live_gmv.to_dict()

        live_indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_indirect_gmv, Unset):
            live_indirect_gmv = self.live_indirect_gmv.to_dict()

        show_gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.show_gpm, Unset):
            show_gpm = self.show_gpm.to_dict()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_live_auction_price is not UNSET:
            field_dict["avg_live_auction_price"] = avg_live_auction_price
        if avg_viewing_duration is not UNSET:
            field_dict["avg_viewing_duration"] = avg_viewing_duration
        if ctor_sku_order is not UNSET:
            field_dict["ctor_sku_order"] = ctor_sku_order
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if live_attributed_gmv is not UNSET:
            field_dict["live_attributed_gmv"] = live_attributed_gmv
        if live_attributed_items_sold is not UNSET:
            field_dict["live_attributed_items_sold"] = live_attributed_items_sold
        if live_attributed_sku_orders is not UNSET:
            field_dict["live_attributed_sku_orders"] = live_attributed_sku_orders
        if live_auction_attributed_gmv is not UNSET:
            field_dict["live_auction_attributed_gmv"] = live_auction_attributed_gmv
        if live_auction_attributed_items_sold is not UNSET:
            field_dict["live_auction_attributed_items_sold"] = live_auction_attributed_items_sold
        if live_auction_attributed_sku_orders is not UNSET:
            field_dict["live_auction_attributed_sku_orders"] = live_auction_attributed_sku_orders
        if live_ctr is not UNSET:
            field_dict["live_ctr"] = live_ctr
        if live_gmv is not UNSET:
            field_dict["live_gmv"] = live_gmv
        if live_indirect_gmv is not UNSET:
            field_dict["live_indirect_gmv"] = live_indirect_gmv
        if show_gpm is not UNSET:
            field_dict["show_gpm"] = show_gpm
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avg_live_auction_price import AvgLiveAuctionPrice  # noqa: PLC0415
        from ..models.live_attributed_gmv import LiveAttributedGmv  # noqa: PLC0415
        from ..models.live_auction_attributed_gmv import LiveAuctionAttributedGmv  # noqa: PLC0415
        from ..models.live_gmv import LiveGmv  # noqa: PLC0415
        from ..models.live_indirect_gmv import LiveIndirectGmv  # noqa: PLC0415
        from ..models.show_gpm import ShowGpm  # noqa: PLC0415

        d = dict(src_dict)
        _avg_live_auction_price = d.pop("avg_live_auction_price", UNSET)
        avg_live_auction_price: AvgLiveAuctionPrice | Unset
        if isinstance(_avg_live_auction_price, Unset):
            avg_live_auction_price = UNSET
        else:
            avg_live_auction_price = AvgLiveAuctionPrice.from_dict(_avg_live_auction_price)

        avg_viewing_duration = d.pop("avg_viewing_duration", UNSET)

        ctor_sku_order = d.pop("ctor_sku_order", UNSET)

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)

        _live_attributed_gmv = d.pop("live_attributed_gmv", UNSET)
        live_attributed_gmv: LiveAttributedGmv | Unset
        if isinstance(_live_attributed_gmv, Unset):
            live_attributed_gmv = UNSET
        else:
            live_attributed_gmv = LiveAttributedGmv.from_dict(_live_attributed_gmv)

        live_attributed_items_sold = d.pop("live_attributed_items_sold", UNSET)

        live_attributed_sku_orders = d.pop("live_attributed_sku_orders", UNSET)

        _live_auction_attributed_gmv = d.pop("live_auction_attributed_gmv", UNSET)
        live_auction_attributed_gmv: LiveAuctionAttributedGmv | Unset
        if isinstance(_live_auction_attributed_gmv, Unset):
            live_auction_attributed_gmv = UNSET
        else:
            live_auction_attributed_gmv = LiveAuctionAttributedGmv.from_dict(_live_auction_attributed_gmv)

        live_auction_attributed_items_sold = d.pop("live_auction_attributed_items_sold", UNSET)

        live_auction_attributed_sku_orders = d.pop("live_auction_attributed_sku_orders", UNSET)

        live_ctr = d.pop("live_ctr", UNSET)

        _live_gmv = d.pop("live_gmv", UNSET)
        live_gmv: LiveGmv | Unset
        if isinstance(_live_gmv, Unset):
            live_gmv = UNSET
        else:
            live_gmv = LiveGmv.from_dict(_live_gmv)

        _live_indirect_gmv = d.pop("live_indirect_gmv", UNSET)
        live_indirect_gmv: LiveIndirectGmv | Unset
        if isinstance(_live_indirect_gmv, Unset):
            live_indirect_gmv = UNSET
        else:
            live_indirect_gmv = LiveIndirectGmv.from_dict(_live_indirect_gmv)

        _show_gpm = d.pop("show_gpm", UNSET)
        show_gpm: ShowGpm | Unset
        if isinstance(_show_gpm, Unset):
            show_gpm = UNSET
        else:
            show_gpm = ShowGpm.from_dict(_show_gpm)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)

        views = d.pop("views", UNSET)

        get_shop_live_performance_overview_response_data_performance_interval = cls(
            avg_live_auction_price=avg_live_auction_price,
            avg_viewing_duration=avg_viewing_duration,
            ctor_sku_order=ctor_sku_order,
            end_date=end_date,
            live_attributed_gmv=live_attributed_gmv,
            live_attributed_items_sold=live_attributed_items_sold,
            live_attributed_sku_orders=live_attributed_sku_orders,
            live_auction_attributed_gmv=live_auction_attributed_gmv,
            live_auction_attributed_items_sold=live_auction_attributed_items_sold,
            live_auction_attributed_sku_orders=live_auction_attributed_sku_orders,
            live_ctr=live_ctr,
            live_gmv=live_gmv,
            live_indirect_gmv=live_indirect_gmv,
            show_gpm=show_gpm,
            start_date=start_date,
            views=views,
        )

        get_shop_live_performance_overview_response_data_performance_interval.additional_properties = d
        return get_shop_live_performance_overview_response_data_performance_interval

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
