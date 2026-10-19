from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GiftDetail")


@_attrs_define
class GiftDetail:
    """
    Attributes:
        product_id (str): TikTok Shop product id of gift.
        sku_id (str): TikTok Shop sku id of gift.
        total_claim_limit (str): The total claim limit for the gift SKU in this activity. Enter an integer from `1` to
            `99999`.
    """

    product_id: str
    sku_id: str
    total_claim_limit: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        sku_id = self.sku_id

        total_claim_limit = self.total_claim_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_id": product_id,
                "sku_id": sku_id,
                "total_claim_limit": total_claim_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id")

        sku_id = d.pop("sku_id")

        total_claim_limit = d.pop("total_claim_limit")

        gift_detail = cls(
            product_id=product_id,
            sku_id=sku_id,
            total_claim_limit=total_claim_limit,
        )

        gift_detail.additional_properties = d
        return gift_detail

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
