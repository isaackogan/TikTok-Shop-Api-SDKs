from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.combined_listing_change_webhook_data_change_type import CombinedListingChangeWebhookDataChangeType
from ..models.combined_listing_change_webhook_data_status import CombinedListingChangeWebhookDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.combined_listing_change_webhook_data_product import CombinedListingChangeWebhookDataProduct


T = TypeVar("T", bound="CombinedListingChangeWebhookData")


@_attrs_define
class CombinedListingChangeWebhookData:
    """
    Attributes:
        combined_listing_id (str | Unset): The combined listing ID.
        products (list[CombinedListingChangeWebhookDataProduct] | Unset): The current list of products in this combined
            listing after the change.
        status (CombinedListingChangeWebhookDataStatus | Unset): The status of the combined listing.
             Possible values:

             * LIVE
             * SYSTEM_DEACTIVATED
             * SELLER_DEACTIVATED
             * DELETED

             Note: Only products in LIVE combined listings will appear on the product display page.
        change_type (CombinedListingChangeWebhookDataChangeType | Unset): The type of change made to this combined
            listing.
             Possible values:

             * CREATE: The combined listing was created.
             * UPDATE: The combined listing was updated to add or remove products.
             * DELETE: The combined listing was deleted.
        added_product_ids (list[str] | Unset): The list of products that were newly added to the combined listing.
        removed_product_ids (list[str] | Unset): The list of products that were removed from the combined listing.
    """

    combined_listing_id: str | Unset = UNSET
    products: list[CombinedListingChangeWebhookDataProduct] | Unset = UNSET
    status: CombinedListingChangeWebhookDataStatus | Unset = UNSET
    change_type: CombinedListingChangeWebhookDataChangeType | Unset = UNSET
    added_product_ids: list[str] | Unset = UNSET
    removed_product_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        combined_listing_id = self.combined_listing_id

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        change_type: str | Unset = UNSET
        if not isinstance(self.change_type, Unset):
            change_type = self.change_type.value

        added_product_ids: list[str] | Unset = UNSET
        if not isinstance(self.added_product_ids, Unset):
            added_product_ids = self.added_product_ids

        removed_product_ids: list[str] | Unset = UNSET
        if not isinstance(self.removed_product_ids, Unset):
            removed_product_ids = self.removed_product_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if combined_listing_id is not UNSET:
            field_dict["combined_listing_id"] = combined_listing_id
        if products is not UNSET:
            field_dict["products"] = products
        if status is not UNSET:
            field_dict["status"] = status
        if change_type is not UNSET:
            field_dict["change_type"] = change_type
        if added_product_ids is not UNSET:
            field_dict["added_product_ids"] = added_product_ids
        if removed_product_ids is not UNSET:
            field_dict["removed_product_ids"] = removed_product_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.combined_listing_change_webhook_data_product import (
            CombinedListingChangeWebhookDataProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        combined_listing_id = d.pop("combined_listing_id", UNSET)

        _products = d.pop("products", UNSET)
        products: list[CombinedListingChangeWebhookDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = CombinedListingChangeWebhookDataProduct.from_dict(products_item_data)

                products.append(products_item)

        _status = d.pop("status", UNSET)
        status: CombinedListingChangeWebhookDataStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CombinedListingChangeWebhookDataStatus(_status)

        _change_type = d.pop("change_type", UNSET)
        change_type: CombinedListingChangeWebhookDataChangeType | Unset
        if isinstance(_change_type, Unset):
            change_type = UNSET
        else:
            change_type = CombinedListingChangeWebhookDataChangeType(_change_type)

        added_product_ids = cast(list[str], d.pop("added_product_ids", UNSET))

        removed_product_ids = cast(list[str], d.pop("removed_product_ids", UNSET))

        combined_listing_change_webhook_data = cls(
            combined_listing_id=combined_listing_id,
            products=products,
            status=status,
            change_type=change_type,
            added_product_ids=added_product_ids,
            removed_product_ids=removed_product_ids,
        )

        combined_listing_change_webhook_data.additional_properties = d
        return combined_listing_change_webhook_data

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
