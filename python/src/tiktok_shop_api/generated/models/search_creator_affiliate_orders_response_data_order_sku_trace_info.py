from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchCreatorAffiliateOrdersResponseDataOrderSkuTraceInfo")



@_attrs_define
class SearchCreatorAffiliateOrdersResponseDataOrderSkuTraceInfo:
    """ 
        Attributes:
            id (str | Unset): When `trace_info.type` is `GENERAL`, this is the `{eid}` provided in `sharing_link`; when
                `trace_info.type` is `SPECIFIC`, this is the `publisher_id`.
            type_ (str | Unset): For the orders coming from the sharing links for specific publishers, the value is
                `SPECIFIC`; for the orders coming from the general sharing links, the value is `GENERAL`.
     """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        search_creator_affiliate_orders_response_data_order_sku_trace_info = cls(
            id=id,
            type_=type_,
        )


        search_creator_affiliate_orders_response_data_order_sku_trace_info.additional_properties = d
        return search_creator_affiliate_orders_response_data_order_sku_trace_info

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
