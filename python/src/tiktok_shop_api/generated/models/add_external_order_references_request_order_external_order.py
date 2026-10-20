from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_external_order_references_request_order_external_order_platform import (
    AddExternalOrderReferencesRequestOrderExternalOrderPlatform,
)

if TYPE_CHECKING:
    from ..models.add_external_order_references_request_order_external_order_line_item import (
        AddExternalOrderReferencesRequestOrderExternalOrderLineItem,
    )


T = TypeVar("T", bound="AddExternalOrderReferencesRequestOrderExternalOrder")


@_attrs_define
class AddExternalOrderReferencesRequestOrderExternalOrder:
    """
    Attributes:
        id (str): The corresponding order ID in your OMS.
        platform (AddExternalOrderReferencesRequestOrderExternalOrderPlatform): The alias of your OMS.
            Possible values:
            - SHOPIFY
            - WOOCOMMERCE
            - BIGCOMMERCE
            - MAGENTO
            - SALESFORCE_COMMERCE_CLOUD
            - CHANNEL_ADVISOR
            - AMAZON
            - ORDER_MANAGEMENT_SYSTEM
            - WAREHOUSE_MANAGEMENT_SYSTEM
            - ERP_SYSTEM

            Notes:
            - To attach information from multiple OMSs to the same order in TikTok Shop, call this API multiple times, each
            with the same TikTok Shop order and a different OMS.
            - To edit the attached information for a TikTok Shop order, call the API with the same OMS.
        line_items (list[AddExternalOrderReferencesRequestOrderExternalOrderLineItem]): Max count: 100.
    """

    id: str
    platform: AddExternalOrderReferencesRequestOrderExternalOrderPlatform
    line_items: list[AddExternalOrderReferencesRequestOrderExternalOrderLineItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        platform = self.platform.value

        line_items = []
        for line_items_item_data in self.line_items:
            line_items_item = line_items_item_data.to_dict()
            line_items.append(line_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform": platform,
                "line_items": line_items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_external_order_references_request_order_external_order_line_item import (
            AddExternalOrderReferencesRequestOrderExternalOrderLineItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id")

        platform = AddExternalOrderReferencesRequestOrderExternalOrderPlatform(d.pop("platform"))

        line_items = []
        _line_items = d.pop("line_items")
        for line_items_item_data in _line_items:
            line_items_item = AddExternalOrderReferencesRequestOrderExternalOrderLineItem.from_dict(
                line_items_item_data
            )

            line_items.append(line_items_item)

        add_external_order_references_request_order_external_order = cls(
            id=id,
            platform=platform,
            line_items=line_items,
        )

        add_external_order_references_request_order_external_order.additional_properties = d
        return add_external_order_references_request_order_external_order

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
