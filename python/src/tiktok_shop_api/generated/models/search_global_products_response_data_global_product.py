from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_global_products_response_data_global_product_status import (
    SearchGlobalProductsResponseDataGlobalProductStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_global_products_response_data_global_product_sku import (
        SearchGlobalProductsResponseDataGlobalProductSku,
    )


T = TypeVar("T", bound="SearchGlobalProductsResponseDataGlobalProduct")


@_attrs_define
class SearchGlobalProductsResponseDataGlobalProduct:
    """
    Attributes:
        id (str | Unset): The global product ID in TikTok Shop.
        title (str | Unset): The product title.
        status (SearchGlobalProductsResponseDataGlobalProductStatus | Unset): The status of the product.
            Possible values:
            - PUBLISHED
            - UNPUBLISHED
            - DRAFT
            - DELETED
        skus (list[SearchGlobalProductsResponseDataGlobalProductSku] | Unset): A list of global Stock Keeping Units
            (SKUs) used to identify distinct variants of the product.
        create_time (int | Unset): The time when the product is created.
            Unix timestamp in seconds.
        update_time (int | Unset): The time when the product is last updated.
            Unix timestamp in seconds.
    """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    status: SearchGlobalProductsResponseDataGlobalProductStatus | Unset = UNSET
    skus: list[SearchGlobalProductsResponseDataGlobalProductSku] | Unset = UNSET
    create_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)

        create_time = self.create_time

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if skus is not UNSET:
            field_dict["skus"] = skus
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_global_products_response_data_global_product_sku import (
            SearchGlobalProductsResponseDataGlobalProductSku,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        _status = d.pop("status", UNSET)
        status: SearchGlobalProductsResponseDataGlobalProductStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SearchGlobalProductsResponseDataGlobalProductStatus(_status)

        _skus = d.pop("skus", UNSET)
        skus: list[SearchGlobalProductsResponseDataGlobalProductSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = SearchGlobalProductsResponseDataGlobalProductSku.from_dict(skus_item_data)

                skus.append(skus_item)

        create_time = d.pop("create_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        search_global_products_response_data_global_product = cls(
            id=id,
            title=title,
            status=status,
            skus=skus,
            create_time=create_time,
            update_time=update_time,
        )

        search_global_products_response_data_global_product.additional_properties = d
        return search_global_products_response_data_global_product

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
