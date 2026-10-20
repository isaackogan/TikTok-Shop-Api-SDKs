from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EditOpenCollaborationSettingsRequestAutoAddProduct")


@_attrs_define
class EditOpenCollaborationSettingsRequestAutoAddProduct:
    """
    Attributes:
        enable (bool): Set to `true` if products are automatically added to affiliate open collaboration plans. The
            seller can add existing non-affiliate products to open collaboration at one time, and future products are added
            automatically. Set to `false` if otherwise.
        commission_rate (int): The commission rate in hundredths of a percent. For example, `3587` is a commission rate
            of `35.87%`. This value must a minimum of `100` and a maximum of `8000`. Not that setting the `enable` property
            to `false` overrides this property.
    """

    enable: bool
    commission_rate: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        commission_rate = self.commission_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "commission_rate": commission_rate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable")

        commission_rate = d.pop("commission_rate")

        edit_open_collaboration_settings_request_auto_add_product = cls(
            enable=enable,
            commission_rate=commission_rate,
        )

        edit_open_collaboration_settings_request_auto_add_product.additional_properties = d
        return edit_open_collaboration_settings_request_auto_add_product

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
