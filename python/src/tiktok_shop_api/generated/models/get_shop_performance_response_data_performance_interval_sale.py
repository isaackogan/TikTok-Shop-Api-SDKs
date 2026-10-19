from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avg_order_value import AvgOrderValue
    from ..models.avg_sku_order_value import AvgSkuOrderValue
    from ..models.get_shop_performance_response_data_performance_interval_sale_creator_live_attributed_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveAttributedGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_creator_live_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_creator_live_indirect_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveIndirectGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_creator_video_attributed_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoAttributedGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_creator_video_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_creator_video_indirect_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoIndirectGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_gmv_with_tax import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTax,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_gmv_with_tiktok_co_funding import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTiktokCoFunding,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_seller_live_attributed_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveAttributedGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_seller_live_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_seller_live_indirect_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveIndirectGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_seller_video_attributed_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoAttributedGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_seller_video_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_seller_video_indirect_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoIndirectGmv,
    )
    from ..models.get_shop_performance_response_data_performance_interval_sale_video_gmv import (
        GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv,
    )
    from ..models.gmv import Gmv
    from ..models.live_attributed_gmv import LiveAttributedGmv
    from ..models.live_gmv import LiveGmv
    from ..models.live_indirect_gmv import LiveIndirectGmv
    from ..models.product_card_attributed_gmv import ProductCardAttributedGmv
    from ..models.refund import Refund
    from ..models.shipping_fee import ShippingFee
    from ..models.tax import Tax
    from ..models.video_attributed_gmv import VideoAttributedGmv
    from ..models.video_indirect_gmv import VideoIndirectGmv


T = TypeVar("T", bound="GetShopPerformanceResponseDataPerformanceIntervalSale")


@_attrs_define
class GetShopPerformanceResponseDataPerformanceIntervalSale:
    """
    Attributes:
        avg_order_value (AvgOrderValue | Unset):
        avg_sku_order_value (AvgSkuOrderValue | Unset):
        cancellations_and_returns (int | Unset): Total number of cancellations and returns during the selected period.
        creator_live_attributed_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveAttributedGmv |
            Unset):
        creator_live_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveGmv | Unset):
        creator_live_indirect_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveIndirectGmv | Unset):
        creator_video_attributed_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoAttributedGmv |
            Unset):
        creator_video_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoGmv | Unset):
        creator_video_indirect_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoIndirectGmv |
            Unset):
        customers_count (int | Unset): Number of unique users who paid for orders during the selected period.
        gmv (Gmv | Unset):
        gmv_with_tax (GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTax | Unset):
        gmv_with_tiktok_co_funding (GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTiktokCoFunding |
            Unset):
        items_sold (int | Unset): The total number of individual items sold. Example: If a customer buys 3 units of SKU
            A and 2 units of SKU B, the items sold would be 5.
        live_attributed_gmv (LiveAttributedGmv | Unset):
        live_gmv (LiveGmv | Unset):
        live_indirect_gmv (LiveIndirectGmv | Unset):
        orders_count (int | Unset): The number of paid orders during the selected period.
        product_card_attributed_gmv (ProductCardAttributedGmv | Unset):
        refunds (Refund | Unset):
        seller_live_attributed_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveAttributedGmv |
            Unset):
        seller_live_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveGmv | Unset):
        seller_live_indirect_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveIndirectGmv | Unset):
        seller_video_attributed_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoAttributedGmv |
            Unset):
        seller_video_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoGmv | Unset):
        seller_video_indirect_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoIndirectGmv | Unset):
        shipping_fees (ShippingFee | Unset):
        sku_orders_count (int | Unset): A total count of distinct SKUs sold.
        tax (Tax | Unset):
        video_attributed_gmv (VideoAttributedGmv | Unset):
        video_gmv (GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv | Unset):
        video_indirect_gmv (VideoIndirectGmv | Unset):
    """

    avg_order_value: AvgOrderValue | Unset = UNSET
    avg_sku_order_value: AvgSkuOrderValue | Unset = UNSET
    cancellations_and_returns: int | Unset = UNSET
    creator_live_attributed_gmv: (
        GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveAttributedGmv | Unset
    ) = UNSET
    creator_live_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveGmv | Unset = UNSET
    creator_live_indirect_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveIndirectGmv | Unset = (
        UNSET
    )
    creator_video_attributed_gmv: (
        GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoAttributedGmv | Unset
    ) = UNSET
    creator_video_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoGmv | Unset = UNSET
    creator_video_indirect_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoIndirectGmv | Unset = (
        UNSET
    )
    customers_count: int | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    gmv_with_tax: GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTax | Unset = UNSET
    gmv_with_tiktok_co_funding: GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTiktokCoFunding | Unset = (
        UNSET
    )
    items_sold: int | Unset = UNSET
    live_attributed_gmv: LiveAttributedGmv | Unset = UNSET
    live_gmv: LiveGmv | Unset = UNSET
    live_indirect_gmv: LiveIndirectGmv | Unset = UNSET
    orders_count: int | Unset = UNSET
    product_card_attributed_gmv: ProductCardAttributedGmv | Unset = UNSET
    refunds: Refund | Unset = UNSET
    seller_live_attributed_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveAttributedGmv | Unset = (
        UNSET
    )
    seller_live_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveGmv | Unset = UNSET
    seller_live_indirect_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveIndirectGmv | Unset = UNSET
    seller_video_attributed_gmv: (
        GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoAttributedGmv | Unset
    ) = UNSET
    seller_video_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoGmv | Unset = UNSET
    seller_video_indirect_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoIndirectGmv | Unset = (
        UNSET
    )
    shipping_fees: ShippingFee | Unset = UNSET
    sku_orders_count: int | Unset = UNSET
    tax: Tax | Unset = UNSET
    video_attributed_gmv: VideoAttributedGmv | Unset = UNSET
    video_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv | Unset = UNSET
    video_indirect_gmv: VideoIndirectGmv | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_order_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_order_value, Unset):
            avg_order_value = self.avg_order_value.to_dict()

        avg_sku_order_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.avg_sku_order_value, Unset):
            avg_sku_order_value = self.avg_sku_order_value.to_dict()

        cancellations_and_returns = self.cancellations_and_returns

        creator_live_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_live_attributed_gmv, Unset):
            creator_live_attributed_gmv = self.creator_live_attributed_gmv.to_dict()

        creator_live_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_live_gmv, Unset):
            creator_live_gmv = self.creator_live_gmv.to_dict()

        creator_live_indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_live_indirect_gmv, Unset):
            creator_live_indirect_gmv = self.creator_live_indirect_gmv.to_dict()

        creator_video_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_video_attributed_gmv, Unset):
            creator_video_attributed_gmv = self.creator_video_attributed_gmv.to_dict()

        creator_video_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_video_gmv, Unset):
            creator_video_gmv = self.creator_video_gmv.to_dict()

        creator_video_indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_video_indirect_gmv, Unset):
            creator_video_indirect_gmv = self.creator_video_indirect_gmv.to_dict()

        customers_count = self.customers_count

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        gmv_with_tax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv_with_tax, Unset):
            gmv_with_tax = self.gmv_with_tax.to_dict()

        gmv_with_tiktok_co_funding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv_with_tiktok_co_funding, Unset):
            gmv_with_tiktok_co_funding = self.gmv_with_tiktok_co_funding.to_dict()

        items_sold = self.items_sold

        live_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_attributed_gmv, Unset):
            live_attributed_gmv = self.live_attributed_gmv.to_dict()

        live_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_gmv, Unset):
            live_gmv = self.live_gmv.to_dict()

        live_indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_indirect_gmv, Unset):
            live_indirect_gmv = self.live_indirect_gmv.to_dict()

        orders_count = self.orders_count

        product_card_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_card_attributed_gmv, Unset):
            product_card_attributed_gmv = self.product_card_attributed_gmv.to_dict()

        refunds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refunds, Unset):
            refunds = self.refunds.to_dict()

        seller_live_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_live_attributed_gmv, Unset):
            seller_live_attributed_gmv = self.seller_live_attributed_gmv.to_dict()

        seller_live_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_live_gmv, Unset):
            seller_live_gmv = self.seller_live_gmv.to_dict()

        seller_live_indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_live_indirect_gmv, Unset):
            seller_live_indirect_gmv = self.seller_live_indirect_gmv.to_dict()

        seller_video_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_video_attributed_gmv, Unset):
            seller_video_attributed_gmv = self.seller_video_attributed_gmv.to_dict()

        seller_video_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_video_gmv, Unset):
            seller_video_gmv = self.seller_video_gmv.to_dict()

        seller_video_indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_video_indirect_gmv, Unset):
            seller_video_indirect_gmv = self.seller_video_indirect_gmv.to_dict()

        shipping_fees: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping_fees, Unset):
            shipping_fees = self.shipping_fees.to_dict()

        sku_orders_count = self.sku_orders_count

        tax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tax, Unset):
            tax = self.tax.to_dict()

        video_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_attributed_gmv, Unset):
            video_attributed_gmv = self.video_attributed_gmv.to_dict()

        video_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_gmv, Unset):
            video_gmv = self.video_gmv.to_dict()

        video_indirect_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_indirect_gmv, Unset):
            video_indirect_gmv = self.video_indirect_gmv.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_order_value is not UNSET:
            field_dict["avg_order_value"] = avg_order_value
        if avg_sku_order_value is not UNSET:
            field_dict["avg_sku_order_value"] = avg_sku_order_value
        if cancellations_and_returns is not UNSET:
            field_dict["cancellations_and_returns"] = cancellations_and_returns
        if creator_live_attributed_gmv is not UNSET:
            field_dict["creator_live_attributed_gmv"] = creator_live_attributed_gmv
        if creator_live_gmv is not UNSET:
            field_dict["creator_live_gmv"] = creator_live_gmv
        if creator_live_indirect_gmv is not UNSET:
            field_dict["creator_live_indirect_gmv"] = creator_live_indirect_gmv
        if creator_video_attributed_gmv is not UNSET:
            field_dict["creator_video_attributed_gmv"] = creator_video_attributed_gmv
        if creator_video_gmv is not UNSET:
            field_dict["creator_video_gmv"] = creator_video_gmv
        if creator_video_indirect_gmv is not UNSET:
            field_dict["creator_video_indirect_gmv"] = creator_video_indirect_gmv
        if customers_count is not UNSET:
            field_dict["customers_count"] = customers_count
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if gmv_with_tax is not UNSET:
            field_dict["gmv_with_tax"] = gmv_with_tax
        if gmv_with_tiktok_co_funding is not UNSET:
            field_dict["gmv_with_tiktok_co_funding"] = gmv_with_tiktok_co_funding
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if live_attributed_gmv is not UNSET:
            field_dict["live_attributed_gmv"] = live_attributed_gmv
        if live_gmv is not UNSET:
            field_dict["live_gmv"] = live_gmv
        if live_indirect_gmv is not UNSET:
            field_dict["live_indirect_gmv"] = live_indirect_gmv
        if orders_count is not UNSET:
            field_dict["orders_count"] = orders_count
        if product_card_attributed_gmv is not UNSET:
            field_dict["product_card_attributed_gmv"] = product_card_attributed_gmv
        if refunds is not UNSET:
            field_dict["refunds"] = refunds
        if seller_live_attributed_gmv is not UNSET:
            field_dict["seller_live_attributed_gmv"] = seller_live_attributed_gmv
        if seller_live_gmv is not UNSET:
            field_dict["seller_live_gmv"] = seller_live_gmv
        if seller_live_indirect_gmv is not UNSET:
            field_dict["seller_live_indirect_gmv"] = seller_live_indirect_gmv
        if seller_video_attributed_gmv is not UNSET:
            field_dict["seller_video_attributed_gmv"] = seller_video_attributed_gmv
        if seller_video_gmv is not UNSET:
            field_dict["seller_video_gmv"] = seller_video_gmv
        if seller_video_indirect_gmv is not UNSET:
            field_dict["seller_video_indirect_gmv"] = seller_video_indirect_gmv
        if shipping_fees is not UNSET:
            field_dict["shipping_fees"] = shipping_fees
        if sku_orders_count is not UNSET:
            field_dict["sku_orders_count"] = sku_orders_count
        if tax is not UNSET:
            field_dict["tax"] = tax
        if video_attributed_gmv is not UNSET:
            field_dict["video_attributed_gmv"] = video_attributed_gmv
        if video_gmv is not UNSET:
            field_dict["video_gmv"] = video_gmv
        if video_indirect_gmv is not UNSET:
            field_dict["video_indirect_gmv"] = video_indirect_gmv

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.avg_order_value import AvgOrderValue  # noqa: PLC0415
        from ..models.avg_sku_order_value import AvgSkuOrderValue  # noqa: PLC0415
        from ..models.get_shop_performance_response_data_performance_interval_sale_creator_live_attributed_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveAttributedGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_creator_live_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_creator_live_indirect_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveIndirectGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_creator_video_attributed_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoAttributedGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_creator_video_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_creator_video_indirect_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoIndirectGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_gmv_with_tax import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTax,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_gmv_with_tiktok_co_funding import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTiktokCoFunding,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_seller_live_attributed_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveAttributedGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_seller_live_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_seller_live_indirect_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveIndirectGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_seller_video_attributed_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoAttributedGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_seller_video_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_seller_video_indirect_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoIndirectGmv,  # noqa: PLC0415
        )
        from ..models.get_shop_performance_response_data_performance_interval_sale_video_gmv import (
            GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv,  # noqa: PLC0415
        )
        from ..models.gmv import Gmv  # noqa: PLC0415
        from ..models.live_attributed_gmv import LiveAttributedGmv  # noqa: PLC0415
        from ..models.live_gmv import LiveGmv  # noqa: PLC0415
        from ..models.live_indirect_gmv import LiveIndirectGmv  # noqa: PLC0415
        from ..models.product_card_attributed_gmv import ProductCardAttributedGmv  # noqa: PLC0415
        from ..models.refund import Refund  # noqa: PLC0415
        from ..models.shipping_fee import ShippingFee  # noqa: PLC0415
        from ..models.tax import Tax  # noqa: PLC0415
        from ..models.video_attributed_gmv import VideoAttributedGmv  # noqa: PLC0415
        from ..models.video_indirect_gmv import VideoIndirectGmv  # noqa: PLC0415

        d = dict(src_dict)
        _avg_order_value = d.pop("avg_order_value", UNSET)
        avg_order_value: AvgOrderValue | Unset
        if isinstance(_avg_order_value, Unset):
            avg_order_value = UNSET
        else:
            avg_order_value = AvgOrderValue.from_dict(_avg_order_value)

        _avg_sku_order_value = d.pop("avg_sku_order_value", UNSET)
        avg_sku_order_value: AvgSkuOrderValue | Unset
        if isinstance(_avg_sku_order_value, Unset):
            avg_sku_order_value = UNSET
        else:
            avg_sku_order_value = AvgSkuOrderValue.from_dict(_avg_sku_order_value)

        cancellations_and_returns = d.pop("cancellations_and_returns", UNSET)

        _creator_live_attributed_gmv = d.pop("creator_live_attributed_gmv", UNSET)
        creator_live_attributed_gmv: (
            GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveAttributedGmv | Unset
        )
        if isinstance(_creator_live_attributed_gmv, Unset):
            creator_live_attributed_gmv = UNSET
        else:
            creator_live_attributed_gmv = (
                GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveAttributedGmv.from_dict(
                    _creator_live_attributed_gmv
                )
            )

        _creator_live_gmv = d.pop("creator_live_gmv", UNSET)
        creator_live_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveGmv | Unset
        if isinstance(_creator_live_gmv, Unset):
            creator_live_gmv = UNSET
        else:
            creator_live_gmv = GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveGmv.from_dict(
                _creator_live_gmv
            )

        _creator_live_indirect_gmv = d.pop("creator_live_indirect_gmv", UNSET)
        creator_live_indirect_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveIndirectGmv | Unset
        if isinstance(_creator_live_indirect_gmv, Unset):
            creator_live_indirect_gmv = UNSET
        else:
            creator_live_indirect_gmv = (
                GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorLiveIndirectGmv.from_dict(
                    _creator_live_indirect_gmv
                )
            )

        _creator_video_attributed_gmv = d.pop("creator_video_attributed_gmv", UNSET)
        creator_video_attributed_gmv: (
            GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoAttributedGmv | Unset
        )
        if isinstance(_creator_video_attributed_gmv, Unset):
            creator_video_attributed_gmv = UNSET
        else:
            creator_video_attributed_gmv = (
                GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoAttributedGmv.from_dict(
                    _creator_video_attributed_gmv
                )
            )

        _creator_video_gmv = d.pop("creator_video_gmv", UNSET)
        creator_video_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoGmv | Unset
        if isinstance(_creator_video_gmv, Unset):
            creator_video_gmv = UNSET
        else:
            creator_video_gmv = GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoGmv.from_dict(
                _creator_video_gmv
            )

        _creator_video_indirect_gmv = d.pop("creator_video_indirect_gmv", UNSET)
        creator_video_indirect_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoIndirectGmv | Unset
        if isinstance(_creator_video_indirect_gmv, Unset):
            creator_video_indirect_gmv = UNSET
        else:
            creator_video_indirect_gmv = (
                GetShopPerformanceResponseDataPerformanceIntervalSaleCreatorVideoIndirectGmv.from_dict(
                    _creator_video_indirect_gmv
                )
            )

        customers_count = d.pop("customers_count", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv, Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)

        _gmv_with_tax = d.pop("gmv_with_tax", UNSET)
        gmv_with_tax: GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTax | Unset
        if isinstance(_gmv_with_tax, Unset):
            gmv_with_tax = UNSET
        else:
            gmv_with_tax = GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTax.from_dict(_gmv_with_tax)

        _gmv_with_tiktok_co_funding = d.pop("gmv_with_tiktok_co_funding", UNSET)
        gmv_with_tiktok_co_funding: GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTiktokCoFunding | Unset
        if isinstance(_gmv_with_tiktok_co_funding, Unset):
            gmv_with_tiktok_co_funding = UNSET
        else:
            gmv_with_tiktok_co_funding = (
                GetShopPerformanceResponseDataPerformanceIntervalSaleGmvWithTiktokCoFunding.from_dict(
                    _gmv_with_tiktok_co_funding
                )
            )

        items_sold = d.pop("items_sold", UNSET)

        _live_attributed_gmv = d.pop("live_attributed_gmv", UNSET)
        live_attributed_gmv: LiveAttributedGmv | Unset
        if isinstance(_live_attributed_gmv, Unset):
            live_attributed_gmv = UNSET
        else:
            live_attributed_gmv = LiveAttributedGmv.from_dict(_live_attributed_gmv)

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

        orders_count = d.pop("orders_count", UNSET)

        _product_card_attributed_gmv = d.pop("product_card_attributed_gmv", UNSET)
        product_card_attributed_gmv: ProductCardAttributedGmv | Unset
        if isinstance(_product_card_attributed_gmv, Unset):
            product_card_attributed_gmv = UNSET
        else:
            product_card_attributed_gmv = ProductCardAttributedGmv.from_dict(_product_card_attributed_gmv)

        _refunds = d.pop("refunds", UNSET)
        refunds: Refund | Unset
        if isinstance(_refunds, Unset):
            refunds = UNSET
        else:
            refunds = Refund.from_dict(_refunds)

        _seller_live_attributed_gmv = d.pop("seller_live_attributed_gmv", UNSET)
        seller_live_attributed_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveAttributedGmv | Unset
        if isinstance(_seller_live_attributed_gmv, Unset):
            seller_live_attributed_gmv = UNSET
        else:
            seller_live_attributed_gmv = (
                GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveAttributedGmv.from_dict(
                    _seller_live_attributed_gmv
                )
            )

        _seller_live_gmv = d.pop("seller_live_gmv", UNSET)
        seller_live_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveGmv | Unset
        if isinstance(_seller_live_gmv, Unset):
            seller_live_gmv = UNSET
        else:
            seller_live_gmv = GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveGmv.from_dict(
                _seller_live_gmv
            )

        _seller_live_indirect_gmv = d.pop("seller_live_indirect_gmv", UNSET)
        seller_live_indirect_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveIndirectGmv | Unset
        if isinstance(_seller_live_indirect_gmv, Unset):
            seller_live_indirect_gmv = UNSET
        else:
            seller_live_indirect_gmv = (
                GetShopPerformanceResponseDataPerformanceIntervalSaleSellerLiveIndirectGmv.from_dict(
                    _seller_live_indirect_gmv
                )
            )

        _seller_video_attributed_gmv = d.pop("seller_video_attributed_gmv", UNSET)
        seller_video_attributed_gmv: (
            GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoAttributedGmv | Unset
        )
        if isinstance(_seller_video_attributed_gmv, Unset):
            seller_video_attributed_gmv = UNSET
        else:
            seller_video_attributed_gmv = (
                GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoAttributedGmv.from_dict(
                    _seller_video_attributed_gmv
                )
            )

        _seller_video_gmv = d.pop("seller_video_gmv", UNSET)
        seller_video_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoGmv | Unset
        if isinstance(_seller_video_gmv, Unset):
            seller_video_gmv = UNSET
        else:
            seller_video_gmv = GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoGmv.from_dict(
                _seller_video_gmv
            )

        _seller_video_indirect_gmv = d.pop("seller_video_indirect_gmv", UNSET)
        seller_video_indirect_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoIndirectGmv | Unset
        if isinstance(_seller_video_indirect_gmv, Unset):
            seller_video_indirect_gmv = UNSET
        else:
            seller_video_indirect_gmv = (
                GetShopPerformanceResponseDataPerformanceIntervalSaleSellerVideoIndirectGmv.from_dict(
                    _seller_video_indirect_gmv
                )
            )

        _shipping_fees = d.pop("shipping_fees", UNSET)
        shipping_fees: ShippingFee | Unset
        if isinstance(_shipping_fees, Unset):
            shipping_fees = UNSET
        else:
            shipping_fees = ShippingFee.from_dict(_shipping_fees)

        sku_orders_count = d.pop("sku_orders_count", UNSET)

        _tax = d.pop("tax", UNSET)
        tax: Tax | Unset
        if isinstance(_tax, Unset):
            tax = UNSET
        else:
            tax = Tax.from_dict(_tax)

        _video_attributed_gmv = d.pop("video_attributed_gmv", UNSET)
        video_attributed_gmv: VideoAttributedGmv | Unset
        if isinstance(_video_attributed_gmv, Unset):
            video_attributed_gmv = UNSET
        else:
            video_attributed_gmv = VideoAttributedGmv.from_dict(_video_attributed_gmv)

        _video_gmv = d.pop("video_gmv", UNSET)
        video_gmv: GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv | Unset
        if isinstance(_video_gmv, Unset):
            video_gmv = UNSET
        else:
            video_gmv = GetShopPerformanceResponseDataPerformanceIntervalSaleVideoGmv.from_dict(_video_gmv)

        _video_indirect_gmv = d.pop("video_indirect_gmv", UNSET)
        video_indirect_gmv: VideoIndirectGmv | Unset
        if isinstance(_video_indirect_gmv, Unset):
            video_indirect_gmv = UNSET
        else:
            video_indirect_gmv = VideoIndirectGmv.from_dict(_video_indirect_gmv)

        get_shop_performance_response_data_performance_interval_sale = cls(
            avg_order_value=avg_order_value,
            avg_sku_order_value=avg_sku_order_value,
            cancellations_and_returns=cancellations_and_returns,
            creator_live_attributed_gmv=creator_live_attributed_gmv,
            creator_live_gmv=creator_live_gmv,
            creator_live_indirect_gmv=creator_live_indirect_gmv,
            creator_video_attributed_gmv=creator_video_attributed_gmv,
            creator_video_gmv=creator_video_gmv,
            creator_video_indirect_gmv=creator_video_indirect_gmv,
            customers_count=customers_count,
            gmv=gmv,
            gmv_with_tax=gmv_with_tax,
            gmv_with_tiktok_co_funding=gmv_with_tiktok_co_funding,
            items_sold=items_sold,
            live_attributed_gmv=live_attributed_gmv,
            live_gmv=live_gmv,
            live_indirect_gmv=live_indirect_gmv,
            orders_count=orders_count,
            product_card_attributed_gmv=product_card_attributed_gmv,
            refunds=refunds,
            seller_live_attributed_gmv=seller_live_attributed_gmv,
            seller_live_gmv=seller_live_gmv,
            seller_live_indirect_gmv=seller_live_indirect_gmv,
            seller_video_attributed_gmv=seller_video_attributed_gmv,
            seller_video_gmv=seller_video_gmv,
            seller_video_indirect_gmv=seller_video_indirect_gmv,
            shipping_fees=shipping_fees,
            sku_orders_count=sku_orders_count,
            tax=tax,
            video_attributed_gmv=video_attributed_gmv,
            video_gmv=video_gmv,
            video_indirect_gmv=video_indirect_gmv,
        )

        get_shop_performance_response_data_performance_interval_sale.additional_properties = d
        return get_shop_performance_response_data_performance_interval_sale

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
