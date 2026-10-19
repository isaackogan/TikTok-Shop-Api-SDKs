from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShowcaseProductsResponseDataProductStatus")


@_attrs_define
class GetShowcaseProductsResponseDataProductStatus:
    """
    Attributes:
        inventory_status (str | Unset): The product inventory status. This an enumerated type with values:
            - IN_STOCK
            - SOLD_OUT
        review_status (str | Unset): The product review status. This is an enumerated type with values:
            - APPROVED
            - UNDER_REVIEW
            - CHANGES_UNDER_REVIEW
            - UNAVAILABLE
            - REJECTED
            - ZERO_COMMISSION
        is_hidden (bool | Unset): Set to `false` if the product is visible in the showcase. Set to `true` if the product
            is hidden from the showcase.
        added_status (str | Unset): The product's add status for the request origin. For `SHOWCASE`, `ADDED` indicates
            that the product is in the showcase, while `REJECTED` indicates that the product is rejected for use in the
            current context. For `LIVE`, `ADDED` means the product is already in the Live room's product list (live bag),
            `NOT_ADDED` means the product can be added, and `REJECTED` means the product cannot be added.
    """

    inventory_status: str | Unset = UNSET
    review_status: str | Unset = UNSET
    is_hidden: bool | Unset = UNSET
    added_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory_status = self.inventory_status

        review_status = self.review_status

        is_hidden = self.is_hidden

        added_status = self.added_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory_status is not UNSET:
            field_dict["inventory_status"] = inventory_status
        if review_status is not UNSET:
            field_dict["review_status"] = review_status
        if is_hidden is not UNSET:
            field_dict["is_hidden"] = is_hidden
        if added_status is not UNSET:
            field_dict["added_status"] = added_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inventory_status = d.pop("inventory_status", UNSET)

        review_status = d.pop("review_status", UNSET)

        is_hidden = d.pop("is_hidden", UNSET)

        added_status = d.pop("added_status", UNSET)

        get_showcase_products_response_data_product_status = cls(
            inventory_status=inventory_status,
            review_status=review_status,
            is_hidden=is_hidden,
            added_status=added_status,
        )

        get_showcase_products_response_data_product_status.additional_properties = d
        return get_showcase_products_response_data_product_status

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
