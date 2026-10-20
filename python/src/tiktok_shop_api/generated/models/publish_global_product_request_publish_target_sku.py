from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fee import Fee
    from ..models.partial_edit_product_request_sku_price import PartialEditProductRequestSkuPrice
    from ..models.publish_global_product_request_publish_target_sku_inventory import (
        PublishGlobalProductRequestPublishTargetSkuInventory,
    )


T = TypeVar("T", bound="PublishGlobalProductRequestPublishTargetSku")


@_attrs_define
class PublishGlobalProductRequestPublishTargetSku:
    """
    Attributes:
        related_global_sku_id (str): The global SKU ID to be published.
            After publishing, a corresponding local product SKU will be created and linked to the global SKU.
        price (PartialEditProductRequestSkuPrice | Unset):
        inventory (PublishGlobalProductRequestPublishTargetSkuInventory | Unset):
        fees (list[Fee] | Unset): The fees required for this product based on TikTok Shop policies. Fees are required
            only for certain product categories, retrieve the requirements from the [Get Category Rules
            API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9).
    """

    related_global_sku_id: str
    price: PartialEditProductRequestSkuPrice | Unset = UNSET
    inventory: PublishGlobalProductRequestPublishTargetSkuInventory | Unset = UNSET
    fees: list[Fee] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        related_global_sku_id = self.related_global_sku_id

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        inventory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = self.inventory.to_dict()

        fees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = fees_item_data.to_dict()
                fees.append(fees_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "related_global_sku_id": related_global_sku_id,
            }
        )
        if price is not UNSET:
            field_dict["price"] = price
        if inventory is not UNSET:
            field_dict["inventory"] = inventory
        if fees is not UNSET:
            field_dict["fees"] = fees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fee import Fee  # noqa: PLC0415
        from ..models.partial_edit_product_request_sku_price import PartialEditProductRequestSkuPrice  # noqa: PLC0415
        from ..models.publish_global_product_request_publish_target_sku_inventory import (
            PublishGlobalProductRequestPublishTargetSkuInventory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        related_global_sku_id = d.pop("related_global_sku_id")

        _price = d.pop("price", UNSET)
        price: PartialEditProductRequestSkuPrice | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = PartialEditProductRequestSkuPrice.from_dict(_price)

        _inventory = d.pop("inventory", UNSET)
        inventory: PublishGlobalProductRequestPublishTargetSkuInventory | Unset
        if isinstance(_inventory, Unset):
            inventory = UNSET
        else:
            inventory = PublishGlobalProductRequestPublishTargetSkuInventory.from_dict(_inventory)

        _fees = d.pop("fees", UNSET)
        fees: list[Fee] | Unset = UNSET
        if _fees is not UNSET:
            fees = []
            for fees_item_data in _fees:
                fees_item = Fee.from_dict(fees_item_data)

                fees.append(fees_item)

        publish_global_product_request_publish_target_sku = cls(
            related_global_sku_id=related_global_sku_id,
            price=price,
            inventory=inventory,
            fees=fees,
        )

        publish_global_product_request_publish_target_sku.additional_properties = d
        return publish_global_product_request_publish_target_sku

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
