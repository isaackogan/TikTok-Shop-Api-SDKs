from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_open_collaboration_settings_request_auto_add_product import (
        EditOpenCollaborationSettingsRequestAutoAddProduct,
    )


T = TypeVar("T", bound="EditOpenCollaborationSettingsRequest")


@_attrs_define
class EditOpenCollaborationSettingsRequest:
    """
    Attributes:
        auto_add_product (EditOpenCollaborationSettingsRequestAutoAddProduct | Unset):
    """

    auto_add_product: EditOpenCollaborationSettingsRequestAutoAddProduct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_add_product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_add_product, Unset):
            auto_add_product = self.auto_add_product.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_add_product is not UNSET:
            field_dict["auto_add_product"] = auto_add_product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_open_collaboration_settings_request_auto_add_product import (
            EditOpenCollaborationSettingsRequestAutoAddProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _auto_add_product = d.pop("auto_add_product", UNSET)
        auto_add_product: EditOpenCollaborationSettingsRequestAutoAddProduct | Unset
        if isinstance(_auto_add_product, Unset):
            auto_add_product = UNSET
        else:
            auto_add_product = EditOpenCollaborationSettingsRequestAutoAddProduct.from_dict(_auto_add_product)

        edit_open_collaboration_settings_request = cls(
            auto_add_product=auto_add_product,
        )

        edit_open_collaboration_settings_request.additional_properties = d
        return edit_open_collaboration_settings_request

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
