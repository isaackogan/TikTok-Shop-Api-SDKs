from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shop_performance_response_data_performance_interval_breakdown_affiliate_product_card_attributed_gmv import GetShopPerformanceResponseDataPerformanceIntervalBreakdownAffiliateProductCardAttributedGmv
  from ..models.get_shop_performance_response_data_performance_interval_breakdown_content_breakdown import GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdown
  from ..models.get_shop_performance_response_data_performance_interval_breakdown_seller_product_card_gmv import GetShopPerformanceResponseDataPerformanceIntervalBreakdownSellerProductCardGmv
  from ..models.get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search import GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearch





T = TypeVar("T", bound="GetShopPerformanceResponseDataPerformanceIntervalBreakdown")



@_attrs_define
class GetShopPerformanceResponseDataPerformanceIntervalBreakdown:
    """ 
        Attributes:
            affiliate_product_card_attributed_gmv
                (GetShopPerformanceResponseDataPerformanceIntervalBreakdownAffiliateProductCardAttributedGmv | Unset):
            content_breakdown (list[GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdown] | Unset):
                GMV breakdown by content type and channel.
            seller_product_card_gmv (GetShopPerformanceResponseDataPerformanceIntervalBreakdownSellerProductCardGmv |
                Unset):
            shop_tab_and_search (GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearch | Unset):
     """

    affiliate_product_card_attributed_gmv: GetShopPerformanceResponseDataPerformanceIntervalBreakdownAffiliateProductCardAttributedGmv | Unset = UNSET
    content_breakdown: list[GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdown] | Unset = UNSET
    seller_product_card_gmv: GetShopPerformanceResponseDataPerformanceIntervalBreakdownSellerProductCardGmv | Unset = UNSET
    shop_tab_and_search: GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_affiliate_product_card_attributed_gmv import GetShopPerformanceResponseDataPerformanceIntervalBreakdownAffiliateProductCardAttributedGmv # noqa: PLC0415
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_content_breakdown import GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdown # noqa: PLC0415
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_seller_product_card_gmv import GetShopPerformanceResponseDataPerformanceIntervalBreakdownSellerProductCardGmv # noqa: PLC0415
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search import GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearch # noqa: PLC0415
        affiliate_product_card_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affiliate_product_card_attributed_gmv, Unset):
            affiliate_product_card_attributed_gmv = self.affiliate_product_card_attributed_gmv.to_dict()

        content_breakdown: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content_breakdown, Unset):
            content_breakdown = []
            for content_breakdown_item_data in self.content_breakdown:
                content_breakdown_item = content_breakdown_item_data.to_dict()
                content_breakdown.append(content_breakdown_item)



        seller_product_card_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_product_card_gmv, Unset):
            seller_product_card_gmv = self.seller_product_card_gmv.to_dict()

        shop_tab_and_search: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop_tab_and_search, Unset):
            shop_tab_and_search = self.shop_tab_and_search.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if affiliate_product_card_attributed_gmv is not UNSET:
            field_dict["affiliate_product_card_attributed_gmv"] = affiliate_product_card_attributed_gmv
        if content_breakdown is not UNSET:
            field_dict["content_breakdown"] = content_breakdown
        if seller_product_card_gmv is not UNSET:
            field_dict["seller_product_card_gmv"] = seller_product_card_gmv
        if shop_tab_and_search is not UNSET:
            field_dict["shop_tab_and_search"] = shop_tab_and_search

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_affiliate_product_card_attributed_gmv import GetShopPerformanceResponseDataPerformanceIntervalBreakdownAffiliateProductCardAttributedGmv # noqa: PLC0415
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_content_breakdown import GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdown # noqa: PLC0415
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_seller_product_card_gmv import GetShopPerformanceResponseDataPerformanceIntervalBreakdownSellerProductCardGmv # noqa: PLC0415
        from ..models.get_shop_performance_response_data_performance_interval_breakdown_shop_tab_and_search import GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearch # noqa: PLC0415
        d = dict(src_dict)
        _affiliate_product_card_attributed_gmv = d.pop("affiliate_product_card_attributed_gmv", UNSET)
        affiliate_product_card_attributed_gmv: GetShopPerformanceResponseDataPerformanceIntervalBreakdownAffiliateProductCardAttributedGmv | Unset
        if isinstance(_affiliate_product_card_attributed_gmv,  Unset):
            affiliate_product_card_attributed_gmv = UNSET
        else:
            affiliate_product_card_attributed_gmv = GetShopPerformanceResponseDataPerformanceIntervalBreakdownAffiliateProductCardAttributedGmv.from_dict(_affiliate_product_card_attributed_gmv)




        _content_breakdown = d.pop("content_breakdown", UNSET)
        content_breakdown: list[GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdown] | Unset = UNSET
        if _content_breakdown is not UNSET:
            content_breakdown = []
            for content_breakdown_item_data in _content_breakdown:
                content_breakdown_item = GetShopPerformanceResponseDataPerformanceIntervalBreakdownContentBreakdown.from_dict(content_breakdown_item_data)



                content_breakdown.append(content_breakdown_item)


        _seller_product_card_gmv = d.pop("seller_product_card_gmv", UNSET)
        seller_product_card_gmv: GetShopPerformanceResponseDataPerformanceIntervalBreakdownSellerProductCardGmv | Unset
        if isinstance(_seller_product_card_gmv,  Unset):
            seller_product_card_gmv = UNSET
        else:
            seller_product_card_gmv = GetShopPerformanceResponseDataPerformanceIntervalBreakdownSellerProductCardGmv.from_dict(_seller_product_card_gmv)




        _shop_tab_and_search = d.pop("shop_tab_and_search", UNSET)
        shop_tab_and_search: GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearch | Unset
        if isinstance(_shop_tab_and_search,  Unset):
            shop_tab_and_search = UNSET
        else:
            shop_tab_and_search = GetShopPerformanceResponseDataPerformanceIntervalBreakdownShopTabAndSearch.from_dict(_shop_tab_and_search)




        get_shop_performance_response_data_performance_interval_breakdown = cls(
            affiliate_product_card_attributed_gmv=affiliate_product_card_attributed_gmv,
            content_breakdown=content_breakdown,
            seller_product_card_gmv=seller_product_card_gmv,
            shop_tab_and_search=shop_tab_and_search,
        )


        get_shop_performance_response_data_performance_interval_breakdown.additional_properties = d
        return get_shop_performance_response_data_performance_interval_breakdown

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
