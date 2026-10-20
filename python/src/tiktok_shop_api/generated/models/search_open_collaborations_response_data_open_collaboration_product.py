from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.original_price import OriginalPrice


T = TypeVar("T", bound="SearchOpenCollaborationsResponseDataOpenCollaborationProduct")


@_attrs_define
class SearchOpenCollaborationsResponseDataOpenCollaborationProduct:
    """
    Attributes:
        id (str | Unset): Product's unique id.
        title (str | Unset): Product's name.
        main_image_url (str | Unset): The product image url.
        status (str | Unset): Product's status.
            Field values:
            - LIVE: When the product is normal for sale, return to the LIVE status
            - OUT_OF_STOCK: When the product is out of stock for the consumer, the OUT_OF_STOCK state is returned
            - SELLER_DEACTIVATE:  When the product is deactivated by the merchant, the SELLER_DEACTIVATE status is returned
            - PLATFORM_DEACTIVATE: When the product is deactivated by the platform or is not available for sale, the
            PLATFORM_DEACTIVATE status is returned
            - GNE_REJECT: When the product is governed or the open collaboration is dismissed, the GNE_REJECT state is
            returned
            - DELETE: When the product is deleted, the DELETE status is returned
            - OTHER: When the product is in an unsaleable state, such as draft, frozen, review, etc, the OTHER status is
            returned
        inventory (int | Unset): The inventory of this product.
        original_price (OriginalPrice | Unset):
    """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    main_image_url: str | Unset = UNSET
    status: str | Unset = UNSET
    inventory: int | Unset = UNSET
    original_price: OriginalPrice | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        main_image_url = self.main_image_url

        status = self.status

        inventory = self.inventory

        original_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_price, Unset):
            original_price = self.original_price.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if main_image_url is not UNSET:
            field_dict["main_image_url"] = main_image_url
        if status is not UNSET:
            field_dict["status"] = status
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if original_price is not UNSET:
            field_dict["original_price"] = original_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.original_price import OriginalPrice  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        main_image_url = d.pop("main_image_url", UNSET)

        status = d.pop("status", UNSET)

        inventory = d.pop("inventory", UNSET)

        _original_price = d.pop("original_price", UNSET)
        original_price: OriginalPrice | Unset
        if isinstance(_original_price, Unset):
            original_price = UNSET
        else:
            original_price = OriginalPrice.from_dict(_original_price)

        search_open_collaborations_response_data_open_collaboration_product = cls(
            id=id,
            title=title,
            main_image_url=main_image_url,
            status=status,
            inventory=inventory,
            original_price=original_price,
        )

        search_open_collaborations_response_data_open_collaboration_product.additional_properties = d
        return search_open_collaborations_response_data_open_collaboration_product

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
