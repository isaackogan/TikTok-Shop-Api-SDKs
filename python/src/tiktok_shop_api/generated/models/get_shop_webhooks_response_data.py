from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_webhooks_response_data_webhook import GetShopWebhooksResponseDataWebhook


T = TypeVar("T", bound="GetShopWebhooksResponseData")


@_attrs_define
class GetShopWebhooksResponseData:
    """
    Attributes:
        webhooks (list[GetShopWebhooksResponseDataWebhook] | Unset): The list of enabled webhooks configured for the
            shop.
        total_count (int | Unset): The total number of webhooks returned.
    """

    webhooks: list[GetShopWebhooksResponseDataWebhook] | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhooks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.webhooks, Unset):
            webhooks = []
            for webhooks_item_data in self.webhooks:
                webhooks_item = webhooks_item_data.to_dict()
                webhooks.append(webhooks_item)

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhooks is not UNSET:
            field_dict["webhooks"] = webhooks
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_webhooks_response_data_webhook import GetShopWebhooksResponseDataWebhook  # noqa: PLC0415

        d = dict(src_dict)
        _webhooks = d.pop("webhooks", UNSET)
        webhooks: list[GetShopWebhooksResponseDataWebhook] | Unset = UNSET
        if _webhooks is not UNSET:
            webhooks = []
            for webhooks_item_data in _webhooks:
                webhooks_item = GetShopWebhooksResponseDataWebhook.from_dict(webhooks_item_data)

                webhooks.append(webhooks_item)

        total_count = d.pop("total_count", UNSET)

        get_shop_webhooks_response_data = cls(
            webhooks=webhooks,
            total_count=total_count,
        )

        get_shop_webhooks_response_data.additional_properties = d
        return get_shop_webhooks_response_data

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
