from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_goods_sku_relations_response_data_operate_goods_sku_relation_info_operate_result_list import (
        UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfoOperateResultList,
    )


T = TypeVar("T", bound="UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfo")


@_attrs_define
class UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfo:
    """
    Attributes:
        operate_result_list (list[UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfoOperateResultList] |
            Unset): Goods-SKU relation results, including the goods ID, SKU ID, success status, and failure reason when
            applicable.
    """

    operate_result_list: (
        list[UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfoOperateResultList] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operate_result_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.operate_result_list, Unset):
            operate_result_list = []
            for operate_result_list_item_data in self.operate_result_list:
                operate_result_list_item = operate_result_list_item_data.to_dict()
                operate_result_list.append(operate_result_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operate_result_list is not UNSET:
            field_dict["operate_result_list"] = operate_result_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_goods_sku_relations_response_data_operate_goods_sku_relation_info_operate_result_list import (
            UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfoOperateResultList,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _operate_result_list = d.pop("operate_result_list", UNSET)
        operate_result_list: (
            list[UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfoOperateResultList] | Unset
        ) = UNSET
        if _operate_result_list is not UNSET:
            operate_result_list = []
            for operate_result_list_item_data in _operate_result_list:
                operate_result_list_item = (
                    UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfoOperateResultList.from_dict(
                        operate_result_list_item_data
                    )
                )

                operate_result_list.append(operate_result_list_item)

        update_goods_sku_relations_response_data_operate_goods_sku_relation_info = cls(
            operate_result_list=operate_result_list,
        )

        update_goods_sku_relations_response_data_operate_goods_sku_relation_info.additional_properties = d
        return update_goods_sku_relations_response_data_operate_goods_sku_relation_info

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
