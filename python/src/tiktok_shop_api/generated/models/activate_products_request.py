from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activate_products_request_listing_platforms_item import ActivateProductsRequestListingPlatformsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivateProductsRequest")


@_attrs_define
class ActivateProductsRequest:
    """
    Attributes:
        product_ids (list[str]): The product IDs to activate.
            Max number of IDs: 20
        listing_platforms (list[ActivateProductsRequestListingPlatformsItem] | Unset): The listing platforms where the
            product will be activated.
            Possible values:
            - TOKOPEDIA
            - TIKTOK_SHOP
            Default: TIKTOK_SHOP

            Applicable only for sellers that migrated from Tokopedia.
    """

    product_ids: list[str]
    listing_platforms: list[ActivateProductsRequestListingPlatformsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_ids = self.product_ids

        listing_platforms: list[str] | Unset = UNSET
        if not isinstance(self.listing_platforms, Unset):
            listing_platforms = []
            for listing_platforms_item_data in self.listing_platforms:
                listing_platforms_item = listing_platforms_item_data.value
                listing_platforms.append(listing_platforms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "product_ids": product_ids,
            }
        )
        if listing_platforms is not UNSET:
            field_dict["listing_platforms"] = listing_platforms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_ids = cast(list[str], d.pop("product_ids"))

        _listing_platforms = d.pop("listing_platforms", UNSET)
        listing_platforms: list[ActivateProductsRequestListingPlatformsItem] | Unset = UNSET
        if _listing_platforms is not UNSET:
            listing_platforms = []
            for listing_platforms_item_data in _listing_platforms:
                listing_platforms_item = ActivateProductsRequestListingPlatformsItem(listing_platforms_item_data)

                listing_platforms.append(listing_platforms_item)

        activate_products_request = cls(
            product_ids=product_ids,
            listing_platforms=listing_platforms,
        )

        activate_products_request.additional_properties = d
        return activate_products_request

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
