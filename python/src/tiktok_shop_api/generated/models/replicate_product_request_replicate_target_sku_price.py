from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplicateProductRequestReplicateTargetSkuPrice")


@_attrs_define
class ReplicateProductRequestReplicateTargetSkuPrice:
    """
    Attributes:
        sale_price (str): The SKU's local display price shown on the product page before any discounts.
            Refer to Product Pricing for the allowed price ranges in each market.
        currency (str | Unset): The currency. You must specify the local currency in the target market.
    """

    sale_price: str
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sale_price = self.sale_price

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sale_price": sale_price,
            }
        )
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sale_price = d.pop("sale_price")

        currency = d.pop("currency", UNSET)

        replicate_product_request_replicate_target_sku_price = cls(
            sale_price=sale_price,
            currency=currency,
        )

        replicate_product_request_replicate_target_sku_price.additional_properties = d
        return replicate_product_request_replicate_target_sku_price

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
