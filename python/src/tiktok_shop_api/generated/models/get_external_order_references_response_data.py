from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_order import ExternalOrder


T = TypeVar("T", bound="GetExternalOrderReferencesResponseData")


@_attrs_define
class GetExternalOrderReferencesResponseData:
    """
    Attributes:
        external_orders (list[ExternalOrder] | Unset): A list of orders that have been synced between your OMS and
            TikTok Shop.

            Note: If you've synced order information between multiple OMSs to the same TikTok Shop order, you'll retrieve
            all external order information.
    """

    external_orders: list[ExternalOrder] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.external_orders, Unset):
            external_orders = []
            for external_orders_item_data in self.external_orders:
                external_orders_item = external_orders_item_data.to_dict()
                external_orders.append(external_orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_orders is not UNSET:
            field_dict["external_orders"] = external_orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_order import ExternalOrder  # noqa: PLC0415

        d = dict(src_dict)
        _external_orders = d.pop("external_orders", UNSET)
        external_orders: list[ExternalOrder] | Unset = UNSET
        if _external_orders is not UNSET:
            external_orders = []
            for external_orders_item_data in _external_orders:
                external_orders_item = ExternalOrder.from_dict(external_orders_item_data)

                external_orders.append(external_orders_item)

        get_external_order_references_response_data = cls(
            external_orders=external_orders,
        )

        get_external_order_references_response_data.additional_properties = d
        return get_external_order_references_response_data

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
