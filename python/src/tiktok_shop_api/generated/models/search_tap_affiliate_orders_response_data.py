from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_tap_affiliate_orders_response_data_sku_order import SearchTAPAffiliateOrdersResponseDataSkuOrder





T = TypeVar("T", bound="SearchTAPAffiliateOrdersResponseData")



@_attrs_define
class SearchTAPAffiliateOrdersResponseData:
    """ 
        Attributes:
            sku_orders (list[SearchTAPAffiliateOrdersResponseDataSkuOrder] | Unset): SKU-level affiliate order records.
                Estimated commission amount fields are populated when the corresponding estimated component is available. Actual
                commission amount fields are populated only for `SETTLED` or `INELIGIBLE` orders and are omitted before those
                states; an individual actual amount can still be omitted when its underlying component is unavailable.
            next_page_token (str | Unset): Pass this pagination token as `page_token` in the next request. Reuse the same
                `campaign_id` (if specified), `create_time_ge`, and `create_time_lt` values for every page; specify both time
                bounds in the first request to keep the search window fixed. Stop paginating when this field is omitted.
            total_count (int | Unset): The total number of SKU orders matching the request filters across all pages.
     """

    sku_orders: list[SearchTAPAffiliateOrdersResponseDataSkuOrder] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_tap_affiliate_orders_response_data_sku_order import SearchTAPAffiliateOrdersResponseDataSkuOrder # noqa: PLC0415
        sku_orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sku_orders, Unset):
            sku_orders = []
            for sku_orders_item_data in self.sku_orders:
                sku_orders_item = sku_orders_item_data.to_dict()
                sku_orders.append(sku_orders_item)



        next_page_token = self.next_page_token

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sku_orders is not UNSET:
            field_dict["sku_orders"] = sku_orders
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_tap_affiliate_orders_response_data_sku_order import SearchTAPAffiliateOrdersResponseDataSkuOrder # noqa: PLC0415
        d = dict(src_dict)
        _sku_orders = d.pop("sku_orders", UNSET)
        sku_orders: list[SearchTAPAffiliateOrdersResponseDataSkuOrder] | Unset = UNSET
        if _sku_orders is not UNSET:
            sku_orders = []
            for sku_orders_item_data in _sku_orders:
                sku_orders_item = SearchTAPAffiliateOrdersResponseDataSkuOrder.from_dict(sku_orders_item_data)



                sku_orders.append(sku_orders_item)


        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        search_tap_affiliate_orders_response_data = cls(
            sku_orders=sku_orders,
            next_page_token=next_page_token,
            total_count=total_count,
        )


        search_tap_affiliate_orders_response_data.additional_properties = d
        return search_tap_affiliate_orders_response_data

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
