from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aov import Aov
    from ..models.avg_live_auction_price import AvgLiveAuctionPrice
    from ..models.avg_price import AvgPrice
    from ..models.get_shop_live_performance_list_response_data_live_stream_session_sales_performance_gmv_with_tiktok_coupon import (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceGmvWithTiktokCoupon,
    )
    from ..models.get_shop_live_performance_list_response_data_live_stream_session_sales_performance_live_auction_gmv import (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionGmv,
    )
    from ..models.get_shop_live_performance_list_response_data_live_stream_session_sales_performance_live_auction_indirect_gmv import (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionIndirectGmv,
    )
    from ..models.live_attributed_gmv import LiveAttributedGmv
    from ..models.live_auction_attributed_gmv import LiveAuctionAttributedGmv
    from ..models.live_gmv import LiveGmv
    from ..models.live_indirect_gmv import LiveIndirectGmv


T = TypeVar("T", bound="GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformance")


@_attrs_define
class GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformance:
    """
    Attributes:
        aov (Aov | Unset):
        attributed_customers (int | Unset): Number of customers attributed to the LIVE session.
        avg_live_auction_price (AvgLiveAuctionPrice | Unset):
        avg_price (AvgPrice | Unset):
        created_sku_orders (int | Unset): The total number of orders created during the selected period, including those
            with pending payment for cash-on-delivery or PayLater. Example: If a customer orders 3 units of SKU A and 2
            units of SKU B, the SKU orders would be 2.
        gmv_with_tiktok_coupons
            (GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceGmvWithTiktokCoupon | Unset):
        live_attributed_gmv (LiveAttributedGmv | Unset):
        live_attributed_items_sold (int | Unset): Number of items sold attributed to the LIVE session.
        live_attributed_orders (int | Unset): Number of orders attributed to the LIVE session.
        live_attributed_sku_orders (int | Unset): Number of paid SKU orders attributed to the LIVE session.
        live_auction_attributed_gmv (LiveAuctionAttributedGmv | Unset):
        live_auction_attributed_items_sold (int | Unset): Number of items sold attributed to LIVE auction products.
        live_auction_attributed_sku_orders (int | Unset): Number of paid SKU orders attributed to LIVE auction products.
        live_auction_gmv (GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionGmv |
            Unset):
        live_auction_indirect_gmv
            (GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionIndirectGmv | Unset):
        live_gmv (LiveGmv | Unset):
        live_indirect_gmv (LiveIndirectGmv | Unset):
        payment_rate (str | Unset): Ratio of paid orders to created orders. Expressed as a raw decimal string.
        products_sold (int | Unset): Number of distinct products sold from the LIVE session.
    """

    aov: Aov | Unset = UNSET
    attributed_customers: int | Unset = UNSET
    avg_live_auction_price: AvgLiveAuctionPrice | Unset = UNSET
    avg_price: AvgPrice | Unset = UNSET
    created_sku_orders: int | Unset = UNSET
    gmv_with_tiktok_coupons: (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceGmvWithTiktokCoupon | Unset
    ) = UNSET
    live_attributed_gmv: LiveAttributedGmv | Unset = UNSET
    live_attributed_items_sold: int | Unset = UNSET
    live_attributed_orders: int | Unset = UNSET
    live_attributed_sku_orders: int | Unset = UNSET
    live_auction_attributed_gmv: LiveAuctionAttributedGmv | Unset = UNSET
    live_auction_attributed_items_sold: int | Unset = UNSET
    live_auction_attributed_sku_orders: int | Unset = UNSET
    live_auction_gmv: GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionGmv | Unset = (
        UNSET
    )
    live_auction_indirect_gmv: (
        GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionIndirectGmv | Unset
    ) = UNSET
    live_gmv: LiveGmv | Unset = UNSET
    live_indirect_gmv: LiveIndirectGmv | Unset = UNSET
    payment_rate: str | Unset = UNSET
    products_sold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aov: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aov, Unset):
            aov = self.aov.to_dict()

        attributed_customers = self.attributed_customers

        avg_live_auction_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_live_auction_price, Unset):
            avg_live_auction_price = self.avg_live_auction_price.to_dict()

        avg_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_price, Unset):
            avg_price = self.avg_price.to_dict()

        created_sku_orders = self.created_sku_orders

        gmv_with_tiktok_coupons: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv_with_tiktok_coupons, Unset):
            gmv_with_tiktok_coupons = self.gmv_with_tiktok_coupons.to_dict()

        live_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_attributed_gmv, Unset):
            live_attributed_gmv = self.live_attributed_gmv.to_dict()

        live_attributed_items_sold = self.live_attributed_items_sold

        live_attributed_orders = self.live_attributed_orders

        live_attributed_sku_orders = self.live_attributed_sku_orders

        live_auction_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_auction_attributed_gmv, Unset):
            live_auction_attributed_gmv = self.live_auction_attributed_gmv.to_dict()

        live_auction_attributed_items_sold = self.live_auction_attributed_items_sold

        live_auction_attributed_sku_orders = self.live_auction_attributed_sku_orders

        live_auction_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_auction_gmv, Unset):
            live_auction_gmv = self.live_auction_gmv.to_dict()

        live_auction_indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_auction_indirect_gmv, Unset):
            live_auction_indirect_gmv = self.live_auction_indirect_gmv.to_dict()

        live_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_gmv, Unset):
            live_gmv = self.live_gmv.to_dict()

        live_indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_indirect_gmv, Unset):
            live_indirect_gmv = self.live_indirect_gmv.to_dict()

        payment_rate = self.payment_rate

        products_sold = self.products_sold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aov is not UNSET:
            field_dict["aov"] = aov
        if attributed_customers is not UNSET:
            field_dict["attributed_customers"] = attributed_customers
        if avg_live_auction_price is not UNSET:
            field_dict["avg_live_auction_price"] = avg_live_auction_price
        if avg_price is not UNSET:
            field_dict["avg_price"] = avg_price
        if created_sku_orders is not UNSET:
            field_dict["created_sku_orders"] = created_sku_orders
        if gmv_with_tiktok_coupons is not UNSET:
            field_dict["gmv_with_tiktok_coupons"] = gmv_with_tiktok_coupons
        if live_attributed_gmv is not UNSET:
            field_dict["live_attributed_gmv"] = live_attributed_gmv
        if live_attributed_items_sold is not UNSET:
            field_dict["live_attributed_items_sold"] = live_attributed_items_sold
        if live_attributed_orders is not UNSET:
            field_dict["live_attributed_orders"] = live_attributed_orders
        if live_attributed_sku_orders is not UNSET:
            field_dict["live_attributed_sku_orders"] = live_attributed_sku_orders
        if live_auction_attributed_gmv is not UNSET:
            field_dict["live_auction_attributed_gmv"] = live_auction_attributed_gmv
        if live_auction_attributed_items_sold is not UNSET:
            field_dict["live_auction_attributed_items_sold"] = live_auction_attributed_items_sold
        if live_auction_attributed_sku_orders is not UNSET:
            field_dict["live_auction_attributed_sku_orders"] = live_auction_attributed_sku_orders
        if live_auction_gmv is not UNSET:
            field_dict["live_auction_gmv"] = live_auction_gmv
        if live_auction_indirect_gmv is not UNSET:
            field_dict["live_auction_indirect_gmv"] = live_auction_indirect_gmv
        if live_gmv is not UNSET:
            field_dict["live_gmv"] = live_gmv
        if live_indirect_gmv is not UNSET:
            field_dict["live_indirect_gmv"] = live_indirect_gmv
        if payment_rate is not UNSET:
            field_dict["payment_rate"] = payment_rate
        if products_sold is not UNSET:
            field_dict["products_sold"] = products_sold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aov import Aov  # noqa: PLC0415
        from ..models.avg_live_auction_price import AvgLiveAuctionPrice  # noqa: PLC0415
        from ..models.avg_price import AvgPrice  # noqa: PLC0415
        from ..models.get_shop_live_performance_list_response_data_live_stream_session_sales_performance_gmv_with_tiktok_coupon import (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceGmvWithTiktokCoupon,  # noqa: PLC0415
        )
        from ..models.get_shop_live_performance_list_response_data_live_stream_session_sales_performance_live_auction_gmv import (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_live_performance_list_response_data_live_stream_session_sales_performance_live_auction_indirect_gmv import (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionIndirectGmv,  # noqa: PLC0415
        )
        from ..models.live_attributed_gmv import LiveAttributedGmv  # noqa: PLC0415
        from ..models.live_auction_attributed_gmv import LiveAuctionAttributedGmv  # noqa: PLC0415
        from ..models.live_gmv import LiveGmv  # noqa: PLC0415
        from ..models.live_indirect_gmv import LiveIndirectGmv  # noqa: PLC0415

        d = dict(src_dict)
        _aov = d.pop("aov", UNSET)
        aov: Aov | Unset
        if isinstance(_aov, Unset):
            aov = UNSET
        else:
            aov = Aov.from_dict(_aov)

        attributed_customers = d.pop("attributed_customers", UNSET)

        _avg_live_auction_price = d.pop("avg_live_auction_price", UNSET)
        avg_live_auction_price: AvgLiveAuctionPrice | Unset
        if isinstance(_avg_live_auction_price, Unset):
            avg_live_auction_price = UNSET
        else:
            avg_live_auction_price = AvgLiveAuctionPrice.from_dict(_avg_live_auction_price)

        _avg_price = d.pop("avg_price", UNSET)
        avg_price: AvgPrice | Unset
        if isinstance(_avg_price, Unset):
            avg_price = UNSET
        else:
            avg_price = AvgPrice.from_dict(_avg_price)

        created_sku_orders = d.pop("created_sku_orders", UNSET)

        _gmv_with_tiktok_coupons = d.pop("gmv_with_tiktok_coupons", UNSET)
        gmv_with_tiktok_coupons: (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceGmvWithTiktokCoupon | Unset
        )
        if isinstance(_gmv_with_tiktok_coupons, Unset):
            gmv_with_tiktok_coupons = UNSET
        else:
            gmv_with_tiktok_coupons = (
                GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceGmvWithTiktokCoupon.from_dict(
                    _gmv_with_tiktok_coupons
                )
            )

        _live_attributed_gmv = d.pop("live_attributed_gmv", UNSET)
        live_attributed_gmv: LiveAttributedGmv | Unset
        if isinstance(_live_attributed_gmv, Unset):
            live_attributed_gmv = UNSET
        else:
            live_attributed_gmv = LiveAttributedGmv.from_dict(_live_attributed_gmv)

        live_attributed_items_sold = d.pop("live_attributed_items_sold", UNSET)

        live_attributed_orders = d.pop("live_attributed_orders", UNSET)

        live_attributed_sku_orders = d.pop("live_attributed_sku_orders", UNSET)

        _live_auction_attributed_gmv = d.pop("live_auction_attributed_gmv", UNSET)
        live_auction_attributed_gmv: LiveAuctionAttributedGmv | Unset
        if isinstance(_live_auction_attributed_gmv, Unset):
            live_auction_attributed_gmv = UNSET
        else:
            live_auction_attributed_gmv = LiveAuctionAttributedGmv.from_dict(_live_auction_attributed_gmv)

        live_auction_attributed_items_sold = d.pop("live_auction_attributed_items_sold", UNSET)

        live_auction_attributed_sku_orders = d.pop("live_auction_attributed_sku_orders", UNSET)

        _live_auction_gmv = d.pop("live_auction_gmv", UNSET)
        live_auction_gmv: GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionGmv | Unset
        if isinstance(_live_auction_gmv, Unset):
            live_auction_gmv = UNSET
        else:
            live_auction_gmv = (
                GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionGmv.from_dict(
                    _live_auction_gmv
                )
            )

        _live_auction_indirect_gmv = d.pop("live_auction_indirect_gmv", UNSET)
        live_auction_indirect_gmv: (
            GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionIndirectGmv | Unset
        )
        if isinstance(_live_auction_indirect_gmv, Unset):
            live_auction_indirect_gmv = UNSET
        else:
            live_auction_indirect_gmv = (
                GetShopLIVEPerformanceListResponseDataLiveStreamSessionSalesPerformanceLiveAuctionIndirectGmv.from_dict(
                    _live_auction_indirect_gmv
                )
            )

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

        payment_rate = d.pop("payment_rate", UNSET)

        products_sold = d.pop("products_sold", UNSET)

        get_shop_live_performance_list_response_data_live_stream_session_sales_performance = cls(
            aov=aov,
            attributed_customers=attributed_customers,
            avg_live_auction_price=avg_live_auction_price,
            avg_price=avg_price,
            created_sku_orders=created_sku_orders,
            gmv_with_tiktok_coupons=gmv_with_tiktok_coupons,
            live_attributed_gmv=live_attributed_gmv,
            live_attributed_items_sold=live_attributed_items_sold,
            live_attributed_orders=live_attributed_orders,
            live_attributed_sku_orders=live_attributed_sku_orders,
            live_auction_attributed_gmv=live_auction_attributed_gmv,
            live_auction_attributed_items_sold=live_auction_attributed_items_sold,
            live_auction_attributed_sku_orders=live_auction_attributed_sku_orders,
            live_auction_gmv=live_auction_gmv,
            live_auction_indirect_gmv=live_auction_indirect_gmv,
            live_gmv=live_gmv,
            live_indirect_gmv=live_indirect_gmv,
            payment_rate=payment_rate,
            products_sold=products_sold,
        )

        get_shop_live_performance_list_response_data_live_stream_session_sales_performance.additional_properties = d
        return get_shop_live_performance_list_response_data_live_stream_session_sales_performance

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
