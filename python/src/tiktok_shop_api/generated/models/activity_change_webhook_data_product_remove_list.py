from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityChangeWebhookDataProductRemoveList")


@_attrs_define
class ActivityChangeWebhookDataProductRemoveList:
    """
    Attributes:
        product_ids (list[str] | Unset): Removed product IDs.
        sku_ids (list[str] | Unset): Removed SKU IDs.
        benefit_product_ids (list[str] | Unset): TikTokShop product ID list.
        exclude_product_ids (list[str] | Unset): IDs of the BXGY exclude products to remove.
             Max count: 100.
    """

    product_ids: list[str] | Unset = UNSET
    sku_ids: list[str] | Unset = UNSET
    benefit_product_ids: list[str] | Unset = UNSET
    exclude_product_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_ids: list[str] | Unset = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids

        sku_ids: list[str] | Unset = UNSET
        if not isinstance(self.sku_ids, Unset):
            sku_ids = self.sku_ids

        benefit_product_ids: list[str] | Unset = UNSET
        if not isinstance(self.benefit_product_ids, Unset):
            benefit_product_ids = self.benefit_product_ids

        exclude_product_ids: list[str] | Unset = UNSET
        if not isinstance(self.exclude_product_ids, Unset):
            exclude_product_ids = self.exclude_product_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids
        if sku_ids is not UNSET:
            field_dict["sku_ids"] = sku_ids
        if benefit_product_ids is not UNSET:
            field_dict["benefit_product_ids"] = benefit_product_ids
        if exclude_product_ids is not UNSET:
            field_dict["exclude_product_ids"] = exclude_product_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_ids = cast(list[str], d.pop("product_ids", UNSET))

        sku_ids = cast(list[str], d.pop("sku_ids", UNSET))

        benefit_product_ids = cast(list[str], d.pop("benefit_product_ids", UNSET))

        exclude_product_ids = cast(list[str], d.pop("exclude_product_ids", UNSET))

        activity_change_webhook_data_product_remove_list = cls(
            product_ids=product_ids,
            sku_ids=sku_ids,
            benefit_product_ids=benefit_product_ids,
            exclude_product_ids=exclude_product_ids,
        )

        activity_change_webhook_data_product_remove_list.additional_properties = d
        return activity_change_webhook_data_product_remove_list

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
