from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_goods_info_response_data_good import SearchGoodsInfoResponseDataGood





T = TypeVar("T", bound="SearchGoodsInfoResponseData")



@_attrs_define
class SearchGoodsInfoResponseData:
    """ 
        Attributes:
            next_page_token (str | Unset): An opaque token used to retrieve the next page. When this value is non-empty,
                pass it unchanged in the next request's `page_token`. An empty string means there are no more pages.
            total_count (int | Unset): The total number of goods that meet the query conditions.
            goods (list[SearchGoodsInfoResponseDataGood] | Unset): A list of detailed information for Fulfilled by TikTok
                goods.
     """

    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    goods: list[SearchGoodsInfoResponseDataGood] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_goods_info_response_data_good import SearchGoodsInfoResponseDataGood # noqa: PLC0415
        next_page_token = self.next_page_token

        total_count = self.total_count

        goods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.goods, Unset):
            goods = []
            for goods_item_data in self.goods:
                goods_item = goods_item_data.to_dict()
                goods.append(goods_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if goods is not UNSET:
            field_dict["goods"] = goods

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_goods_info_response_data_good import SearchGoodsInfoResponseDataGood # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _goods = d.pop("goods", UNSET)
        goods: list[SearchGoodsInfoResponseDataGood] | Unset = UNSET
        if _goods is not UNSET:
            goods = []
            for goods_item_data in _goods:
                goods_item = SearchGoodsInfoResponseDataGood.from_dict(goods_item_data)



                goods.append(goods_item)


        search_goods_info_response_data = cls(
            next_page_token=next_page_token,
            total_count=total_count,
            goods=goods,
        )


        search_goods_info_response_data.additional_properties = d
        return search_goods_info_response_data

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
