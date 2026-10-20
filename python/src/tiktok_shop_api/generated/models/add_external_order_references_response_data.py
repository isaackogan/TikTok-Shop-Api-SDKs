from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_external_order_references_response_data_error import AddExternalOrderReferencesResponseDataError


T = TypeVar("T", bound="AddExternalOrderReferencesResponseData")


@_attrs_define
class AddExternalOrderReferencesResponseData:
    """
    Attributes:
        errors (list[AddExternalOrderReferencesResponseDataError] | Unset): Per-order errors. Each item identifies a
            TikTok Shop order and its external OMS reference that could not be processed. On a successful API response,
            references for orders not listed here are saved even when this list is non-empty.
    """

    errors: list[AddExternalOrderReferencesResponseDataError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_external_order_references_response_data_error import (
            AddExternalOrderReferencesResponseDataError,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[AddExternalOrderReferencesResponseDataError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = AddExternalOrderReferencesResponseDataError.from_dict(errors_item_data)

                errors.append(errors_item)

        add_external_order_references_response_data = cls(
            errors=errors,
        )

        add_external_order_references_response_data.additional_properties = d
        return add_external_order_references_response_data

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
