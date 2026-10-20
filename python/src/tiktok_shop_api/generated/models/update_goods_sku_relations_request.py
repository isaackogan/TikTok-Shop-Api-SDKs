from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_goods_sku_relations_request_operation_type import UpdateGoodsSKURelationsRequestOperationType

if TYPE_CHECKING:
    from ..models.update_goods_sku_relations_request_operate_goods_sku_relation_list import (
        UpdateGoodsSKURelationsRequestOperateGoodsSkuRelationList,
    )


T = TypeVar("T", bound="UpdateGoodsSKURelationsRequest")


@_attrs_define
class UpdateGoodsSKURelationsRequest:
    """
    Attributes:
        operate_goods_sku_relation_list (list[UpdateGoodsSKURelationsRequestOperateGoodsSkuRelationList]): List of goods
            and SKU relations to bind or unbind.
        operation_type (UpdateGoodsSKURelationsRequestOperationType): Operation type for the goods-SKU relation.
            Possible values: BIND (bind the listed SKUs to the goods); UN_BIND (unbind the listed SKUs from the goods).
    """

    operate_goods_sku_relation_list: list[UpdateGoodsSKURelationsRequestOperateGoodsSkuRelationList]
    operation_type: UpdateGoodsSKURelationsRequestOperationType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operate_goods_sku_relation_list = []
        for operate_goods_sku_relation_list_item_data in self.operate_goods_sku_relation_list:
            operate_goods_sku_relation_list_item = operate_goods_sku_relation_list_item_data.to_dict()
            operate_goods_sku_relation_list.append(operate_goods_sku_relation_list_item)

        operation_type = self.operation_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operate_goods_sku_relation_list": operate_goods_sku_relation_list,
                "operation_type": operation_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_goods_sku_relations_request_operate_goods_sku_relation_list import (
            UpdateGoodsSKURelationsRequestOperateGoodsSkuRelationList,  # noqa: PLC0415
        )

        d = dict(src_dict)
        operate_goods_sku_relation_list = []
        _operate_goods_sku_relation_list = d.pop("operate_goods_sku_relation_list")
        for operate_goods_sku_relation_list_item_data in _operate_goods_sku_relation_list:
            operate_goods_sku_relation_list_item = UpdateGoodsSKURelationsRequestOperateGoodsSkuRelationList.from_dict(
                operate_goods_sku_relation_list_item_data
            )

            operate_goods_sku_relation_list.append(operate_goods_sku_relation_list_item)

        operation_type = UpdateGoodsSKURelationsRequestOperationType(d.pop("operation_type"))

        update_goods_sku_relations_request = cls(
            operate_goods_sku_relation_list=operate_goods_sku_relation_list,
            operation_type=operation_type,
        )

        update_goods_sku_relations_request.additional_properties = d
        return update_goods_sku_relations_request

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
