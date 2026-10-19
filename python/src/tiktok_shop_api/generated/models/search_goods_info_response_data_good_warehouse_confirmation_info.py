from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_goods_info_response_data_good_merchant_declaration_info_weight import (
        SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoWeight,
    )
    from ..models.search_goods_info_response_data_good_warehouse_confirmation_info_dimension import (
        SearchGoodsInfoResponseDataGoodWarehouseConfirmationInfoDimension,
    )


T = TypeVar("T", bound="SearchGoodsInfoResponseDataGoodWarehouseConfirmationInfo")


@_attrs_define
class SearchGoodsInfoResponseDataGoodWarehouseConfirmationInfo:
    """
    Attributes:
        weight (SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoWeight | Unset):
        dimension (SearchGoodsInfoResponseDataGoodWarehouseConfirmationInfoDimension | Unset):
    """

    weight: SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoWeight | Unset = UNSET
    dimension: SearchGoodsInfoResponseDataGoodWarehouseConfirmationInfoDimension | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()

        dimension: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dimension, Unset):
            dimension = self.dimension.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight
        if dimension is not UNSET:
            field_dict["dimension"] = dimension

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_goods_info_response_data_good_merchant_declaration_info_weight import (
            SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoWeight,  # noqa: PLC0415
        )
        from ..models.search_goods_info_response_data_good_warehouse_confirmation_info_dimension import (
            SearchGoodsInfoResponseDataGoodWarehouseConfirmationInfoDimension,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _weight = d.pop("weight", UNSET)
        weight: SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoWeight | Unset
        if isinstance(_weight, Unset):
            weight = UNSET
        else:
            weight = SearchGoodsInfoResponseDataGoodMerchantDeclarationInfoWeight.from_dict(_weight)

        _dimension = d.pop("dimension", UNSET)
        dimension: SearchGoodsInfoResponseDataGoodWarehouseConfirmationInfoDimension | Unset
        if isinstance(_dimension, Unset):
            dimension = UNSET
        else:
            dimension = SearchGoodsInfoResponseDataGoodWarehouseConfirmationInfoDimension.from_dict(_dimension)

        search_goods_info_response_data_good_warehouse_confirmation_info = cls(
            weight=weight,
            dimension=dimension,
        )

        search_goods_info_response_data_good_warehouse_confirmation_info.additional_properties = d
        return search_goods_info_response_data_good_warehouse_confirmation_info

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
