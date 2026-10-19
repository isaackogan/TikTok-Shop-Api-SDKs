from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.goods_match_webhook_data_match_type import GoodsMatchWebhookDataMatchType
from ..models.goods_match_webhook_data_product_type import GoodsMatchWebhookDataProductType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GoodsMatchWebhookData")


@_attrs_define
class GoodsMatchWebhookData:
    """
    Attributes:
        match_type (GoodsMatchWebhookDataMatchType | Unset): Indicates whether the seller is matching or unmatching
            products. Possible enumerations are: `MATCH` and `UNMATCH`.
        product_type (GoodsMatchWebhookDataProductType | Unset): Possible enumerations are: `LOCAL` and `GLOBAL`.
        goods_id (str | Unset): FBT Goods ID.
        product_id (str | Unset): TikTok Shop product ID.
        sku_id (str | Unset): TikTok Shop SKU ID.
        update_time (int | Unset): The time when the action occurred. Unix timestamp.
    """

    match_type: GoodsMatchWebhookDataMatchType | Unset = UNSET
    product_type: GoodsMatchWebhookDataProductType | Unset = UNSET
    goods_id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_type: str | Unset = UNSET
        if not isinstance(self.match_type, Unset):
            match_type = self.match_type.value

        product_type: str | Unset = UNSET
        if not isinstance(self.product_type, Unset):
            product_type = self.product_type.value

        goods_id = self.goods_id

        product_id = self.product_id

        sku_id = self.sku_id

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_type is not UNSET:
            field_dict["match_type"] = match_type
        if product_type is not UNSET:
            field_dict["product_type"] = product_type
        if goods_id is not UNSET:
            field_dict["goods_id"] = goods_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _match_type = d.pop("match_type", UNSET)
        match_type: GoodsMatchWebhookDataMatchType | Unset
        if isinstance(_match_type, Unset):
            match_type = UNSET
        else:
            match_type = GoodsMatchWebhookDataMatchType(_match_type)

        _product_type = d.pop("product_type", UNSET)
        product_type: GoodsMatchWebhookDataProductType | Unset
        if isinstance(_product_type, Unset):
            product_type = UNSET
        else:
            product_type = GoodsMatchWebhookDataProductType(_product_type)

        goods_id = d.pop("goods_id", UNSET)

        product_id = d.pop("product_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        update_time = d.pop("update_time", UNSET)

        goods_match_webhook_data = cls(
            match_type=match_type,
            product_type=product_type,
            goods_id=goods_id,
            product_id=product_id,
            sku_id=sku_id,
            update_time=update_time,
        )

        goods_match_webhook_data.additional_properties = d
        return goods_match_webhook_data

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
