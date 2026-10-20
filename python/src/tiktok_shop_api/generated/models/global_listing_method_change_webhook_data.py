from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalListingMethodChangeWebhookData")


@_attrs_define
class GlobalListingMethodChangeWebhookData:
    """
    Attributes:
        global_product_id (str | Unset): The global product ID associated with the local product.
        local_product_id (list[str] | Unset): The local product ID.
        listing_method (str | Unset): The listing method applicable to the local product.
             Possible values:

             * GLOBAL_PUBLISHING: Create a global product, then publish it to target local markets.
             * LOCAL_REPLICATION: Create local product, then replicate it to other target local markets.
    """

    global_product_id: str | Unset = UNSET
    local_product_id: list[str] | Unset = UNSET
    listing_method: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_product_id = self.global_product_id

        local_product_id: list[str] | Unset = UNSET
        if not isinstance(self.local_product_id, Unset):
            local_product_id = self.local_product_id

        listing_method = self.listing_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_product_id is not UNSET:
            field_dict["global_product_id"] = global_product_id
        if local_product_id is not UNSET:
            field_dict["local_product_id"] = local_product_id
        if listing_method is not UNSET:
            field_dict["listing_method"] = listing_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        global_product_id = d.pop("global_product_id", UNSET)

        local_product_id = cast(list[str], d.pop("local_product_id", UNSET))

        listing_method = d.pop("listing_method", UNSET)

        global_listing_method_change_webhook_data = cls(
            global_product_id=global_product_id,
            local_product_id=local_product_id,
            listing_method=listing_method,
        )

        global_listing_method_change_webhook_data.additional_properties = d
        return global_listing_method_change_webhook_data

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
