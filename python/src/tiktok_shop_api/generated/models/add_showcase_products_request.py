from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddShowcaseProductsRequest")


@_attrs_define
class AddShowcaseProductsRequest:
    """
    Attributes:
        add_type (str): Specifies how products are added to the showcase. This an enumerated type with values:
            - PRODUCT_ID
            - PRODUCT_LINK
        product_ids (list[str] | Unset): A list of product identifiers included if `add_type` is set to `PRODUCT_ID`.
            The products associated with the identifiers are added to the showcase. Maximum length of the list is 20 product
            identifiers.
        product_link (str | Unset): A product URL to use when `add_type` is set to `PRODUCT_LINK`. The product
            associated with the URL is added to the showcase.
    """

    add_type: str
    product_ids: list[str] | Unset = UNSET
    product_link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        add_type = self.add_type

        product_ids: list[str] | Unset = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids

        product_link = self.product_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "add_type": add_type,
            }
        )
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids
        if product_link is not UNSET:
            field_dict["product_link"] = product_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        add_type = d.pop("add_type")

        product_ids = cast(list[str], d.pop("product_ids", UNSET))

        product_link = d.pop("product_link", UNSET)

        add_showcase_products_request = cls(
            add_type=add_type,
            product_ids=product_ids,
            product_link=product_link,
        )

        add_showcase_products_request.additional_properties = d
        return add_showcase_products_request

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
