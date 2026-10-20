from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.live_attributed_gmv import LiveAttributedGmv





T = TypeVar("T", bound="GetShopProductPerformanceListResponseDataProductAffiliateLivePerformance")



@_attrs_define
class GetShopProductPerformanceListResponseDataProductAffiliateLivePerformance:
    """ 
        Attributes:
            live_attributed_gmv (LiveAttributedGmv | Unset):
            new_live_count (int | Unset): Number of new live streams from affiliate.
            product_impressions (int | Unset): Product impressions from affiliate live.
            product_clicks (int | Unset): Product clicks from affiliate live.
            ctr (str | Unset): Click-through rate from affiliate live.
            add_cart_count (int | Unset): Number of times products were added to cart from affiliate live.
            add_cart_rate (str | Unset): Add to cart rate from affiliate live.
            click_order_rate (str | Unset): Click to order rate from affiliate live.
            unique_product_impressions (int | Unset): Unique product impressions from affiliate live.
            unique_clicks (int | Unset): Unique clicks from affiliate live.
            unique_ctr (str | Unset): Unique click-through rate from affiliate live.
            atc_users (int | Unset): Number of users who added to cart from affiliate live.
            unique_atc_rate (str | Unset): Unique add to cart rate from affiliate live.
            unique_click_order_rate (str | Unset): Unique click to order rate from affiliate live.
     """

    live_attributed_gmv: LiveAttributedGmv | Unset = UNSET
    new_live_count: int | Unset = UNSET
    product_impressions: int | Unset = UNSET
    product_clicks: int | Unset = UNSET
    ctr: str | Unset = UNSET
    add_cart_count: int | Unset = UNSET
    add_cart_rate: str | Unset = UNSET
    click_order_rate: str | Unset = UNSET
    unique_product_impressions: int | Unset = UNSET
    unique_clicks: int | Unset = UNSET
    unique_ctr: str | Unset = UNSET
    atc_users: int | Unset = UNSET
    unique_atc_rate: str | Unset = UNSET
    unique_click_order_rate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.live_attributed_gmv import LiveAttributedGmv # noqa: PLC0415
        live_attributed_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.live_attributed_gmv, Unset):
            live_attributed_gmv = self.live_attributed_gmv.to_dict()

        new_live_count = self.new_live_count

        product_impressions = self.product_impressions

        product_clicks = self.product_clicks

        ctr = self.ctr

        add_cart_count = self.add_cart_count

        add_cart_rate = self.add_cart_rate

        click_order_rate = self.click_order_rate

        unique_product_impressions = self.unique_product_impressions

        unique_clicks = self.unique_clicks

        unique_ctr = self.unique_ctr

        atc_users = self.atc_users

        unique_atc_rate = self.unique_atc_rate

        unique_click_order_rate = self.unique_click_order_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if live_attributed_gmv is not UNSET:
            field_dict["live_attributed_gmv"] = live_attributed_gmv
        if new_live_count is not UNSET:
            field_dict["new_live_count"] = new_live_count
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if add_cart_count is not UNSET:
            field_dict["add_cart_count"] = add_cart_count
        if add_cart_rate is not UNSET:
            field_dict["add_cart_rate"] = add_cart_rate
        if click_order_rate is not UNSET:
            field_dict["click_order_rate"] = click_order_rate
        if unique_product_impressions is not UNSET:
            field_dict["unique_product_impressions"] = unique_product_impressions
        if unique_clicks is not UNSET:
            field_dict["unique_clicks"] = unique_clicks
        if unique_ctr is not UNSET:
            field_dict["unique_ctr"] = unique_ctr
        if atc_users is not UNSET:
            field_dict["atc_users"] = atc_users
        if unique_atc_rate is not UNSET:
            field_dict["unique_atc_rate"] = unique_atc_rate
        if unique_click_order_rate is not UNSET:
            field_dict["unique_click_order_rate"] = unique_click_order_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.live_attributed_gmv import LiveAttributedGmv # noqa: PLC0415
        d = dict(src_dict)
        _live_attributed_gmv = d.pop("live_attributed_gmv", UNSET)
        live_attributed_gmv: LiveAttributedGmv | Unset
        if isinstance(_live_attributed_gmv,  Unset):
            live_attributed_gmv = UNSET
        else:
            live_attributed_gmv = LiveAttributedGmv.from_dict(_live_attributed_gmv)




        new_live_count = d.pop("new_live_count", UNSET)

        product_impressions = d.pop("product_impressions", UNSET)

        product_clicks = d.pop("product_clicks", UNSET)

        ctr = d.pop("ctr", UNSET)

        add_cart_count = d.pop("add_cart_count", UNSET)

        add_cart_rate = d.pop("add_cart_rate", UNSET)

        click_order_rate = d.pop("click_order_rate", UNSET)

        unique_product_impressions = d.pop("unique_product_impressions", UNSET)

        unique_clicks = d.pop("unique_clicks", UNSET)

        unique_ctr = d.pop("unique_ctr", UNSET)

        atc_users = d.pop("atc_users", UNSET)

        unique_atc_rate = d.pop("unique_atc_rate", UNSET)

        unique_click_order_rate = d.pop("unique_click_order_rate", UNSET)

        get_shop_product_performance_list_response_data_product_affiliate_live_performance = cls(
            live_attributed_gmv=live_attributed_gmv,
            new_live_count=new_live_count,
            product_impressions=product_impressions,
            product_clicks=product_clicks,
            ctr=ctr,
            add_cart_count=add_cart_count,
            add_cart_rate=add_cart_rate,
            click_order_rate=click_order_rate,
            unique_product_impressions=unique_product_impressions,
            unique_clicks=unique_clicks,
            unique_ctr=unique_ctr,
            atc_users=atc_users,
            unique_atc_rate=unique_atc_rate,
            unique_click_order_rate=unique_click_order_rate,
        )


        get_shop_product_performance_list_response_data_product_affiliate_live_performance.additional_properties = d
        return get_shop_product_performance_list_response_data_product_affiliate_live_performance

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
