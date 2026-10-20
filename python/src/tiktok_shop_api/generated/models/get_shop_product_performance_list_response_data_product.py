from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_product_performance_list_response_data_product_affiliate_live_performance import (
        GetShopProductPerformanceListResponseDataProductAffiliateLivePerformance,
    )
    from ..models.get_shop_product_performance_list_response_data_product_affiliate_total_performance import (
        GetShopProductPerformanceListResponseDataProductAffiliateTotalPerformance,
    )
    from ..models.get_shop_product_performance_list_response_data_product_affiliate_video_performance import (
        GetShopProductPerformanceListResponseDataProductAffiliateVideoPerformance,
    )
    from ..models.get_shop_product_performance_list_response_data_product_seller_live_performance import (
        GetShopProductPerformanceListResponseDataProductSellerLivePerformance,
    )
    from ..models.get_shop_product_performance_list_response_data_product_seller_product_card_performance import (
        GetShopProductPerformanceListResponseDataProductSellerProductCardPerformance,
    )
    from ..models.get_shop_product_performance_list_response_data_product_seller_video_performance import (
        GetShopProductPerformanceListResponseDataProductSellerVideoPerformance,
    )
    from ..models.get_shop_product_performance_list_response_data_product_shop_tab_performance import (
        GetShopProductPerformanceListResponseDataProductShopTabPerformance,
    )
    from ..models.get_shop_product_performance_list_response_data_product_total_performance import (
        GetShopProductPerformanceListResponseDataProductTotalPerformance,
    )


T = TypeVar("T", bound="GetShopProductPerformanceListResponseDataProduct")


@_attrs_define
class GetShopProductPerformanceListResponseDataProduct:
    """
    Attributes:
        id (str | Unset): Product ID.
        total_performance (GetShopProductPerformanceListResponseDataProductTotalPerformance | Unset):
        seller_live_performance (GetShopProductPerformanceListResponseDataProductSellerLivePerformance | Unset):
        seller_video_performance (GetShopProductPerformanceListResponseDataProductSellerVideoPerformance | Unset):
        seller_product_card_performance (GetShopProductPerformanceListResponseDataProductSellerProductCardPerformance |
            Unset):
        affiliate_total_performance (GetShopProductPerformanceListResponseDataProductAffiliateTotalPerformance | Unset):
        affiliate_live_performance (GetShopProductPerformanceListResponseDataProductAffiliateLivePerformance | Unset):
        affiliate_video_performance (GetShopProductPerformanceListResponseDataProductAffiliateVideoPerformance | Unset):
        shop_tab_performance (GetShopProductPerformanceListResponseDataProductShopTabPerformance | Unset):
    """

    id: str | Unset = UNSET
    total_performance: GetShopProductPerformanceListResponseDataProductTotalPerformance | Unset = UNSET
    seller_live_performance: GetShopProductPerformanceListResponseDataProductSellerLivePerformance | Unset = UNSET
    seller_video_performance: GetShopProductPerformanceListResponseDataProductSellerVideoPerformance | Unset = UNSET
    seller_product_card_performance: (
        GetShopProductPerformanceListResponseDataProductSellerProductCardPerformance | Unset
    ) = UNSET
    affiliate_total_performance: GetShopProductPerformanceListResponseDataProductAffiliateTotalPerformance | Unset = (
        UNSET
    )
    affiliate_live_performance: GetShopProductPerformanceListResponseDataProductAffiliateLivePerformance | Unset = UNSET
    affiliate_video_performance: GetShopProductPerformanceListResponseDataProductAffiliateVideoPerformance | Unset = (
        UNSET
    )
    shop_tab_performance: GetShopProductPerformanceListResponseDataProductShopTabPerformance | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        total_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_performance, Unset):
            total_performance = self.total_performance.to_dict()

        seller_live_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_live_performance, Unset):
            seller_live_performance = self.seller_live_performance.to_dict()

        seller_video_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_video_performance, Unset):
            seller_video_performance = self.seller_video_performance.to_dict()

        seller_product_card_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_product_card_performance, Unset):
            seller_product_card_performance = self.seller_product_card_performance.to_dict()

        affiliate_total_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affiliate_total_performance, Unset):
            affiliate_total_performance = self.affiliate_total_performance.to_dict()

        affiliate_live_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affiliate_live_performance, Unset):
            affiliate_live_performance = self.affiliate_live_performance.to_dict()

        affiliate_video_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affiliate_video_performance, Unset):
            affiliate_video_performance = self.affiliate_video_performance.to_dict()

        shop_tab_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop_tab_performance, Unset):
            shop_tab_performance = self.shop_tab_performance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if total_performance is not UNSET:
            field_dict["total_performance"] = total_performance
        if seller_live_performance is not UNSET:
            field_dict["seller_live_performance"] = seller_live_performance
        if seller_video_performance is not UNSET:
            field_dict["seller_video_performance"] = seller_video_performance
        if seller_product_card_performance is not UNSET:
            field_dict["seller_product_card_performance"] = seller_product_card_performance
        if affiliate_total_performance is not UNSET:
            field_dict["affiliate_total_performance"] = affiliate_total_performance
        if affiliate_live_performance is not UNSET:
            field_dict["affiliate_live_performance"] = affiliate_live_performance
        if affiliate_video_performance is not UNSET:
            field_dict["affiliate_video_performance"] = affiliate_video_performance
        if shop_tab_performance is not UNSET:
            field_dict["shop_tab_performance"] = shop_tab_performance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_product_performance_list_response_data_product_affiliate_live_performance import (
            GetShopProductPerformanceListResponseDataProductAffiliateLivePerformance,  # noqa: PLC0415
        )
        from ..models.get_shop_product_performance_list_response_data_product_affiliate_total_performance import (
            GetShopProductPerformanceListResponseDataProductAffiliateTotalPerformance,  # noqa: PLC0415
        )
        from ..models.get_shop_product_performance_list_response_data_product_affiliate_video_performance import (
            GetShopProductPerformanceListResponseDataProductAffiliateVideoPerformance,  # noqa: PLC0415
        )
        from ..models.get_shop_product_performance_list_response_data_product_seller_live_performance import (
            GetShopProductPerformanceListResponseDataProductSellerLivePerformance,  # noqa: PLC0415
        )
        from ..models.get_shop_product_performance_list_response_data_product_seller_product_card_performance import (
            GetShopProductPerformanceListResponseDataProductSellerProductCardPerformance,  # noqa: PLC0415
        )
        from ..models.get_shop_product_performance_list_response_data_product_seller_video_performance import (
            GetShopProductPerformanceListResponseDataProductSellerVideoPerformance,  # noqa: PLC0415
        )
        from ..models.get_shop_product_performance_list_response_data_product_shop_tab_performance import (
            GetShopProductPerformanceListResponseDataProductShopTabPerformance,  # noqa: PLC0415
        )
        from ..models.get_shop_product_performance_list_response_data_product_total_performance import (
            GetShopProductPerformanceListResponseDataProductTotalPerformance,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _total_performance = d.pop("total_performance", UNSET)
        total_performance: GetShopProductPerformanceListResponseDataProductTotalPerformance | Unset
        if isinstance(_total_performance, Unset):
            total_performance = UNSET
        else:
            total_performance = GetShopProductPerformanceListResponseDataProductTotalPerformance.from_dict(
                _total_performance
            )

        _seller_live_performance = d.pop("seller_live_performance", UNSET)
        seller_live_performance: GetShopProductPerformanceListResponseDataProductSellerLivePerformance | Unset
        if isinstance(_seller_live_performance, Unset):
            seller_live_performance = UNSET
        else:
            seller_live_performance = GetShopProductPerformanceListResponseDataProductSellerLivePerformance.from_dict(
                _seller_live_performance
            )

        _seller_video_performance = d.pop("seller_video_performance", UNSET)
        seller_video_performance: GetShopProductPerformanceListResponseDataProductSellerVideoPerformance | Unset
        if isinstance(_seller_video_performance, Unset):
            seller_video_performance = UNSET
        else:
            seller_video_performance = GetShopProductPerformanceListResponseDataProductSellerVideoPerformance.from_dict(
                _seller_video_performance
            )

        _seller_product_card_performance = d.pop("seller_product_card_performance", UNSET)
        seller_product_card_performance: (
            GetShopProductPerformanceListResponseDataProductSellerProductCardPerformance | Unset
        )
        if isinstance(_seller_product_card_performance, Unset):
            seller_product_card_performance = UNSET
        else:
            seller_product_card_performance = (
                GetShopProductPerformanceListResponseDataProductSellerProductCardPerformance.from_dict(
                    _seller_product_card_performance
                )
            )

        _affiliate_total_performance = d.pop("affiliate_total_performance", UNSET)
        affiliate_total_performance: GetShopProductPerformanceListResponseDataProductAffiliateTotalPerformance | Unset
        if isinstance(_affiliate_total_performance, Unset):
            affiliate_total_performance = UNSET
        else:
            affiliate_total_performance = (
                GetShopProductPerformanceListResponseDataProductAffiliateTotalPerformance.from_dict(
                    _affiliate_total_performance
                )
            )

        _affiliate_live_performance = d.pop("affiliate_live_performance", UNSET)
        affiliate_live_performance: GetShopProductPerformanceListResponseDataProductAffiliateLivePerformance | Unset
        if isinstance(_affiliate_live_performance, Unset):
            affiliate_live_performance = UNSET
        else:
            affiliate_live_performance = (
                GetShopProductPerformanceListResponseDataProductAffiliateLivePerformance.from_dict(
                    _affiliate_live_performance
                )
            )

        _affiliate_video_performance = d.pop("affiliate_video_performance", UNSET)
        affiliate_video_performance: GetShopProductPerformanceListResponseDataProductAffiliateVideoPerformance | Unset
        if isinstance(_affiliate_video_performance, Unset):
            affiliate_video_performance = UNSET
        else:
            affiliate_video_performance = (
                GetShopProductPerformanceListResponseDataProductAffiliateVideoPerformance.from_dict(
                    _affiliate_video_performance
                )
            )

        _shop_tab_performance = d.pop("shop_tab_performance", UNSET)
        shop_tab_performance: GetShopProductPerformanceListResponseDataProductShopTabPerformance | Unset
        if isinstance(_shop_tab_performance, Unset):
            shop_tab_performance = UNSET
        else:
            shop_tab_performance = GetShopProductPerformanceListResponseDataProductShopTabPerformance.from_dict(
                _shop_tab_performance
            )

        get_shop_product_performance_list_response_data_product = cls(
            id=id,
            total_performance=total_performance,
            seller_live_performance=seller_live_performance,
            seller_video_performance=seller_video_performance,
            seller_product_card_performance=seller_product_card_performance,
            affiliate_total_performance=affiliate_total_performance,
            affiliate_live_performance=affiliate_live_performance,
            affiliate_video_performance=affiliate_video_performance,
            shop_tab_performance=shop_tab_performance,
        )

        get_shop_product_performance_list_response_data_product.additional_properties = d
        return get_shop_product_performance_list_response_data_product

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
