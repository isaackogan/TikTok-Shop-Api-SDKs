from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_shop_performance_response_data_performance_interval_sale_video_gmv import GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv
  from ..models.get_shop_video_performance_overview_response_data_performance_interval_shoppable_video_attributed_gmv import GetShopVideoPerformanceOverviewResponseDataPerformanceIntervalShoppableVideoAttributedGmv
  from ..models.gpm import Gpm
  from ..models.video_attributed_gmv import VideoAttributedGmv
  from ..models.video_indirect_gmv import VideoIndirectGmv





T = TypeVar("T", bound="GetShopVideoPerformanceOverviewResponseDataPerformanceInterval")



@_attrs_define
class GetShopVideoPerformanceOverviewResponseDataPerformanceInterval:
    """ 
        Attributes:
            avg_daily_customers (int | Unset): Daily average number of customers.
            ctor_sku_order (str | Unset): Conversion rate from product clicks to SKU orders in raw decimal format.
            ctr (str | Unset): Ratio of product clicks to video views in raw decimal format.
            end_date (datetime.date | Unset): End date of the interval (ISO 8601 YYYY-MM-DD format) in shop registered
                timezone, exclusive.
            gpm (Gpm | Unset):
            product_clicks (int | Unset): The number of product clicks from videos.
            product_impressions (int | Unset): The number of impressions of all video products.
            shoppable_video_attributed_gmv
                (GetShopVideoPerformanceOverviewResponseDataPerformanceIntervalShoppableVideoAttributedGmv | Unset):
            start_date (datetime.date | Unset): Start date of the interval (ISO 8601 YYYY-MM-DD format) in shop registered
                timezone, inclusive.
            today (bool | Unset): Whether the interval contains real-time data for today.
            video_attributed_gmv (VideoAttributedGmv | Unset):
            video_attributed_sku_orders (int | Unset): The number of paid SKU orders attributed to videos.
            video_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv | Unset):
            video_indirect_gmv (VideoIndirectGmv | Unset):
            video_product_viewers (int | Unset): The number of users who viewed products from videos. Returned only for
                offline data.
            video_views (int | Unset): The number of video views. Returned only for offline data.
     """

    avg_daily_customers: int | Unset = UNSET
    ctor_sku_order: str | Unset = UNSET
    ctr: str | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    gpm: Gpm | Unset = UNSET
    product_clicks: int | Unset = UNSET
    product_impressions: int | Unset = UNSET
    shoppable_video_attributed_gmv: GetShopVideoPerformanceOverviewResponseDataPerformanceIntervalShoppableVideoAttributedGmv | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    today: bool | Unset = UNSET
    video_attributed_gmv: VideoAttributedGmv | Unset = UNSET
    video_attributed_sku_orders: int | Unset = UNSET
    video_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv | Unset = UNSET
    video_indirect_gmv: VideoIndirectGmv | Unset = UNSET
    video_product_viewers: int | Unset = UNSET
    video_views: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_performance_response_data_performance_interval_sale_video_gmv import GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv # noqa: PLC0415
        from ..models.get_shop_video_performance_overview_response_data_performance_interval_shoppable_video_attributed_gmv import GetShopVideoPerformanceOverviewResponseDataPerformanceIntervalShoppableVideoAttributedGmv # noqa: PLC0415
        from ..models.gpm import Gpm # noqa: PLC0415
        from ..models.video_attributed_gmv import VideoAttributedGmv # noqa: PLC0415
        from ..models.video_indirect_gmv import VideoIndirectGmv # noqa: PLC0415
        avg_daily_customers = self.avg_daily_customers

        ctor_sku_order = self.ctor_sku_order

        ctr = self.ctr

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpm, Unset):
            gpm = self.gpm.to_dict()

        product_clicks = self.product_clicks

        product_impressions = self.product_impressions

        shoppable_video_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shoppable_video_attributed_gmv, Unset):
            shoppable_video_attributed_gmv = self.shoppable_video_attributed_gmv.to_dict()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        today = self.today

        video_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_attributed_gmv, Unset):
            video_attributed_gmv = self.video_attributed_gmv.to_dict()

        video_attributed_sku_orders = self.video_attributed_sku_orders

        video_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_gmv, Unset):
            video_gmv = self.video_gmv.to_dict()

        video_indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_indirect_gmv, Unset):
            video_indirect_gmv = self.video_indirect_gmv.to_dict()

        video_product_viewers = self.video_product_viewers

        video_views = self.video_views


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if avg_daily_customers is not UNSET:
            field_dict["avg_daily_customers"] = avg_daily_customers
        if ctor_sku_order is not UNSET:
            field_dict["ctor_sku_order"] = ctor_sku_order
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if gpm is not UNSET:
            field_dict["gpm"] = gpm
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if shoppable_video_attributed_gmv is not UNSET:
            field_dict["shoppable_video_attributed_gmv"] = shoppable_video_attributed_gmv
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if today is not UNSET:
            field_dict["today"] = today
        if video_attributed_gmv is not UNSET:
            field_dict["video_attributed_gmv"] = video_attributed_gmv
        if video_attributed_sku_orders is not UNSET:
            field_dict["video_attributed_sku_orders"] = video_attributed_sku_orders
        if video_gmv is not UNSET:
            field_dict["video_gmv"] = video_gmv
        if video_indirect_gmv is not UNSET:
            field_dict["video_indirect_gmv"] = video_indirect_gmv
        if video_product_viewers is not UNSET:
            field_dict["video_product_viewers"] = video_product_viewers
        if video_views is not UNSET:
            field_dict["video_views"] = video_views

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_performance_response_data_performance_interval_sale_video_gmv import GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv # noqa: PLC0415
        from ..models.get_shop_video_performance_overview_response_data_performance_interval_shoppable_video_attributed_gmv import GetShopVideoPerformanceOverviewResponseDataPerformanceIntervalShoppableVideoAttributedGmv # noqa: PLC0415
        from ..models.gpm import Gpm # noqa: PLC0415
        from ..models.video_attributed_gmv import VideoAttributedGmv # noqa: PLC0415
        from ..models.video_indirect_gmv import VideoIndirectGmv # noqa: PLC0415
        d = dict(src_dict)
        avg_daily_customers = d.pop("avg_daily_customers", UNSET)

        ctor_sku_order = d.pop("ctor_sku_order", UNSET)

        ctr = d.pop("ctr", UNSET)

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        _gpm = d.pop("gpm", UNSET)
        gpm: Gpm | Unset
        if isinstance(_gpm,  Unset):
            gpm = UNSET
        else:
            gpm = Gpm.from_dict(_gpm)




        product_clicks = d.pop("product_clicks", UNSET)

        product_impressions = d.pop("product_impressions", UNSET)

        _shoppable_video_attributed_gmv = d.pop("shoppable_video_attributed_gmv", UNSET)
        shoppable_video_attributed_gmv: GetShopVideoPerformanceOverviewResponseDataPerformanceIntervalShoppableVideoAttributedGmv | Unset
        if isinstance(_shoppable_video_attributed_gmv,  Unset):
            shoppable_video_attributed_gmv = UNSET
        else:
            shoppable_video_attributed_gmv = GetShopVideoPerformanceOverviewResponseDataPerformanceIntervalShoppableVideoAttributedGmv.from_dict(_shoppable_video_attributed_gmv)




        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        today = d.pop("today", UNSET)

        _video_attributed_gmv = d.pop("video_attributed_gmv", UNSET)
        video_attributed_gmv: VideoAttributedGmv | Unset
        if isinstance(_video_attributed_gmv,  Unset):
            video_attributed_gmv = UNSET
        else:
            video_attributed_gmv = VideoAttributedGmv.from_dict(_video_attributed_gmv)




        video_attributed_sku_orders = d.pop("video_attributed_sku_orders", UNSET)

        _video_gmv = d.pop("video_gmv", UNSET)
        video_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv | Unset
        if isinstance(_video_gmv,  Unset):
            video_gmv = UNSET
        else:
            video_gmv = GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv.from_dict(_video_gmv)




        _video_indirect_gmv = d.pop("video_indirect_gmv", UNSET)
        video_indirect_gmv: VideoIndirectGmv | Unset
        if isinstance(_video_indirect_gmv,  Unset):
            video_indirect_gmv = UNSET
        else:
            video_indirect_gmv = VideoIndirectGmv.from_dict(_video_indirect_gmv)




        video_product_viewers = d.pop("video_product_viewers", UNSET)

        video_views = d.pop("video_views", UNSET)

        get_shop_video_performance_overview_response_data_performance_interval = cls(
            avg_daily_customers=avg_daily_customers,
            ctor_sku_order=ctor_sku_order,
            ctr=ctr,
            end_date=end_date,
            gpm=gpm,
            product_clicks=product_clicks,
            product_impressions=product_impressions,
            shoppable_video_attributed_gmv=shoppable_video_attributed_gmv,
            start_date=start_date,
            today=today,
            video_attributed_gmv=video_attributed_gmv,
            video_attributed_sku_orders=video_attributed_sku_orders,
            video_gmv=video_gmv,
            video_indirect_gmv=video_indirect_gmv,
            video_product_viewers=video_product_viewers,
            video_views=video_views,
        )


        get_shop_video_performance_overview_response_data_performance_interval.additional_properties = d
        return get_shop_video_performance_overview_response_data_performance_interval

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
