from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_replication_status_change_webhook_data_replicated_product import (
        GlobalReplicationStatusChangeWebhookDataReplicatedProduct,
    )


T = TypeVar("T", bound="GlobalReplicationStatusChangeWebhookData")


@_attrs_define
class GlobalReplicationStatusChangeWebhookData:
    """
    Attributes:
        source_product_id (str | Unset): The ID of the product that's being replicated to other markets.
        replicated_product (GlobalReplicationStatusChangeWebhookDataReplicatedProduct | Unset):
    """

    source_product_id: str | Unset = UNSET
    replicated_product: GlobalReplicationStatusChangeWebhookDataReplicatedProduct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_product_id = self.source_product_id

        replicated_product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.replicated_product, Unset):
            replicated_product = self.replicated_product.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_product_id is not UNSET:
            field_dict["source_product_id"] = source_product_id
        if replicated_product is not UNSET:
            field_dict["replicated_product"] = replicated_product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_replication_status_change_webhook_data_replicated_product import (
            GlobalReplicationStatusChangeWebhookDataReplicatedProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        source_product_id = d.pop("source_product_id", UNSET)

        _replicated_product = d.pop("replicated_product", UNSET)
        replicated_product: GlobalReplicationStatusChangeWebhookDataReplicatedProduct | Unset
        if isinstance(_replicated_product, Unset):
            replicated_product = UNSET
        else:
            replicated_product = GlobalReplicationStatusChangeWebhookDataReplicatedProduct.from_dict(
                _replicated_product
            )

        global_replication_status_change_webhook_data = cls(
            source_product_id=source_product_id,
            replicated_product=replicated_product,
        )

        global_replication_status_change_webhook_data.additional_properties = d
        return global_replication_status_change_webhook_data

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
