from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetActivityResponseDataDiscountGiftDiscountGiftInfoGiftDetail")


@_attrs_define
class GetActivityResponseDataDiscountGiftDiscountGiftInfoGiftDetail:
    """
    Attributes:
        product_id (str | Unset): TikTok Shop product id of gift.
        sku_id (str | Unset): TikTok Shop sku ID of gift.
        total_claim_limit (str | Unset): The quantity limit of the gift sku which is involved in the activity. The range
            is [1, 99999].  If you are updating the value of an existing sku, the value cannot be decreased.
    """

    product_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    total_claim_limit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        sku_id = self.sku_id

        total_claim_limit = self.total_claim_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if total_claim_limit is not UNSET:
            field_dict["total_claim_limit"] = total_claim_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        total_claim_limit = d.pop("total_claim_limit", UNSET)

        get_activity_response_data_discount_gift_discount_gift_info_gift_detail = cls(
            product_id=product_id,
            sku_id=sku_id,
            total_claim_limit=total_claim_limit,
        )

        get_activity_response_data_discount_gift_discount_gift_info_gift_detail.additional_properties = d
        return get_activity_response_data_discount_gift_discount_gift_info_gift_detail

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
