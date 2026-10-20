from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_cap_affiliate_orders_response_data_sku_order import (
        SearchCAPAffiliateOrdersResponseDataSkuOrder,
    )


T = TypeVar("T", bound="SearchCAPAffiliateOrdersResponseData")


@_attrs_define
class SearchCAPAffiliateOrdersResponseData:
    """
    Attributes:
        sku_orders (list[SearchCAPAffiliateOrdersResponseDataSkuOrder] | Unset): SKU orders returned for the current
            page.

            For monetary fields whose names start with `actual_`, the nested `amount` can be present only when
            `settle_status` is `SETTLED` or `INELIGIBLE`. For all other statuses, the `amount` property is omitted. Even for
            `SETTLED` or `INELIGIBLE` orders, an individual `actual_*` field can still omit `amount`.
        next_page_token (str | Unset): Pagination token for the next page. The token contains only the search-after sort
            position; it does not preserve the search filters or `page_size`. If this field is returned, pass it as
            `page_token` in the next request, provide a valid `page_size`, and resend the same partner authorization context
            and request-body filters used for the first page. The `page_size` value can be set independently for each page.
            For stable pagination, explicitly provide the same fixed `create_time_ge` and `create_time_lt` values on every
            request instead of relying on the rolling default time range. Stop paginating when this field is omitted. The
            field is omitted when the returned page contains fewer records than `page_size`.
        total_count (int | Unset): Total number of SKU orders matching the current search criteria across all pages.
    """

    sku_orders: list[SearchCAPAffiliateOrdersResponseDataSkuOrder] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        field_dict.update({})
        if sku_orders is not UNSET:
            field_dict["sku_orders"] = sku_orders
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_cap_affiliate_orders_response_data_sku_order import (
            SearchCAPAffiliateOrdersResponseDataSkuOrder,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _sku_orders = d.pop("sku_orders", UNSET)
        sku_orders: list[SearchCAPAffiliateOrdersResponseDataSkuOrder] | Unset = UNSET
        if _sku_orders is not UNSET:
            sku_orders = []
            for sku_orders_item_data in _sku_orders:
                sku_orders_item = SearchCAPAffiliateOrdersResponseDataSkuOrder.from_dict(sku_orders_item_data)

                sku_orders.append(sku_orders_item)

        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        search_cap_affiliate_orders_response_data = cls(
            sku_orders=sku_orders,
            next_page_token=next_page_token,
            total_count=total_count,
        )

        search_cap_affiliate_orders_response_data.additional_properties = d
        return search_cap_affiliate_orders_response_data

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
