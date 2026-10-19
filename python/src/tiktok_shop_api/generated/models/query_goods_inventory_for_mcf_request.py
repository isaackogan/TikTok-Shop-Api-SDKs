from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.query_goods_inventory_for_mcf_request_good import QueryGoodsInventoryForMCFRequestGood


T = TypeVar("T", bound="QueryGoodsInventoryForMCFRequest")


@_attrs_define
class QueryGoodsInventoryForMCFRequest:
    """
    Attributes:
        goods (list[QueryGoodsInventoryForMCFRequestGood]): Goods to query. The array must contain 1 to 50 entries.
    """

    goods: list[QueryGoodsInventoryForMCFRequestGood]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goods = []
        for goods_item_data in self.goods:
            goods_item = goods_item_data.to_dict()
            goods.append(goods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "goods": goods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_goods_inventory_for_mcf_request_good import (
            QueryGoodsInventoryForMCFRequestGood,  # noqa: PLC0415
        )

        d = dict(src_dict)
        goods = []
        _goods = d.pop("goods")
        for goods_item_data in _goods:
            goods_item = QueryGoodsInventoryForMCFRequestGood.from_dict(goods_item_data)

            goods.append(goods_item)

        query_goods_inventory_for_mcf_request = cls(
            goods=goods,
        )

        query_goods_inventory_for_mcf_request.additional_properties = d
        return query_goods_inventory_for_mcf_request

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
