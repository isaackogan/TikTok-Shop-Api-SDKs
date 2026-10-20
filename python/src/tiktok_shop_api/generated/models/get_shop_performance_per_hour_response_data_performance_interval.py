from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.avg_order_value import AvgOrderValue
  from ..models.avg_sku_order_value import AvgSkuOrderValue
  from ..models.gmv import Gmv
  from ..models.live_attributed_gmv import LiveAttributedGmv
  from ..models.product_card_attributed_gmv import ProductCardAttributedGmv
  from ..models.video_attributed_gmv import VideoAttributedGmv





T = TypeVar("T", bound="GetShopPerformancePerHourResponseDataPerformanceInterval")



@_attrs_define
class GetShopPerformancePerHourResponseDataPerformanceInterval:
    """ 
        Attributes:
            avg_order_value (AvgOrderValue | Unset):
            avg_sku_order_value (AvgSkuOrderValue | Unset):
            customers (int | Unset): The number of individual customers who made a purchase. This metric counts each
                customer once, even if they made multiple purchases.
            customers_count (int | Unset): Number of unique users who paid for orders during the hour.
            gmv (Gmv | Unset):
            index (int | Unset): hour index, 0-23.
                0 means 00:00 - 00:59.
            items_sold (int | Unset): The total number of individual items sold. Example: If a customer buys 3 units of SKU
                A and 2 units of SKU B, the items sold would be 5.
            live_attributed_gmv (LiveAttributedGmv | Unset):
            orders_count (int | Unset): The number of paid orders during the hour.
            product_card_attributed_gmv (ProductCardAttributedGmv | Unset):
            product_clicks (int | Unset): Total number of product clicks during the hour.
            product_impressions (int | Unset): Total number of product impressions during the hour.
            sku_orders_count (int | Unset): The number of distinct SKUs sold during the hour.
            unique_clicks (int | Unset): Total number of unique product clicks during the hour.
            unique_product_impressions (int | Unset): Total number of unique product impressions during the hour.
            video_attributed_gmv (VideoAttributedGmv | Unset):
            visitors (int | Unset): Number of unique users who visited your product detail pages before the most recent
                update time.
     """

    avg_order_value: AvgOrderValue | Unset = UNSET
    avg_sku_order_value: AvgSkuOrderValue | Unset = UNSET
    customers: int | Unset = UNSET
    customers_count: int | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    index: int | Unset = UNSET
    items_sold: int | Unset = UNSET
    live_attributed_gmv: LiveAttributedGmv | Unset = UNSET
    orders_count: int | Unset = UNSET
    product_card_attributed_gmv: ProductCardAttributedGmv | Unset = UNSET
    product_clicks: int | Unset = UNSET
    product_impressions: int | Unset = UNSET
    sku_orders_count: int | Unset = UNSET
    unique_clicks: int | Unset = UNSET
    unique_product_impressions: int | Unset = UNSET
    video_attributed_gmv: VideoAttributedGmv | Unset = UNSET
    visitors: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.avg_order_value import AvgOrderValue # noqa: PLC0415
        from ..models.avg_sku_order_value import AvgSkuOrderValue # noqa: PLC0415
        from ..models.gmv import Gmv # noqa: PLC0415
        from ..models.live_attributed_gmv import LiveAttributedGmv # noqa: PLC0415
        from ..models.product_card_attributed_gmv import ProductCardAttributedGmv # noqa: PLC0415
        from ..models.video_attributed_gmv import VideoAttributedGmv # noqa: PLC0415
        avg_order_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_order_value, Unset):
            avg_order_value = self.avg_order_value.to_dict()

        avg_sku_order_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_sku_order_value, Unset):
            avg_sku_order_value = self.avg_sku_order_value.to_dict()

        customers = self.customers

        customers_count = self.customers_count

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        index = self.index

        items_sold = self.items_sold

        live_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_attributed_gmv, Unset):
            live_attributed_gmv = self.live_attributed_gmv.to_dict()

        orders_count = self.orders_count

        product_card_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_card_attributed_gmv, Unset):
            product_card_attributed_gmv = self.product_card_attributed_gmv.to_dict()

        product_clicks = self.product_clicks

        product_impressions = self.product_impressions

        sku_orders_count = self.sku_orders_count

        unique_clicks = self.unique_clicks

        unique_product_impressions = self.unique_product_impressions

        video_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_attributed_gmv, Unset):
            video_attributed_gmv = self.video_attributed_gmv.to_dict()

        visitors = self.visitors


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if avg_order_value is not UNSET:
            field_dict["avg_order_value"] = avg_order_value
        if avg_sku_order_value is not UNSET:
            field_dict["avg_sku_order_value"] = avg_sku_order_value
        if customers is not UNSET:
            field_dict["customers"] = customers
        if customers_count is not UNSET:
            field_dict["customers_count"] = customers_count
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if index is not UNSET:
            field_dict["index"] = index
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if live_attributed_gmv is not UNSET:
            field_dict["live_attributed_gmv"] = live_attributed_gmv
        if orders_count is not UNSET:
            field_dict["orders_count"] = orders_count
        if product_card_attributed_gmv is not UNSET:
            field_dict["product_card_attributed_gmv"] = product_card_attributed_gmv
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if sku_orders_count is not UNSET:
            field_dict["sku_orders_count"] = sku_orders_count
        if unique_clicks is not UNSET:
            field_dict["unique_clicks"] = unique_clicks
        if unique_product_impressions is not UNSET:
            field_dict["unique_product_impressions"] = unique_product_impressions
        if video_attributed_gmv is not UNSET:
            field_dict["video_attributed_gmv"] = video_attributed_gmv
        if visitors is not UNSET:
            field_dict["visitors"] = visitors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avg_order_value import AvgOrderValue # noqa: PLC0415
        from ..models.avg_sku_order_value import AvgSkuOrderValue # noqa: PLC0415
        from ..models.gmv import Gmv # noqa: PLC0415
        from ..models.live_attributed_gmv import LiveAttributedGmv # noqa: PLC0415
        from ..models.product_card_attributed_gmv import ProductCardAttributedGmv # noqa: PLC0415
        from ..models.video_attributed_gmv import VideoAttributedGmv # noqa: PLC0415
        d = dict(src_dict)
        _avg_order_value = d.pop("avg_order_value", UNSET)
        avg_order_value: AvgOrderValue | Unset
        if isinstance(_avg_order_value,  Unset):
            avg_order_value = UNSET
        else:
            avg_order_value = AvgOrderValue.from_dict(_avg_order_value)




        _avg_sku_order_value = d.pop("avg_sku_order_value", UNSET)
        avg_sku_order_value: AvgSkuOrderValue | Unset
        if isinstance(_avg_sku_order_value,  Unset):
            avg_sku_order_value = UNSET
        else:
            avg_sku_order_value = AvgSkuOrderValue.from_dict(_avg_sku_order_value)




        customers = d.pop("customers", UNSET)

        customers_count = d.pop("customers_count", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)




        index = d.pop("index", UNSET)

        items_sold = d.pop("items_sold", UNSET)

        _live_attributed_gmv = d.pop("live_attributed_gmv", UNSET)
        live_attributed_gmv: LiveAttributedGmv | Unset
        if isinstance(_live_attributed_gmv,  Unset):
            live_attributed_gmv = UNSET
        else:
            live_attributed_gmv = LiveAttributedGmv.from_dict(_live_attributed_gmv)




        orders_count = d.pop("orders_count", UNSET)

        _product_card_attributed_gmv = d.pop("product_card_attributed_gmv", UNSET)
        product_card_attributed_gmv: ProductCardAttributedGmv | Unset
        if isinstance(_product_card_attributed_gmv,  Unset):
            product_card_attributed_gmv = UNSET
        else:
            product_card_attributed_gmv = ProductCardAttributedGmv.from_dict(_product_card_attributed_gmv)




        product_clicks = d.pop("product_clicks", UNSET)

        product_impressions = d.pop("product_impressions", UNSET)

        sku_orders_count = d.pop("sku_orders_count", UNSET)

        unique_clicks = d.pop("unique_clicks", UNSET)

        unique_product_impressions = d.pop("unique_product_impressions", UNSET)

        _video_attributed_gmv = d.pop("video_attributed_gmv", UNSET)
        video_attributed_gmv: VideoAttributedGmv | Unset
        if isinstance(_video_attributed_gmv,  Unset):
            video_attributed_gmv = UNSET
        else:
            video_attributed_gmv = VideoAttributedGmv.from_dict(_video_attributed_gmv)




        visitors = d.pop("visitors", UNSET)

        get_shop_performance_per_hour_response_data_performance_interval = cls(
            avg_order_value=avg_order_value,
            avg_sku_order_value=avg_sku_order_value,
            customers=customers,
            customers_count=customers_count,
            gmv=gmv,
            index=index,
            items_sold=items_sold,
            live_attributed_gmv=live_attributed_gmv,
            orders_count=orders_count,
            product_card_attributed_gmv=product_card_attributed_gmv,
            product_clicks=product_clicks,
            product_impressions=product_impressions,
            sku_orders_count=sku_orders_count,
            unique_clicks=unique_clicks,
            unique_product_impressions=unique_product_impressions,
            video_attributed_gmv=video_attributed_gmv,
            visitors=visitors,
        )


        get_shop_performance_per_hour_response_data_performance_interval.additional_properties = d
        return get_shop_performance_per_hour_response_data_performance_interval

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
