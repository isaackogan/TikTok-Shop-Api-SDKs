from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_inventory_response_data_error import UpdateInventoryResponseDataError


T = TypeVar("T", bound="UpdateInventoryResponseData")


@_attrs_define
class UpdateInventoryResponseData:
    """
    Attributes:
        errors (list[UpdateInventoryResponseDataError] | Unset): Inventory update errors for individual SKU and
            warehouse combinations. A successful top-level response can still include this list when individual updates
            fail, so inspect it before treating all updates as successful.
    """

    errors: list[UpdateInventoryResponseDataError] | Unset = UNSET
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
        from ..models.update_inventory_response_data_error import UpdateInventoryResponseDataError  # noqa: PLC0415

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[UpdateInventoryResponseDataError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = UpdateInventoryResponseDataError.from_dict(errors_item_data)

                errors.append(errors_item)

        update_inventory_response_data = cls(
            errors=errors,
        )

        update_inventory_response_data.additional_properties = d
        return update_inventory_response_data

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
