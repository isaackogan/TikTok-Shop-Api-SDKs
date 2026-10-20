from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_external_order_references_response_data_error_detail_external_order import (
        AddExternalOrderReferencesResponseDataErrorDetailExternalOrder,
    )


T = TypeVar("T", bound="AddExternalOrderReferencesResponseDataErrorDetail")


@_attrs_define
class AddExternalOrderReferencesResponseDataErrorDetail:
    """
    Attributes:
        order_id (str | Unset): The unique identifier for a TikTok Shop order.
        external_order (AddExternalOrderReferencesResponseDataErrorDetailExternalOrder | Unset):
    """

    order_id: str | Unset = UNSET
    external_order: AddExternalOrderReferencesResponseDataErrorDetailExternalOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        external_order: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_order, Unset):
            external_order = self.external_order.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if external_order is not UNSET:
            field_dict["external_order"] = external_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_external_order_references_response_data_error_detail_external_order import (
            AddExternalOrderReferencesResponseDataErrorDetailExternalOrder,  # noqa: PLC0415
        )

        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        _external_order = d.pop("external_order", UNSET)
        external_order: AddExternalOrderReferencesResponseDataErrorDetailExternalOrder | Unset
        if isinstance(_external_order, Unset):
            external_order = UNSET
        else:
            external_order = AddExternalOrderReferencesResponseDataErrorDetailExternalOrder.from_dict(_external_order)

        add_external_order_references_response_data_error_detail = cls(
            order_id=order_id,
            external_order=external_order,
        )

        add_external_order_references_response_data_error_detail.additional_properties = d
        return add_external_order_references_response_data_error_detail

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
