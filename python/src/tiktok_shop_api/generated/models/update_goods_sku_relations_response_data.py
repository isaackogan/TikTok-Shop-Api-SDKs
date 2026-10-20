from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_goods_sku_relations_response_data_operate_goods_sku_relation_info import (
        UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfo,
    )


T = TypeVar("T", bound="UpdateGoodsSKURelationsResponseData")


@_attrs_define
class UpdateGoodsSKURelationsResponseData:
    """
    Attributes:
        operate_goods_sku_relation_info (UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfo | Unset):
    """

    operate_goods_sku_relation_info: UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operate_goods_sku_relation_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operate_goods_sku_relation_info, Unset):
            operate_goods_sku_relation_info = self.operate_goods_sku_relation_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operate_goods_sku_relation_info is not UNSET:
            field_dict["operate_goods_sku_relation_info"] = operate_goods_sku_relation_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_goods_sku_relations_response_data_operate_goods_sku_relation_info import (
            UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _operate_goods_sku_relation_info = d.pop("operate_goods_sku_relation_info", UNSET)
        operate_goods_sku_relation_info: UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfo | Unset
        if isinstance(_operate_goods_sku_relation_info, Unset):
            operate_goods_sku_relation_info = UNSET
        else:
            operate_goods_sku_relation_info = UpdateGoodsSKURelationsResponseDataOperateGoodsSkuRelationInfo.from_dict(
                _operate_goods_sku_relation_info
            )

        update_goods_sku_relations_response_data = cls(
            operate_goods_sku_relation_info=operate_goods_sku_relation_info,
        )

        update_goods_sku_relations_response_data.additional_properties = d
        return update_goods_sku_relations_response_data

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
