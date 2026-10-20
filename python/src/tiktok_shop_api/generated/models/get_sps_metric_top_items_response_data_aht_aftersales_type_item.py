from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSPSMetricTopItemsResponseDataAhtAftersalesTypeItem")



@_attrs_define
class GetSPSMetricTopItemsResponseDataAhtAftersalesTypeItem:
    """ 
        Attributes:
            handle_duration_hours (str | Unset): Average handle duration in hours.
            product_id (str | Unset): Product ID.
            product_name (str | Unset): Product name.
            return_order_count (int | Unset): Total number of return orders.
            top_aftersales_type_name (str | Unset): Top aftersales type returned by TikTok Shop aftersales classification.
            top_type_order_count (int | Unset): Number of orders associated with the top aftersales type.
            image_url (str | Unset): Product image URL.
     """

    handle_duration_hours: str | Unset = UNSET
    product_id: str | Unset = UNSET
    product_name: str | Unset = UNSET
    return_order_count: int | Unset = UNSET
    top_aftersales_type_name: str | Unset = UNSET
    top_type_order_count: int | Unset = UNSET
    image_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        handle_duration_hours = self.handle_duration_hours

        product_id = self.product_id

        product_name = self.product_name

        return_order_count = self.return_order_count

        top_aftersales_type_name = self.top_aftersales_type_name

        top_type_order_count = self.top_type_order_count

        image_url = self.image_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if handle_duration_hours is not UNSET:
            field_dict["handle_duration_hours"] = handle_duration_hours
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if return_order_count is not UNSET:
            field_dict["return_order_count"] = return_order_count
        if top_aftersales_type_name is not UNSET:
            field_dict["top_aftersales_type_name"] = top_aftersales_type_name
        if top_type_order_count is not UNSET:
            field_dict["top_type_order_count"] = top_type_order_count
        if image_url is not UNSET:
            field_dict["image_url"] = image_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handle_duration_hours = d.pop("handle_duration_hours", UNSET)

        product_id = d.pop("product_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        return_order_count = d.pop("return_order_count", UNSET)

        top_aftersales_type_name = d.pop("top_aftersales_type_name", UNSET)

        top_type_order_count = d.pop("top_type_order_count", UNSET)

        image_url = d.pop("image_url", UNSET)

        get_sps_metric_top_items_response_data_aht_aftersales_type_item = cls(
            handle_duration_hours=handle_duration_hours,
            product_id=product_id,
            product_name=product_name,
            return_order_count=return_order_count,
            top_aftersales_type_name=top_aftersales_type_name,
            top_type_order_count=top_type_order_count,
            image_url=image_url,
        )


        get_sps_metric_top_items_response_data_aht_aftersales_type_item.additional_properties = d
        return get_sps_metric_top_items_response_data_aht_aftersales_type_item

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
