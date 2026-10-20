from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sku_status_change_webhook_data_sku import SKUStatusChangeWebhookDataSku


T = TypeVar("T", bound="SKUStatusChangeWebhookData")


@_attrs_define
class SKUStatusChangeWebhookData:
    """
    Attributes:
        product_id (str | Unset): The ID of the product whose SKU status changed.
        skus (list[SKUStatusChangeWebhookDataSku] | Unset): The list of SKUs whose status changed.
        update_time (int | Unset): The time when the change occurred. Unix timestamp.
    """

    product_id: str | Unset = UNSET
    skus: list[SKUStatusChangeWebhookDataSku] | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if skus is not UNSET:
            field_dict["skus"] = skus
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sku_status_change_webhook_data_sku import SKUStatusChangeWebhookDataSku  # noqa: PLC0415

        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        _skus = d.pop("skus", UNSET)
        skus: list[SKUStatusChangeWebhookDataSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = SKUStatusChangeWebhookDataSku.from_dict(skus_item_data)

                skus.append(skus_item)

        update_time = d.pop("update_time", UNSET)

        sku_status_change_webhook_data = cls(
            product_id=product_id,
            skus=skus,
            update_time=update_time,
        )

        sku_status_change_webhook_data.additional_properties = d
        return sku_status_change_webhook_data

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
